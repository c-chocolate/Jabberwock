# JABBERWOCK

This tool collects JavaScript from a URL list, converts it to WebAssembly, and performs vectorization.

## input-output

input：URL list（Specified in tool.py)

output：DataFrame pkl file where vectors are stored

## How to use the code

`python tool.py`

## option

| option | default |
| ---- | ---- |
| --benign_list | benign_list.txt |
| --malicious_list | malicious_list.txt |
| --nonlabel_list | nonlabel_list.txt |
| -l, --label_mode | 0 |
|-b, --benign_num | 100 |
|-m, --malicious_num | 100 |
|-n, --nonlabel_num | 100 |
|-v, --vec_mode | 1 |
|-p, --parameter | 100 |
|-t, --tool_type | 0 |


### vec_mode

Types of parameters specified by "parameter" in Doc2Vec

Default values are set except for those specified here.

1: vec_size

2: epochs

3: min_count

4: dm

### parameter

Value of parameter specified by "mode"

### urlnum

Number of URLs in the URL list that you want to convert

### tool_type

0: Normal（do all)

1: JavaScript collection and conversion to WebAssembly Text

2: Vectorization of WebAssembly Text

## Caution
This tool uses Wobfuscator by Alan et al.
Place wobfuscator_tool in the folder a2_model.