"""Shared HTTP helper for the drift scripts.

Exists so the TLS fallback lives in one place. Python's OpenSSL and curl do not
always agree about a certificate chain: on a machine behind an intercepting
proxy, urllib refuses every request here ("Basic Constraints of CA cert not
marked critical") while curl accepts the same chain. curl still verifies -- this
is a different trust store, not a weaker check.

Verification is never disabled. If both transports refuse, the caller gets the
error and reports it rather than working around it.
"""

import os
import subprocess

from urllib.parse import urlparse
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

USER_AGENT = "ss13-ai-skills-drift-check"

# Only these hosts ever see the token. The unauthenticated GitHub API allows 60
# requests an hour, which a CI run can exhaust; a token lifts it. Everything here
# reads public data either way -- the token buys rate limit, not access.
TOKEN_HOSTS = ("api.github.com", "raw.githubusercontent.com")


def _auth_header(url):
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        return {}
    if urlparse(url).hostname not in TOKEN_HOSTS:
        return {}
    return {"Authorization": "Bearer %s" % token}


class Transport(object):
    """Remembers which transport worked, so one TLS failure is not re-tried per URL."""

    def __init__(self):
        self.name = "urllib"
        self._curl_checked = None

    def have_curl(self):
        if self._curl_checked is None:
            try:
                subprocess.run(["curl", "--version"],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self._curl_checked = True
            except (OSError, subprocess.SubprocessError):
                self._curl_checked = False
        return self._curl_checked

    def get(self, url, timeout):
        if self.name == "curl":
            return _curl(url, timeout)
        try:
            return _urllib(url, timeout)
        except HTTPError:
            raise                      # a 404 is an answer, not a transport failure
        except (URLError, OSError) as exc:
            if not _is_tls_trust_error(exc) or not self.have_curl():
                raise
            text = _curl(url, timeout)
            self.name = "curl"
            return text


def _urllib(url, timeout):
    headers = {"User-Agent": USER_AGENT}
    headers.update(_auth_header(url))
    request = Request(url, headers=headers)
    with urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", "replace")


def _curl(url, timeout):
    args = ["curl", "-sS", "--fail", "--max-time", str(timeout),
            "-H", "User-Agent: %s" % USER_AGENT]
    for name, value in _auth_header(url).items():
        # Passed as an argument, not an env var, so it never lands in a shell history
        # or a child process' environment beyond this call.
        args += ["-H", "%s: %s" % (name, value)]
    args.append(url)
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise OSError(result.stderr.decode("utf-8", "replace").strip() or
                      "curl exited %d" % result.returncode)
    return result.stdout.decode("utf-8", "replace")


def _is_tls_trust_error(exc):
    text = str(exc)
    return "CERTIFICATE_VERIFY_FAILED" in text or "SSL" in text
