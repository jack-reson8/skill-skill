#!/usr/bin/env python3
"""skill_audit.py <skill_dir> [--all] [--badge] — static checks that catch skills which won't take effect.
Checks: frontmatter (name format, description length / trigger words), name collisions with other installed skills,
every file under references/ scripts/ assets/ is pointed to from SKILL.md (orphans never get read),
every path SKILL.md mentions exists, steps that name an output artifact, shouting (ALL-CAPS MUST/NEVER), size."""
import os, re, sys, glob
ROOTS = [os.path.expanduser('~/.claude/skills')]

def fm(text):
    m = re.match(r'---\n(.*?)\n---\n', text, re.S)
    if not m: return None, text
    d, key = {}, None
    for line in m.group(1).splitlines():
        if line.startswith((' ', '\t')) and key:            # folded / indented continuation
            d[key] = (d[key] + ' ' + line.strip()).strip(); continue
        k, _, v = line.partition(':'); key = k.strip()
        d[key] = '' if v.strip() in ('>', '|', '>-', '|-') else v.strip()
    return d, text[m.end():]

def audit(sd):
    issues, notes = [], []
    p = os.path.join(sd, 'SKILL.md')
    if not os.path.exists(p): return [f'no SKILL.md in {sd}'], []
    text = open(p).read(); meta, body = fm(text)
    if not meta: return ['missing YAML frontmatter'], []
    name, desc = meta.get('name', ''), meta.get('description', '')
    if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', name): issues.append(f'name "{name}" must be lowercase-hyphen')
    if name != os.path.basename(sd.rstrip('/')): issues.append(f'name "{name}" ≠ folder "{os.path.basename(sd)}"')
    if not desc: issues.append('empty description')
    if len(desc) > 1024: issues.append(f'description {len(desc)} chars > 1024')
    if desc and not re.search(r'(use when|use whenever|use it|trigger|使用|触发)', desc, re.I): issues.append('description has no "Use when…" trigger clause')
    for root in ROOTS:
        for other in glob.glob(os.path.join(root, '*', 'SKILL.md')):
            if os.path.dirname(other) != os.path.abspath(sd):
                om, _ = fm(open(other).read())
                if om and om.get('name') == name: issues.append(f'name collides with {other}')
    # orphans: bundled files never mentioned in SKILL.md won't be read
    for sub in ('references', 'scripts', 'assets'):
        for f in glob.glob(os.path.join(sd, sub, '**', '*'), recursive=True):
            rel = os.path.relpath(f, sd); folder = os.path.dirname(rel) + '/'
            if os.path.isfile(f) and sub != 'assets' and os.path.basename(f) not in text and not re.search(re.escape(folder) + r'(?:<|\*|`|\s|$)', text):
                issues.append(f'orphan: {os.path.relpath(f, sd)} is never mentioned in SKILL.md')
    # dangling: paths mentioned but missing
    for ref in set(re.findall(r'`((?:references|scripts|assets)/[\w./-]+)`', text)):
        if not os.path.exists(os.path.join(sd, ref)): issues.append(f'dangling path: {ref}')
    # effect: steps should end in something the model produces or checks
    steps = re.findall(r'^##+ .*$', body, re.M)
    produce = len(re.findall(r'\b(write|save|output|produce|render|run|check)\b|→|写|输出|生成|检查|运行|保存|改写', body, re.I))
    notes.append(f'{len(body.splitlines())} body lines, {len(steps)} sections, {produce} action/artifact words')
    shout = re.findall(r'\b(MUST|NEVER|ALWAYS)\b', body)
    if produce == 0: notes.append('warn: no step produces an artifact or runs a check — the skill may not change output')
    if len(shout) > 3: notes.append(f'warn: {len(shout)} ALL-CAPS commands — explain the why instead')
    if len(body.splitlines()) > 500: issues.append('SKILL.md body > 500 lines — move detail into references with pointers')
    for ref in glob.glob(os.path.join(sd, 'references', '*.md')):
        n = len(open(ref).read().splitlines())
        if n > 300 and '## ' not in open(ref).read()[:800]: notes.append(f'warn: {os.path.basename(ref)}: {n} lines, add a table of contents')
    return issues, notes

def score(issues, notes):
    return max(0, 100 - 15 * len(issues) - 5 * sum(n.startswith('warn') for n in notes))

def card(name, sc):
    stars = '★' * round(sc / 20) + '☆' * (5 - round(sc / 20))
    color = 'brightgreen' if sc >= 90 else 'yellow' if sc >= 70 else 'red'
    return stars, f'![skill health](https://img.shields.io/badge/skill%20health-{sc}%2F100-{color})'

if __name__ == '__main__':
    targets = [os.path.dirname(p) for r in ROOTS for p in glob.glob(os.path.join(r, '*', 'SKILL.md'))] if '--all' in sys.argv else [sys.argv[1]]
    bad, scores = 0, []
    for sd in targets:
        issues, notes = audit(os.path.abspath(os.path.expanduser(sd)))
        sc = score(issues, notes); stars, badge = card(os.path.basename(sd), sc)
        print(f'\n== {os.path.basename(sd.rstrip("/"))}   {sc}/100  {stars}'); [print('  ✗', i) for i in issues]; [print('  ·', n) for n in notes]
        if not issues: print('  ✓ no blocking issues')
        if '--badge' in sys.argv: print('  badge:', badge)
        bad += len(issues); scores.append(sc)
    if len(scores) > 1: print(f'\nAverage skill health: {sum(scores) // len(scores)}/100 across {len(scores)} skills')
    sys.exit(1 if bad else 0)
