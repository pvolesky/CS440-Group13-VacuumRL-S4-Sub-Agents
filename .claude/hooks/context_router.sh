#!/usr/bin/env bash
# UserPromptSubmit hook: injects short, task-relevant context based on keywords in the prompt.
# Input  : JSON on stdin (field "prompt"). Output: plain text on stdout, added as context.
# Config : routes.tsv (regex <TAB> snippet file in snippets/). Edit that file, not this script.
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MAX="${VACUUM_RL_MAX_SNIPPETS:-3}"

input="$(cat)"
if command -v jq >/dev/null 2>&1; then
  prompt="$(printf '%s' "$input" | jq -r '.prompt // empty' 2>/dev/null)"
else
  prompt="$input"   # fallback: match against raw JSON
fi
if [ -z "$prompt" ]; then exit 0; fi

count=0
out=""
while IFS=$'\t' read -r pattern file; do
  case "$pattern" in ""|\#*) continue ;; esac
  [ -f "$DIR/snippets/$file" ] || continue
  if printf '%s' "$prompt" | grep -qiE "$pattern"; then
    out+="$(cat "$DIR/snippets/$file")"$'\n'
    count=$((count + 1))
    if [ "$count" -ge "$MAX" ]; then break; fi
  fi
done < "$DIR/routes.tsv"

if [ -n "$out" ]; then
  printf '[context-router: task-relevant hints]\n%s' "$out"
fi
exit 0
