# /bud

A [Claude Code](https://claude.ai/code) skill that graduates a subdirectory into its own
GitHub repo — commit history intact — scaffolds it, and prunes it from the parent.

A bud grows on the parent plant, then separates and roots on its own. Sketch an MVP inside
a repo; when it outgrows the folder, `/bud <subdir>` makes it a repo.

## Install

```bash
claude plugins marketplace add kleer001/claude-slash-bud && claude plugins install bud
```

Requires `git` and an authenticated [`gh`](https://cli.github.com) CLI.

## Usage

```
/bud <subdir>                     # e.g. /bud mvp-thing
/bud <subdir> --name NAME         # repo name (default: the subdir's basename)
/bud <subdir> --public            # default is private
/bud <subdir> --dest DIR          # clone location (default: sibling of the parent repo)
```

Run it from inside the parent repo. With no argument it lists the tracked top-level
directories and asks which one.

## What it does

1. **Split** — `git subtree split` rewrites the subdirectory's history into a branch whose
   root *is* that folder.
2. **Publish** — creates the GitHub repo, pushes the split branch to `main`, clones it back
   to a fresh directory, and asserts that the clone carries every commit and every tracked file.
3. **Scaffold** — writes a README, `CLAUDE.md`, MIT `LICENSE`, and `.gitignore` from what the
   code actually is, skipping any that already exist. Commits and pushes them.
4. **Prune** — re-clones the new remote and re-checks every file, tags the parent
   `pre-bud/<name>-<stamp>`, bundles the whole parent repo to `~/.claude/bud-backups/`, then
   removes the directory, commits, and pushes.

Nothing destructive happens until a fresh clone of the new remote is proven complete. If that
check fails, the run stops with the parent untouched. Undo the prune with
`git reset --hard pre-bud/<name>-<stamp>`.

## Honest caveats

- `git rm` prunes the tip, not the past — the subdirectory's blobs remain reachable in the
  parent's history. Expunging them is `git filter-repo` plus a force-push: a different
  operation, deliberately not automated here.
- `subtree split` follows only the prefix. Anything the subdirectory imported from elsewhere
  in the parent does not come along, so the new repo may not build until those are vendored.

## No network between the two sides?

Air gap, text-only channel, no GitHub — the history still travels as a file. See
[`references/offline-transfer.md`](references/offline-transfer.md) for the `git bundle`,
`fast-export`, and `format-patch` routes, plus the no-history shortcut.

## License

MIT — see [LICENSE](LICENSE).
