# skill-skill

A Claude skill for writing skills that **actually change what gets generated**, not piles of notes.

一个用来写 skill 的 skill：让 skill 在实际生成时真正起作用，而不是堆资料。

## What it does

- **Distil from real work.** Turns the user's corrections, rejections and accepted outputs into rules and checks.
- **Forcing functions over advice.** Uses required artifacts, gates, scripts, checklists run at a named moment, and templates. References only count when a step points to them.
- **Descriptions and names that trigger.** Covers trigger phrases (including Chinese), the 1024-char limit, and collision checks.
- **Static audit** (`scripts/skill_audit.py`). Catches bad names, missing trigger clauses, name collisions, orphan reference files that nothing points to, dangling paths, oversized bodies and ALL-CAPS overuse.
- **Quick effect test.** For 2–3 real prompts, writes 3 observable effects each, then checks them with and without the skill.

## Install

```bash
git clone https://github.com/jack-reson8/skill-skill ~/.claude/skills/skill-skill
```

## Audit any skill

```bash
python3 ~/.claude/skills/skill-skill/scripts/skill_audit.py path/to/skill   # or --all for ~/.claude/skills
```

No dependencies beyond Python 3. For full eval benchmarks and description optimisation, pair it with Anthropic's `skill-creator`.

## License

MIT
