# skill-skill

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | Tiếng Việt | [हिन्दी](README.hi.md)

<p align="center"><img src="docs/share.png" alt="skill-skill: skills that actually change output" width="100%"></p>
<p align="center"><sub>Thuộc bộ <a href="https://github.com/jack-reson8/copy-that"><b>Copy That</b></a> · cài cả bộ bằng một lệnh</sub></p>

[![skill health](https://img.shields.io/badge/skill%20health-100%2F100-brightgreen)](https://jack-reson8.github.io/skill-skill/check/)

Một Claude skill để viết skill, giúp skill **thực sự thay đổi kết quả sinh ra**, chứ không chỉ là một đống ghi chú.

> **Mới: [Tôi đã kiểm tra 899 Claude skill công khai](reports/2026-10/README.md)** ([中文](reports/2026-10/README.zh-CN.md)). Nhiều skill không hề cho model biết khi nào nên dùng chúng; các bản sửa đã được gửi lên upstream.
>
> [![Claude skill health](reports/2026-10/chart.png)](reports/2026-10/README.md)

## Tính năng

- **Chắt lọc từ công việc thực tế.** Biến các lần chỉnh sửa, từ chối và kết quả được chấp nhận của người dùng thành quy tắc và bước kiểm tra.
- **Cơ chế bắt buộc thay vì lời khuyên.** Dùng sản phẩm đầu ra bắt buộc, cổng kiểm soát (gate), script, checklist chạy vào thời điểm xác định và template. Tài liệu tham khảo chỉ được tính khi có một bước trỏ tới.
- **Description và tên gọi dễ kích hoạt.** Bao gồm cụm từ kích hoạt (cả tiếng Trung), giới hạn 1024 ký tự và kiểm tra trùng tên.
- **Kiểm tra tĩnh** (`scripts/skill_audit.py`). Phát hiện tên sai quy tắc, thiếu điều kiện kích hoạt, trùng tên, file tham khảo mồ côi không được nhắc tới ở đâu, đường dẫn hỏng, phần nội dung quá dài và lạm dụng chữ IN HOA.
- **Kiểm tra hiệu quả nhanh.** Với 2–3 prompt thực tế, viết ra 3 hiệu quả có thể quan sát cho mỗi prompt, rồi kiểm tra khi có và không có skill.

## Cài đặt

Trong Claude Code:

```
/plugin marketplace add jack-reson8/skill-skill
/plugin install skill-skill@skill-skill
```

Hoặc dùng như một thư mục skill thông thường:

```bash
git clone https://github.com/jack-reson8/skill-skill /tmp/skill-skill && cp -R /tmp/skill-skill/plugins/skill-skill/skills/skill-skill ~/.claude/skills/
```

**Codex** (CLI hoặc ứng dụng ChatGPT trên máy tính):

```bash
codex plugin marketplace add jack-reson8/skill-skill
codex plugin add skill-skill@skill-skill
```

Hoặc sao chép `plugins/skill-skill/skills/skill-skill` vào `~/.codex/skills/`. Skill này tuân theo chuẩn mở [Agent Skills](https://agentskills.io), nên chạy được trong Claude Code, Codex và mọi agent đọc được SKILL.md.

**Các agent khác** (Cursor, Gemini CLI, GitHub Copilot và các agent khác được skills CLI hỗ trợ):

```bash
npx skills add jack-reson8/skill-skill
```

## Kiểm tra bất kỳ skill nào và nhận điểm sức khỏe

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

Kiểm tra một repo công khai bất kỳ thành báo cáo kèm biểu đồ: `python3 scripts/skill_report.py owner/repo`.

Có điểm rồi? Hãy đặt badge vào README của skill và chia sẻ (`--badge` sẽ in ra markdown).

Không cần phụ thuộc nào ngoài Python 3. Để chạy benchmark đánh giá đầy đủ và tối ưu description, hãy dùng kèm `skill-creator` của Anthropic.

## Câu hỏi thường gặp

**Tại sao Claude không dùng skill của tôi?** Claude chỉ dựa vào `description` để quyết định. Hãy nêu skill làm gì *và khi nào nên dùng*, bằng những cụm từ người dùng thực sự gõ, và giữ dưới 1.024 ký tự. `skill_audit.py` sẽ cảnh báo các description chưa đạt yêu cầu này.

**Quy tắc đặt tên trong SKILL.md là gì?** Tên gồm 1–64 chữ cái thường, chữ số và dấu gạch ngang đơn, đồng thời phải khớp với tên thư mục cha ([đặc tả Agent Skills](https://agentskills.io/specification)).

**Nó khác skill-creator của Anthropic thế nào?** skill-creator chạy đánh giá đầy đủ và tối ưu description. skill-skill là đường tắt: chắt lọc công việc thực tế thành các cơ chế bắt buộc và lint tĩnh trong vài giây. Hãy dùng cả hai.

Trang dự án: https://jack-reson8.github.io/skill-skill/

## Giấy phép

MIT
