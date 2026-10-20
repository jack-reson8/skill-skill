# I audited 899 public Claude skills. Many never tell the model when to use them.

*October 2026 · [中文版](README.zh-CN.md)*

![Claude skill health](chart.png)

A skill only helps if the model loads it, and the model decides that from one field: the `description`. I ran [skill-skill](https://github.com/jack-reson8/skill-skill)'s audit against the [Agent Skills spec](https://agentskills.io/specification) on three of the most-used skill repos: **anthropics/skills**, **obra/superpowers** and **ComposioHQ/awesome-claude-skills** (899 skills).

## What I found

- **"When to use" is often missing.** The spec says a description "should describe both what the skill does and when to use it". Anthropic's own skill-creator warns that models tend to under-trigger skills. In the official repo 3 of 20 descriptions don't say when to use the skill. In obra/superpowers it's 1 of 15. In the 864-skill Composio collection it's 846, mostly generated in bulk.
- **Spec violations are easy to miss.** 93 skills had names with spaces, capitals or underscores, or names that didn't match their folder. The official `claude-api` description parses to 1,068 characters, above the 1,024 limit.
- **Broken file references are rare but real.** A few reference files are never pointed to (so they're never read), and a few paths point to files that don't exist.

The two best-maintained repos average 96–97/100. Hand-written skills are in good shape. The problems cluster in bulk-generated ones and in long descriptions that grew over time.

## Fixes sent upstream

- [anthropics/skills#2050](https://github.com/anthropics/skills/pull/2050): `claude-api` description 1,068 → 1,019 characters, with no trigger removed.
- [ComposioHQ/awesome-claude-skills#2312](https://github.com/ComposioHQ/awesome-claude-skills/pull/2312): 65 skill names fixed to match their folders. 28 more need a folder rename and are left to the maintainers.

## Check your own skills

```bash
git clone https://github.com/jack-reson8/skill-skill /tmp/skill-skill && cp -R /tmp/skill-skill/plugins/skill-skill/skills/skill-skill ~/.claude/skills/
python3 ~/.claude/skills/skill-skill/scripts/skill_audit.py --all --badge   # your installed skills + a README badge
python3 ~/.claude/skills/skill-skill/scripts/skill_report.py owner/repo     # any public repo → report + chart
```

Per-skill findings: [findings.md](findings.md) · raw data: [data.json](data.json). Scores are a static lint, not a judgment of how useful a skill is. The audit can be wrong; issues and PRs are welcome.
