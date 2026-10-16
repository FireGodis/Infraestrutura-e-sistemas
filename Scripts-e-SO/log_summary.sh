#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 1 || ! -f "$1" ]]; then
  echo "Uso: $0 caminho-do-log" >&2
  exit 2
fi
printf 'Linhas: '
wc -l < "$1"
printf 'Erros: '
grep -Eic 'error|erro|fail|falha' "$1" || true
