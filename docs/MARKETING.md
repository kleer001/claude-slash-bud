# Marketing plan — /bud

## Positioning

**One line:** `/bud` graduates a subdirectory into its own GitHub repo — history intact — then
prunes the parent.

**Tagline:** For every folder that outgrows its mother repo.
**Sub-tagline:** Split. Publish. Prune.

"Mother repo" is the project's own vocabulary — `SKILL.md` and both scripts call the parent the
mother — so the tagline speaks the same language as the tool.

**Category:** Claude Code plugin (skill). Free, MIT, install in one command.

**The wedge:** everyone who has done this by hand knows the recipe — `git subtree split`, create
the repo, push, verify, `git rm`. Nobody remembers it, and the verify step is the one people skip.
`/bud` is not "a git command you didn't know"; it is *the fifteen-minute chore you keep deferring,
done in one line, with a proof step you would not have written yourself.*

## Message pillars

Every piece of copy leans on one of these three. Never all three at once.

1. **History survives.** `git subtree split` carries the commits. The new repo is not
   `Initial commit` on top of a year of work.
2. **It refuses to lie.** Nothing destructive runs until a fresh clone of the remote is proven
   to contain every tracked file. Failure aborts with the parent untouched. Tag + bundle before
   the cut. This is the differentiator against a shell alias or a gist.
3. **It finishes the job.** README, `CLAUDE.md`, `LICENSE`, `.gitignore` written *from the code*,
   repo description set, parent pruned and pushed. Not a split — a graduation.

## Audience

| Segment | Where they are | What lands |
|---|---|---|
| Claude Code users browsing plugins | plugin marketplaces, `awesome-claude-code` lists | Pillar 3 — one command, done |
| Monorepo escapees / indie devs | r/git, Hacker News, dev.tv/blog aggregators | Pillar 1 — history intact |
| Careful engineers who distrust automation | HN comments, GitHub issues, code review culture | Pillar 2 — the safety contract |
| Agent-tooling watchers | X/Bluesky, LinkedIn, newsletters | The pattern: an agent skill that *refuses* rather than retries |

The third segment is the one that decides whether this spreads. Lead the technical write-up with
the safety contract, not the convenience.

## Channels, in priority order

1. **The repo itself.** Highest-leverage surface. Banner, one-command install, usage table above
   the fold, the safety contract as its own section, honest caveats section. Set the GitHub repo
   description and topics (`claude-code`, `claude-code-plugin`, `git`, `git-subtree`, `monorepo`,
   `developer-tools`).
2. **Claude Code plugin/skill directories.** Submit to community marketplace lists and
   `awesome-claude-code`-style indexes. Low effort, compounding, and it is where intent-driven
   discovery actually happens.
3. **Show HN / r/git / r/ClaudeAI.** One post each, spaced out, each written for its room. HN:
   the verify-before-destroy design. r/git: what `subtree split` does and does not carry. r/ClaudeAI:
   the demo.
4. **A single technical write-up.** "How to split a subdirectory into its own repo without losing
   history — and how to prove you didn't." Teaches the manual recipe honestly, then shows the
   plugin. This is the evergreen artifact everything else links to.
5. **Short demo video (60–90s).** Terminal, real repo, one command, end at the new repo's GitHub
   page with its commit history visible. The history graph *is* the proof.
6. **Cross-promotion inside the `claude-slash-*` family.** Each repo's README links the others.
   Shared visual system (same banner geometry, same black-disc mark) so they read as a suite.

## Launch sequence

**Phase 1 — the surface.** README with banner, repo description, topics, license, working
one-command install. Nothing ships before install-from-scratch is verified on a clean machine.

**Phase 2 — the proof.** Demo GIF/video and the technical write-up. Both live in the repo so
every later link has somewhere to land.

**Phase 3 — distribution.** Directory submissions first (they take time to land), then the forum
posts spaced days apart, then social.

**Phase 4 — sustain.** Answer every issue. Convert recurring questions into README sections.
Each new `claude-slash-*` skill re-exposes the whole family.

## Asset checklist

- [x] Banner, `docs/images/banner.jpg` (regenerate with `docs/images/make_banner.py`)
- [x] Square mark, `docs/images/mark.svg` — for the GitHub avatar, favicon, and social preview.
      Deliberately not a crop of the banner: that artwork is wide and low-contrast and dies in a
      square. The mark is built on `/bob`'s system instead, so the two repos read as one suite.
- [x] Public README with install, usage, safety contract, caveats
- [ ] GitHub repo description + topics set
- [ ] Demo recording
- [ ] Technical write-up
- [ ] Directory submissions

## Metrics

Vanity metrics are stars. The real signal is narrower:

- **Installs** relative to repo views — does the pitch convert?
- **Issues that describe a real split**, not an install failure — is it being used on real repos?
- **Referrals from directory listings** vs. forum spikes — which channel compounds?

A forum post produces a spike and no tail. A directory listing produces a tail and no spike.
Judge them on different clocks.

## Objections, and the honest answer

**"This is three git commands."** It is five, plus a verification step most people skip, plus the
scaffolding, plus remembering the flag order. The value is that it is done and proven, not that
it is novel.

**"I don't trust automation near `git rm`."** Correct instinct. The parent is tagged and bundled
before anything is removed, the remote is re-verified immediately before the cut, and undo is one
`git reset --hard`. Say this early and without hedging — it converts skeptics better than any
convenience claim.

**"Does it rewrite my parent's history?"** No. The subdirectory's blobs stay reachable in the
parent's past. Expunging them is `git filter-repo` plus a force-push, deliberately not automated.
Ship this caveat in the README; hiding it costs more trust than it saves.

## Copy bank

- For every folder that outgrows its mother repo.
- Split. Publish. Prune.
- It refuses to cut until it can prove the copy is complete.
- Your subfolder, with its commits, on its own.
- `git subtree split` is the easy part. Proving nothing was lost is the rest.
