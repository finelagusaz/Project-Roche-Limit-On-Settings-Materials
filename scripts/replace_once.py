"""置き換えの組を、それぞれ一度だけ現れることを確かめてから適用する。

使い方: python3 -I scripts/replace_once.py 対象.md 置き換え定義.py

置き換え定義.py には REPS = [(置き換え前, 置き換え後), ...] を書く。
一つでも 0 回・2 回以上現れたら、ファイルには何も書き込まずに止まる。
"""
import importlib.util
import sys

path, reps_path = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location('reps', reps_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

text = open(path, encoding='utf-8').read()
for before, after in module.REPS:
    count = text.count(before)
    if count != 1:
        sys.exit(f'{count} 回現れた: {before[:60]!r}')
    text = text.replace(before, after)

open(path, 'w', encoding='utf-8').write(text)
print(f'{len(module.REPS)} 件を置き換えた')
