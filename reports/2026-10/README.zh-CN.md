# 我体检了 899 个公开的 Claude skill，很多没告诉模型什么时候该用它

*2026 年 10 月 · [English](README.md)*

![Claude skill health](chart.png)

一个 skill 写得再好，模型不加载也没用。模型决定加不加载，只看一个字段：`description`。我用 [skill-skill](https://github.com/jack-reson8/skill-skill) 的审计脚本，按 [Agent Skills 规范](https://agentskills.io/specification)，检查了三个最常用的 skill 仓库：**anthropics/skills**、**obra/superpowers**、**ComposioHQ/awesome-claude-skills**，一共 899 个 skill。

## 发现了什么

- **很多 skill 没写"什么时候用"。** 规范要求 description 既要写这个 skill 做什么，也要写什么时候用；Anthropic 自己的 skill-creator 也提醒过，模型本来就容易少调用 skill。官方仓库 20 个里有 3 个没写，superpowers 15 个里有 1 个，Composio 合集 864 个里有 846 个没写，大多是批量生成的。
- **规范违规很容易被忽略。** 93 个 skill 的名字带空格、大写或下划线，或者和所在文件夹不一致。官方的 `claude-api` skill，description 解析出来有 1068 个字符，超过了 1024 的上限。
- **文件引用出错的情况不多，但确实存在。** 有几个参考文件没有任何地方指向它（所以永远不会被读到），也有几个路径指向了不存在的文件。

维护得最好的两个仓库平均 96–97 分，手写的 skill 整体状况不错。问题主要集中在批量生成的 skill，以及越改越长的 description 上。

## 已经提交的修复

- [anthropics/skills#2050](https://github.com/anthropics/skills/pull/2050)：把 `claude-api` 的 description 从 1068 个字符压到 1019 个，一个触发条件都没删。
- [ComposioHQ/awesome-claude-skills#2312](https://github.com/ComposioHQ/awesome-claude-skills/pull/2312)：把 65 个 skill 的名字改成和文件夹一致。另外 28 个需要连文件夹一起改名，留给维护者决定。

## 体检你自己的 skill

```bash
git clone https://github.com/jack-reson8/skill-skill /tmp/skill-skill && cp -R /tmp/skill-skill/plugins/skill-skill/skills/skill-skill ~/.claude/skills/
python3 ~/.claude/skills/skill-skill/scripts/skill_audit.py --all --badge   # 检查本机装的所有 skill，并生成 README 徽章
python3 ~/.claude/skills/skill-skill/scripts/skill_report.py owner/repo     # 任意公开仓库 → 报告 + 图表
```

每个 skill 的详细问题见 [findings.md](findings.md)，原始数据见 [data.json](data.json)。分数只是静态检查，不代表一个 skill 好不好用。审计也可能判错，欢迎提 issue 和 PR。
