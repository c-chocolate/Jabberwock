# JABBERWOCK

This tool collects JavaScript from a URL list, converts it to WebAssembly, and performs vectorization.

## input-output

input：URL list

output：DataFrame pkl file where vectors are stored

## How to use the code

`python tool.py`

## option

| option | default |
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

1: labeled

2: non-labeled

### input

#### labeled

Need a list of benign and malicious URLs.

Default points to the same location as tool.py.

Optionally, the URL list of inputs can be changed.(--benign_list, --malicious_list)

Can specify the number of URLs to use out of a URL list.(-b, -m)

#### non-labeled

Need a list of URLs.

Default points to the same location as tool.py.

Optionally, the URL list of inputs can be changed.(--nonlabel_list)

Can specify the number of URLs to use out of a URL list.(-n)

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