# CLAUDE.md

Project Roche Limit（SS・伺かゴースト）の設定資料。読み手は昔からのファンと二次創作をしたい人。

## ファイル

- `on_sttings_materials.md`: 本体。1. 目次 / 2. 人物 / 3. 世界設定 / 4. 技術 / 5. 兵器・乗り物
- `extreme_world.md`: Extreme World の用語（本体とは別）
- `template.md`: 人物・用語の書式と共通の決まり。項目を足す・直すときは先に読む
- `README.md`: 利用条件（FSW 宣言）と借用設定の出典。他作品の設定を借りたらここにも書く
- `ss_backlog.md`: SS（`../Project-Roche-Limit-Crossing`）から移植する項目のバックログ。移したら状態を ✅ にする

## 目次の更新

本体と `extreme_world.md` の目次は `<!-- TOC -->` 〜 `<!-- /TOC -->` の間にある。見出しを足す・変えたら作り直す。

```bash
python3 scripts/toc.py on_sttings_materials.md
python3 scripts/toc.py extreme_world.md
```

- 本体の2章は `###`（人物名）まで、他の章は `#####` まで載せる。`extreme_world.md` は `##` から `#####` まで
- 目次に載る見出しが重なると、リンクが最初の一つに飛ぶ。汎用の見出しには `作者メモ（項目名）` のように括弧で項目名を添える

## 作業の進め方

- 設定の解釈が分かれるところは推測で埋めず、作者に確認する
- SS やゴーストの資料から設定を取り込むときは、スキル `import-settings` の手順に従う
- `scripts/replace_once.py`: 置き換え前の文字列が一度だけ現れることを確かめてから書き換える
- `scripts/read_any.py`: utf-8 で読めなければ cp932 で読む（古いゴーストの memo 用）
- コミットメッセージは `feat:` / `docs:` などの接頭辞のあとに日本語で書く
