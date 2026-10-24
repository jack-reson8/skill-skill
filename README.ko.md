# skill-skill

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | 한국어 | [Tiếng Việt](README.vi.md) | [हिन्दी](README.hi.md)

![skill health](https://img.shields.io/badge/skill%20health-100%2F100-brightgreen)

스킬을 쓰기 위한 Claude 스킬입니다. 메모만 잔뜩 쌓인 스킬이 아니라, **실제 생성 결과를 바꾸는** 스킬을 만들어 줍니다.

> **새 소식: [공개된 Claude 스킬 899개를 감사했습니다](reports/2026-10/README.md)** ([中文](reports/2026-10/README.zh-CN.md)). 많은 스킬이 모델에게 언제 써야 하는지를 알려주지 않습니다. 수정 사항은 업스트림에 보냈습니다.
>
> [![Claude skill health](reports/2026-10/chart.png)](reports/2026-10/README.md)

## 주요 기능

- **실제 작업에서 추출합니다.** 사용자의 수정, 거절, 채택된 결과물을 규칙과 점검 항목으로 바꿉니다.
- **조언 대신 강제 장치.** 필수 산출물, 게이트, 스크립트, 정해진 시점에 실행하는 체크리스트, 템플릿을 사용합니다. 참고 자료는 어떤 단계가 가리킬 때만 인정됩니다.
- **제대로 트리거되는 description과 이름.** 트리거 문구(중국어 포함), 1024자 제한, 이름 충돌 검사를 다룹니다.
- **정적 감사** (`scripts/skill_audit.py`). 잘못된 이름, 누락된 트리거 조건, 이름 충돌, 어디에서도 참조되지 않는 고아 참조 파일, 깨진 경로, 지나치게 긴 본문, 대문자 남용을 찾아냅니다.
- **빠른 효과 테스트.** 실제 프롬프트 2~3개에 대해 관찰 가능한 효과를 각각 3개씩 적고, 스킬이 있을 때와 없을 때를 비교해 확인합니다.

## 설치

Claude Code에서:

```
/plugin marketplace add jack-reson8/skill-skill
/plugin install skill-skill@skill-skill
```

또는 일반 스킬 폴더로:

```bash
git clone https://github.com/jack-reson8/skill-skill /tmp/skill-skill && cp -R /tmp/skill-skill/plugins/skill-skill/skills/skill-skill ~/.claude/skills/
```

**Codex** (CLI 또는 ChatGPT 데스크톱 앱):

```bash
codex plugin marketplace add jack-reson8/skill-skill
codex plugin add skill-skill@skill-skill
```

또는 `plugins/skill-skill/skills/skill-skill`을 `~/.codex/skills/`에 복사하세요. 이 스킬은 개방형 [Agent Skills](https://agentskills.io) 표준을 따르므로 Claude Code, Codex 및 SKILL.md를 읽는 모든 에이전트에서 동작합니다.

**기타 에이전트** (Cursor, Gemini CLI, GitHub Copilot 및 skills CLI가 지원하는 다른 에이전트):

```bash
npx skills add jack-reson8/skill-skill
```

## 모든 스킬을 감사하고 건강 점수 받기

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

공개 저장소를 감사해 차트가 포함된 리포트로 만들 수 있습니다: `python3 scripts/skill_report.py owner/repo`.

점수를 받았다면 스킬의 README에 배지를 달아 공유해 보세요 (`--badge`가 markdown을 출력합니다).

Python 3 외에는 의존성이 없습니다. 전체 평가 벤치마크와 description 최적화가 필요하면 Anthropic의 `skill-creator`와 함께 사용하세요.

## FAQ

**Claude가 내 스킬을 쓰지 않는 이유는?** Claude는 `description`만 보고 판단합니다. 스킬이 무엇을 하는지와 *언제 쓰는지*를 사용자가 실제로 입력하는 표현으로 적고, 1,024자 이내로 유지하세요. `skill_audit.py`가 이 조건을 충족하지 못하는 description을 알려줍니다.

**SKILL.md 이름 규칙은?** 이름은 소문자 영문, 숫자, 단일 하이픈으로 이루어진 1~64자여야 하며 상위 폴더 이름과 일치해야 합니다 ([Agent Skills 사양](https://agentskills.io/specification)).

**Anthropic의 skill-creator와 무엇이 다른가요?** skill-creator는 전체 평가와 description 최적화를 수행합니다. skill-skill은 빠른 경로로, 실제 작업을 강제 장치로 정리하고 몇 초 안에 정적 린트를 제공합니다. 둘을 함께 쓰세요.

프로젝트 페이지: https://jack-reson8.github.io/skill-skill/

## 라이선스

MIT
