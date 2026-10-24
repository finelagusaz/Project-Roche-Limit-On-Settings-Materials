"""テキストファイルを utf-8 で読み、読めなければ cp932（Shift_JIS）で読んで表示する。

使い方: python3 -I scripts/read_any.py ファイル [ファイル ...]

古いゴーストの memo.txt や descript.txt は cp932 のものが多い。
"""
import sys

for path in sys.argv[1:]:
    data = open(path, 'rb').read()
    for encoding in ('utf-8-sig', 'cp932'):
        try:
            text = data.decode(encoding)
            break
        except UnicodeDecodeError:
            pass
    else:
        encoding = 'cp932（読めない文字は置換）'
        text = data.decode('cp932', errors='replace')
    print(f'===== {path} [{encoding}]')
    print(text)
