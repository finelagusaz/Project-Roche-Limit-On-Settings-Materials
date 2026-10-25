"""目次（<!-- TOC --> 〜 <!-- /TOC -->）を見出しから作り直す。

使い方: python3 scripts/toc.py on_sttings_materials.md
        python3 scripts/toc.py extreme_world.md

本体は章（#）から、extreme_world.md は ## から載せる。
"""
import re
import sys


def anchor(heading):
    a = heading.strip().lower()
    a = re.sub(r'[.「」（）()？?、,:：/／＝=\[\]]', '', a)
    return a.replace(' ', '-')


path = sys.argv[1]
text = open(path, encoding='utf-8').read()
body = text[text.index('<!-- /TOC -->'):]
# 本体は章見出し（# 2. 人物 など）を目次に含める。extreme_world.md は ## から
top = 1 if re.search(r'^# 2\. 人物$', body, re.M) else 2

lines = []
chapter = None
for m in re.finditer(r'^(#{1,6}) (.+)$', body, re.M):
    level, heading = len(m.group(1)), m.group(2)
    if level == 1:
        chapter = heading
    if level < top:
        continue
    # 2章は人物名（###）まで、ほかの章は ##### まで載せる
    if chapter == '2. 人物' and level > 3:
        continue
    if level > 5:
        continue
    lines.append('    ' * (level - top) + f'- [{heading}](#{anchor(heading)})')

if top == 1:
    start = text.index('- [2. 人物]')
else:
    start = text.index('<!-- TOC -->') + len('<!-- TOC -->\n\n')
end = text.index('\n\n<!-- /TOC -->')
open(path, 'w', encoding='utf-8').write(text[:start] + '\n'.join(lines) + text[end:])
