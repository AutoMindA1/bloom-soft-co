#!/usr/bin/env bash
# Sketch on a throwaway branch. Keep it (PR) or nuke it (local + remote).
#
#   scripts/ideate.sh start <name>   create ideate/<name> from origin/main
#   scripts/ideate.sh keep           push current ideate/* and open a draft PR
#   scripts/ideate.sh trash          delete current ideate/* local + remote (PERMANENT)
#   scripts/ideate.sh list           show every ideate/* branch
#
# Honors $IDEATE_BASE (default: main) if you want to sketch off a non-main base.

set -euo pipefail

BASE="${IDEATE_BASE:-main}"
PREFIX="ideate/"

usage() { sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//'; }

current_branch() { git symbolic-ref --short HEAD; }

require_ideate_branch() {
  local b
  b="$(current_branch)"
  if [[ "$b" != ${PREFIX}* ]]; then
    echo "error: current branch '$b' is not an ${PREFIX}* branch" >&2
    exit 1
  fi
  printf '%s' "$b"
}

require_clean_tree() {
  if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "error: working tree has uncommitted changes. Commit, stash, or discard first." >&2
    exit 1
  fi
}

cmd="${1:-}"
case "$cmd" in
  start)
    name="${2:-}"
    if [ -z "$name" ]; then echo "usage: $0 start <name>" >&2; exit 1; fi
    require_clean_tree
    branch="${PREFIX}${name}"
    if git show-ref --quiet "refs/heads/$branch"; then
      echo "error: branch '$branch' already exists" >&2; exit 1
    fi
    git fetch origin "$BASE" --quiet
    git switch -c "$branch" "origin/$BASE"
    echo "-> on $branch (from origin/$BASE)"
    echo "   sketch freely. when done: '$0 keep' or '$0 trash'"
    ;;

  keep)
    branch="$(require_ideate_branch)"
    git push -u origin "$branch"
    if command -v gh >/dev/null 2>&1; then
      gh pr create --draft --base "$BASE" --head "$branch" \
        --title "Ideate: ${branch#$PREFIX}" \
        --body "Ideation branch promoted from \`$0 keep\`. Review or close."
    else
      remote_url="$(git remote get-url origin 2>/dev/null || echo '')"
      echo "pushed. open a PR manually (gh CLI not installed)."
      [ -n "$remote_url" ] && echo "remote: $remote_url"
    fi
    ;;

  trash)
    branch="$(require_ideate_branch)"
    echo "about to PERMANENTLY delete '$branch' (local + remote)."
    echo "any unmerged commits on this branch will be unreachable and garbage-collected."
    printf "type the branch name to confirm: "
    read -r confirm
    if [ "$confirm" != "$branch" ]; then
      echo "aborted." >&2; exit 1
    fi
    git switch "$BASE"
    git branch -D "$branch"
    if git ls-remote --exit-code --heads origin "$branch" >/dev/null 2>&1; then
      git push origin --delete "$branch"
    else
      echo "(remote branch not present)"
    fi
    echo "-> '$branch' nuked."
    ;;

  list)
    echo "local:"
    git branch --list "${PREFIX}*" | sed 's/^/  /' || true
    echo "remote:"
    git branch -r --list "origin/${PREFIX}*" | sed 's/^/  /' || true
    ;;

  ""|-h|--help) usage ;;
  *) usage; exit 1 ;;
esac
