### Imports ##
import os
import subprocess
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import graphviz
import json
import visuals

### Get .java translation ###
def java_translation(filename):
    os.chdir('CodeGen-main')
    subprocess.check_output("python -m codegen_sources.model.translate --src_lang python --tgt_lang java --model_path translator_transcoder_size_from_DOBF.pth --beam_size 1 < " + filename, shell=True)
    return

### Get code2seq tokenization ###
def code2seq_tokens():
    os.chdir('..')
    with open("CodeGen-main/JavaSample.txt") as new_java:
        with open("code2seq/Input.java", "w") as old_java:
            for line in new_java:
                old_java.write(line)
    os.chdir('code2seq')
    subprocess.check_output("python3 code2seq.py --load models/java-large-model/model_iter52.release --predict", shell=True)
    return

### Get .JSON of parsed code ###
def parse_code(filename):
    subprocess.check_output("python3 python_parser.py " + filename, shell=True)
    with open('python_sample.json') as f:
        ast_json = f.read()
    jdata = json.loads(ast_json)
    os.chdir('..')
    return jdata

### Get graph of AST ###
def draw_graph(json_data):
    ast = graphviz.Digraph('Abstract Syntax Tree', node_attr={'font color': 'black', 'color': 'cyan:aquamarine', 'style': 'filled'})
    ast.attr(bgcolor='aliceblue')
    count = 0
    for node in json_data:
        label = node.get('type')
        if 'value' in node:
            label = label + ': ' + node.get('value')
        ast.node(str(count), label)
        count += 1
    for i in range(0, len(json_data)):
        if 'children' in json_data[i]:
            childs = json_data[i].get('children')
            for node_num in childs:
                ast.edge(str(i), str(node_num))
    ast.render(directory='ast-output', view=True)

## Pretty display of tokenization ###
def main():
    Tk().withdraw()  # we don't want a full GUI yet, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    java_translation(filename)
    code2seq_tokens()
    jdat = parse_code(filename)
    draw_graph(jdat)
    subprocess.check_output("python3 visuals.py", shell=True)
    return

main()