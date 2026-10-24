# Publishing a skill: lists, marketplaces, bots

Read this at step 7, before opening any listing PR. Each line is a failure or bot message we actually got while listing six skills across ~15 repos.

## Before any PR: `scripts/publish_check.py <repo> --scan` must say READY

| What broke | Who caught it | Rule |
|---|---|---|
| `description: Post — … look native and sell: Xiaohongshu …` | strict YAML loaders, skill_audit | A plain scalar can't contain `": "`. Quote the description (`publish_check` and the audit fail it). |
| Scan 78 < 80 on awesome-ai-plugins | HOL `plugin-scanner` | Ship `LICENSE` **and** `SECURITY.md` at the root *and* in every `plugins/<name>/`. That alone moves 86 → 96–100. |
| `HARDCODED_SECRET` on a skill named `waboxapp` + `-automation` | secret scanner | Data files are scanned too. `xapp-`, `sk-`, `ghp_`, `AKIA` with enough characters after them look like tokens. Compress (`.gz`) or rename report data. |
| `CLAUDE_MARKETPLACE_STRICT_INVALID` | old scanner 3.0.x | The old scanner wants root `strict`; Claude Code and newer scanners want it per plugin. Don't add it; explain in the PR. |
| Glama check on awesome-mcp-servers | bot | MCP servers must be listed and passing on glama.ai first. Only the account owner can do this. |
| `validate` failing on a fix PR (Composio) | auto-labeler | It only accepts README-only listing PRs. Put fixes and listings in separate PRs and leave a one-line note for reviewers. |
| Vercel "attempting to deploy" (sickn33) | Vercel | It's the maintainer's preview deploy for fork PRs. Ignore it. |
| Pinned plugin source (`sha`) pointed at the broken commit | buildwithclaude | After fixing a repo, re-pin every open PR that pins a commit. |
| `name` in plugin.json ≠ marketplace entry, full-width `＠` in install lines | users can't install | `publish_check` verifies both. |

## Writing the PR

- Read the list's CONTRIBUTING, PR template and `.github/workflows` first. Bots enforce what humans don't write down: alphabetical order, README-only, keyword blocklists, minimum scores.
- One open PR per list. To add another skill, append it to your open PR and leave a one-line comment, instead of opening a new PR.
- Place each entry alphabetically in the closest category, and copy the neighbours' format exactly (table row vs bullet, `*By @you*` suffix, description ≤150 chars).
- PR body: what it is (one sentence each), real-world use, proof (audit score, a report), "I am the author", plus a line saying an AI assistant prepared it on the author's behalf.
- Vendoring lists (they copy skill folders into their repo, e.g. ok-skills) also need the README count and index updated in every language the Contributing section names.
- Gates you can't meet yet: a minimum repo age (e.g. 14 days) or star count. Note them with the date they open; don't submit early.

## After: `scripts/pr_triage.py` instead of reading notifications

It sorts every open PR into ACTION (you can fix it), YOU (the account owner must act: register, authorize, sign), or WAIT (a maintainer, or an expected bot message). Fix every ACTION item, reply on the PR once, and re-run. Most bot mail is WAIT.
