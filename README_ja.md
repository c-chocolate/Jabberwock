# JABBERWOCK

このツールはURLリストからJavaScriptを収集し、WebAssembly Textに変換し、ベクトル化を行います。

## 入出力

入力：URLリスト（tool.py内で指定)

出力：ベクトルをが保存されたDataFrameのpklファイル

## コードの使い方

'python tool.py <mode> <parameter> <urlnum> <tool_type>'

# mode

Doc2Vecにおいてparameterで指定するパラメータの種類
ここで指定するもの以外は初期値を設定している

1: vec_size
2: epochs
3: min_count
4:dm

# parameter

modeで指定したパラメータの値

# urlnum

URLリストのうち変換したいURLの数

# tool_type

0: 通常（全て行う)
1: JavaScriptの収集とWebAssembly Textへの変換
2: WebAssembly Textのベクトル化

## 注意
このツールはAlanらによるWobfuscatorを使用しています。
フォルダa2_model内にwobfuscator_toolを置いてください。