# Claude skill health report

899 skills in 3 repos, audited with [skill-skill](https://github.com/jack-reson8/skill-skill) against the [Agent Skills spec](https://agentskills.io/specification).

| Repo | Skills | Avg health | No "when to use" in description | Spec violations (name / folder / length) | Broken file refs |
|---|---|---|---|---|---|
| [anthropics/skills](https://github.com/anthropics/skills/tree/dbd4588) | 20 | 96/100 | 15% | 10% | 1 |
| [obra/superpowers](https://github.com/obra/superpowers/tree/bb92a77) | 15 | 97/100 | 7% | 0% | 2 |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills/tree/be2a406) | 864 | 92/100 | 98% | 11% | 2 |

## Findings

**anthropics/skills**
- `skills/claude-api`: description 1068 chars > 1024
- `skills/pdf`: 1 orphan file(s) nothing points to: scripts/create_validation_image.py
- `template`: name "template-skill" ≠ folder "template"

**obra/superpowers**
- `skills/using-superpowers`: 1 orphan file(s) nothing points to: references/gemini-tools.md
- `skills/writing-skills`: 1 dangling path(s): scripts/tool.sh

**ComposioHQ/awesome-claude-skills**
- `composio-skills/-21risk-automation`: name "-21risk-automation" must be lowercase-hyphen
- `composio-skills/-2chat-automation`: name "-2chat-automation" must be lowercase-hyphen
- `composio-skills/ahrefs-automation`: name "Ahrefs Automation" must be lowercase-hyphen; name "Ahrefs Automation" ≠ folder "ahrefs-automation"
- `composio-skills/anthropic_administrator-automation`: name "anthropic_administrator-automation" must be lowercase-hyphen
- `composio-skills/apify-automation`: name "Apify Automation" must be lowercase-hyphen; name "Apify Automation" ≠ folder "apify-automation"
- `composio-skills/apollo-automation`: name "Apollo Automation" must be lowercase-hyphen; name "Apollo Automation" ≠ folder "apollo-automation"
- `composio-skills/ashby-automation`: name "Ashby Automation" must be lowercase-hyphen; name "Ashby Automation" ≠ folder "ashby-automation"
- `composio-skills/attio-automation`: name "Attio Automation" must be lowercase-hyphen; name "Attio Automation" ≠ folder "attio-automation"
- …and 87 more (see data.json)


Reproduce: `python3 scripts/skill_report.py anthropics/skills obra/superpowers ComposioHQ/awesome-claude-skills`