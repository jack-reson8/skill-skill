# skill-skill

[English](README.md) | 简体中文 | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md) | [हिन्दी](README.hi.md)

![skill health](https://img.shields.io/badge/skill%20health-100%2F100-brightgreen)

一个用来写 skill 的 skill：让 skill 在实际生成时**真正起作用**，而不是堆一堆笔记。

> **新报告：[我审计了 899 个公开的 Claude skill](reports/2026-10/README.zh-CN.md)**（[English](reports/2026-10/README.md)）。很多 skill 根本没告诉模型什么时候该用它；修复已提交到上游。
>
> [![Claude skill health](reports/2026-10/chart.png)](reports/2026-10/README.zh-CN.md)

## 它能做什么

- **从真实工作中提炼。** 把用户的纠正、否决和采纳的产出，转成规则和检查项。
- **用强制机制代替建议。** 使用必交产物、关卡、脚本、在指定时刻执行的检查清单和模板。只有被某个步骤明确引用的参考资料才算数。
- **能触发的描述和名字。** 涵盖触发短语（包括中文）、1024 字符上限和重名检查。
- **静态审计**（`scripts/skill_audit.py`）。能发现不合规的名字、缺失的触发条件、重名、没有任何地方引用的孤立参考文件、失效路径、过长的正文，以及滥用全大写。
- **快速效果测试。** 针对 2–3 个真实提示词，各写 3 个可观察的效果，然后对比启用和不启用该 skill 的结果。

## 安装

在 Claude Code 中：

```
/plugin marketplace add jack-reson8/skill-skill
/plugin install skill-skill@skill-skill
```

或者作为普通 skill 文件夹安装：

```bash
git clone https://github.com/jack-reson8/skill-skill /tmp/skill-skill && cp -R /tmp/skill-skill/plugins/skill-skill/skills/skill-skill ~/.claude/skills/
```

**Codex**（CLI 或 ChatGPT 桌面应用）：

```bash
codex plugin marketplace add jack-reson8/skill-skill
codex plugin add skill-skill@skill-skill
```

或者把 `plugins/skill-skill/skills/skill-skill` 复制到 `~/.codex/skills/`。该 skill 遵循开放的 [Agent Skills](https://agentskills.io) 标准，因此可用于 Claude Code、Codex 以及任何能读取 SKILL.md 的 agent。

**其他 agent**（Cursor、Gemini CLI、GitHub Copilot，以及 skills CLI 支持的其他 agent）：

```bash
npx skills add jack-reson8/skill-skill
```

## 审计任意 skill，获得健康评分

```bash
python3 ~/.claude/skills/skill-skill/scripts/skill_audit.py path/to/skill   # or --all for ~/.claude/skills, --badge for a README badge
```

```
== bad-skill   15/100  ★☆☆☆☆
  ✗ name "Bad_Skill" must be lowercase-hyphen
  ✗ description has no "Use when…" trigger clause
  ✗ orphan: references/orphan.md is never mentioned in SKILL.md
  ✗ dangling path: references/missing.md
  · warn: 4 ALL-CAPS commands — explain the why instead

== pro-motion   100/100  ★★★★★
  ✓ no blocking issues

Average skill health: 92/100 across 6 skills
```

把任意公开仓库审计成带图表的报告： `python3 scripts/skill_report.py owner/repo`.

拿到分数了？把徽章放进你的 skill 的 README 并分享出去（`--badge` 会输出 markdown）。

除 Python 3 外无其他依赖。如需完整的评测基准和描述优化，可搭配 Anthropic 的 `skill-creator` 使用。

## 常见问题

**为什么 Claude 不使用我的 skill？** Claude 只根据 `description` 来决定是否使用。请写清 skill 做什么*以及什么时候使用*，用你的用户实际会输入的说法，并控制在 1,024 字符以内。`skill_audit.py` 会标出不满足这一点的描述。

**SKILL.md 的名字有什么规则？** 名字为 1–64 个小写字母、数字和单个连字符，并且必须与父文件夹同名（[Agent Skills 规范](https://agentskills.io/specification)）。

**它和 Anthropic 的 skill-creator 有什么不同？** skill-creator 会跑完整评测并优化描述。skill-skill 走的是快速路径：把真实工作提炼成强制机制，几秒内给出静态检查。两个可以一起用。

项目主页：https://jack-reson8.github.io/skill-skill/

## 许可证

MIT
