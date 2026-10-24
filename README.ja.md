# skill-skill

[English](README.md) | [简体中文](README.zh-CN.md) | 日本語 | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md) | [हिन्दी](README.hi.md)

![skill health](https://img.shields.io/badge/skill%20health-100%2F100-brightgreen)

スキルを書くための Claude スキル。ただのメモの山ではなく、**生成結果を実際に変える**スキルを作れます。

> **新着: [公開されている 899 個の Claude スキルを監査しました](reports/2026-10/README.md)**（[中文](reports/2026-10/README.zh-CN.md)）。多くのスキルは、いつ使うべきかをモデルに伝えていません。修正は upstream に送信済みです。
>
> [![Claude skill health](reports/2026-10/chart.png)](reports/2026-10/README.md)

## できること

- **実際の作業から抽出する。** ユーザーの修正、却下、採用された出力を、ルールとチェックに変換します。
- **助言ではなく強制力を。** 必須の成果物、ゲート、スクリプト、決められたタイミングで実行するチェックリスト、テンプレートを使います。リファレンスは、いずれかのステップから参照されている場合にのみ有効とみなします。
- **きちんと発動する description と名前。** トリガーフレーズ（中国語を含む）、1024 文字の上限、名前の衝突チェックに対応します。
- **静的監査**（`scripts/skill_audit.py`）。不正な名前、トリガー条件の欠落、名前の衝突、どこからも参照されていない孤立したリファレンスファイル、リンク切れのパス、肥大化した本文、全大文字の多用を検出します。
- **簡易効果テスト。** 実際のプロンプトを 2〜3 個選び、それぞれ観察可能な効果を 3 つ書き出して、スキルあり・なしで確認します。

## インストール

Claude Code の場合:

```
/plugin marketplace add jack-reson8/skill-skill
/plugin install skill-skill@skill-skill
```

または、通常のスキルフォルダとして:

```bash
git clone https://github.com/jack-reson8/skill-skill /tmp/skill-skill && cp -R /tmp/skill-skill/plugins/skill-skill/skills/skill-skill ~/.claude/skills/
```

**Codex**（CLI または ChatGPT デスクトップアプリ）:

```bash
codex plugin marketplace add jack-reson8/skill-skill
codex plugin add skill-skill@skill-skill
```

または `plugins/skill-skill/skills/skill-skill` を `~/.codex/skills/` にコピーします。このスキルはオープンな [Agent Skills](https://agentskills.io) 標準に準拠しているため、Claude Code、Codex、SKILL.md を読み込めるあらゆるエージェントで動作します。

**その他のエージェント**（Cursor、Gemini CLI、GitHub Copilot、その他 skills CLI 対応エージェント）:

```bash
npx skills add jack-reson8/skill-skill
```

## 任意のスキルを監査してヘルススコアを取得

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

公開リポジトリを監査して、グラフ付きレポートを作成: `python3 scripts/skill_report.py owner/repo`.

スコアが出たら、スキルの README にバッジを貼って共有しましょう（`--badge` で markdown を出力します）。

Python 3 以外の依存はありません。本格的な評価ベンチマークや description の最適化には、Anthropic の `skill-creator` と併用してください。

## FAQ

**なぜ Claude は自分のスキルを使ってくれないのですか？** Claude は `description` だけを見て判断します。スキルが何をするかと*いつ使うか*を、ユーザーが実際に入力する言い回しで書き、1,024 文字以内に収めてください。`skill_audit.py` は、これを満たさない description を検出します。

**SKILL.md の名前のルールは？** 名前は小文字の英字・数字・単独のハイフンで 1〜64 文字、かつ親フォルダ名と一致する必要があります（[Agent Skills 仕様](https://agentskills.io/specification)）。

**Anthropic の skill-creator とは何が違いますか？** skill-creator は本格的な評価と description の最適化を行います。skill-skill は高速な手段で、実際の作業を強制力のある仕組みに落とし込み、数秒で静的チェックを行います。両方の併用をおすすめします。

プロジェクトページ: https://jack-reson8.github.io/skill-skill/

## ライセンス

MIT
