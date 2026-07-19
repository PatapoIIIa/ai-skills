#!/bin/bash

./InstallDeps.sh

set -e
set -x

#load dep exports
#need to switch to game dir for Dockerfile weirdness
original_dir=$PWD
cd "$1"
. dependencies.sh
cd "$original_dir"

NEED_BUN_INSTALL=0
if [ -x "$HOME/.bun/bin/bun" ]; then
	export PATH="$HOME/.bun/bin:$PATH"
fi

# If Bun is not present or older than BUN_VERSION, install using the official installer.
if ! command -v bun >/dev/null 2>&1; then
	NEED_BUN_INSTALL=1
else
	INSTALLED_BUN_VERSION=$(bun --version)
	if [ "$(printf '%s\n' "$BUN_VERSION" "$INSTALLED_BUN_VERSION" | sort -V | head -n1)" != "$BUN_VERSION" ]; then
		NEED_BUN_INSTALL=1
	fi
fi

if [ "$NEED_BUN_INSTALL" = "1" ]; then
	echo "Installing Bun $BUN_VERSION..."
	curl -fsSL https://bun.sh/install | bash

	if [ -x "$HOME/.bun/bin/bun" ]; then
		export PATH="$HOME/.bun/bin:$PATH"
	else
		echo "ERROR: Bun installation failed; $HOME/.bun/bin/bun not found"
		exit 1
	fi
fi

INSTALLED_BUN_VERSION=$(bun --version)

echo "Using bun $INSTALLED_BUN_VERSION (minimum required: $BUN_VERSION)"

# rust-g: prebuilt release binaries are linked against a newer glibc than the
# TGS container ships (Debian bookworm = 2.36). An incompatible .so fails to
# load at runtime and breaks asset registration in ways that don't point back
# here, so verify with ldd and fall back to a locally built copy kept next to
# this script (build instructions: skill reference build-and-rustg.md).
echo "Fetching prebuilt rust-g $RUST_G_VERSION..."
curl -fsSL -o "$1/librust_g.so" "https://github.com/tgstation/rust-g/releases/download/$RUST_G_VERSION/librust_g.so" || rm -f "$1/librust_g.so"

if [ -f "$1/librust_g.so" ] && ! ldd "$1/librust_g.so" 2>&1 | grep -q "not found"; then
	echo "Prebuilt rust-g is compatible with this glibc."
else
	echo "Prebuilt rust-g is missing or incompatible; trying local build..."
	if [ -f "$original_dir/librust_g.so" ]; then
		cp "$original_dir/librust_g.so" "$1/librust_g.so"
		if ldd "$1/librust_g.so" 2>&1 | grep -q "not found"; then
			echo "ERROR: local librust_g.so also has unresolved libraries:"
			ldd "$1/librust_g.so" || true
			exit 1
		fi
	else
		echo "ERROR: no compatible librust_g.so available. Build it from source"
		echo "inside the container and place it in Configuration/EventScripts/."
		exit 1
	fi
fi
chmod +x "$1/librust_g.so"

# Get unzip
apt-get install -y unzip

# compile tgui
echo "Compiling tgui..."
cd "$1"
env TG_BOOTSTRAP_CACHE="$original_dir" CBT_BUILD_MODE="TGS" tools/bootstrap/javascript.sh tools/build/build.ts
