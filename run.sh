#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
if ! command -v python3 >/dev/null 2>&1; then
    echo "Instala Python 3.10 o posterior (Debian/Ubuntu: sudo apt install python3 python3-venv)." >&2
    exit 1
fi
exec python3 start.py
