"""on_sttings_materials.md の目次（<!-- TOC --> 〜 <!-- /TOC -->）を見出しから作り直す。

使い方: python3 scripts/toc.py on_sttings_materials.md
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

lines = []
chapter = None
for m in re.finditer(r'^(#{1,6}) (.+)$', body, re.M):
    level, heading = len(m.group(1)), m.group(2)
    if level == 1:
        chapter = heading
    # 2章は人物名（###）まで、ほかの章は ##### まで載せる
    if chapter == '2. 人物' and level > 3:
        continue
    if level > 5:
        continue
    lines.append('    ' * (level - 1) + f'- [{heading}](#{anchor(heading)})')

start = text.index('- [2. 人物]')
end = text.index('\n\n<!-- /TOC -->')
open(path, 'w', encoding='utf-8').write(text[:start] + '\n'.join(lines) + text[end:])
