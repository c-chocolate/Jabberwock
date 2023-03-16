# JABBERWOCK

This tool collects JavaScript from a URL list, converts it to WebAssembly Text, and performs vectorization.

## input-output

input：URL list（Specified in tool.py)

output：DataFrame pkl file where vectors are stored

## How to use the code

`python tool.py <mode> <parameter> <urlnum> <tool_type>`

### mode

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