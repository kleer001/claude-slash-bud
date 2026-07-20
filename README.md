# bud

A Claude Code skill: graduate a subdirectory of a repo into its own standalone
GitHub repo with history intact, scaffold it, and prune it from the parent.

Install by placing this directory at `~/.claude/skills/bud`, then invoke `/bud <subdir>`
from inside the parent repo. Requires `git` and an authenticated `gh` CLI.

See `SKILL.md` for the flow, `references/offline-transfer.md` for the no-network paths.
