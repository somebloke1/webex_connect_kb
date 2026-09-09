#!/usr/bin/env bash
set -euo pipefail
task_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$task_root"
case "${1:-}" in
  '') task_requirements=requirements.txt ;;
  --with-asr) task_requirements=requirements-asr.txt ;;
  *) echo 'Usage: scripts/setup_venv.sh [--with-asr]' >&2; exit 2 ;;
esac
command -v uv >/dev/null || { echo 'Install uv: https://docs.astral.sh/uv/getting-started/installation/' >&2; exit 2; }
if [[ ! -x .venv/bin/python ]]; then
  uv venv --python 3.13 .venv
fi
# Install, rather than sync, to preserve packages in an existing workspace venv.
uv pip install --python .venv/bin/python --require-hashes -r "$task_requirements"
.venv/bin/python scripts/transcribe.py --help >/dev/null
echo "Ready: $task_root/.venv/bin/python scripts/transcribe.py --help"
