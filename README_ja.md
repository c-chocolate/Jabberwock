# JABBERWOCK

このツールはURLリストからJavaScriptを収集し、WebAssemblyに変換し、ベクトル化を行います。

## 入出力

入力：URLリスト

出力：ベクトルをが保存されたDataFrameのpklファイル

## コードの使い方

`python tool.py`

## オプション

| オプション | デフォルト |
| ---- | ---- |
| -l, --label_mode | 0 |
| --benign_list | benign_list.txt | 
| --malicious_list | malicious_list.txt |
| --nonlabel_list | nonlabel_list.txt |
|-b, --benign_num | 100 |
|-m, --malicious_num | 100 |
|-n, --nonlabel_num | 100 |
|-v, --vec_mode | 1 |
|-p, --parameter | 100 |
|-t, --tool_type | 0 |

### label_mode

1: ラベル付

2: ラベルなし

### input

#### labeled

良性と悪性のURLリストが必要

デフォルトはtool.pyと同じ場所に設置

オプションでURLリストを変更できる(--benign_list, --malicious_list)

URLリストのうち使うURLの数を指定できる(-b, -m)

#### non-labeled

URLリストが必要

デフォルトはtool.pyと同じ場所に設置

オプションでURLリストを変更できる(--nonlabel_list)

URLリストのうち使うURLの数を指定できる(-n)

# vec_mode

Doc2Vecにおいてparameterで指定するパラメータの種類
ここで指定するもの以外は初期値を設定している

1: vec_size
2: epochs
3: min_count
4: dm

# parameter

modeで指定したパラメータの値

# tool_type

0: 通常（全て行う)
1: JavaScriptの収集とWebAssembly Textへの変換
2: WebAssembly Textのベクトル化

## 注意
このツールはAlanらによるWobfuscatorを使用しています。
フォルダa2_model内にwobfuscator_toolを置いてください。