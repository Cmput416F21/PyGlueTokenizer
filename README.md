# PyGlueTokenizer
A tool for obtaining natural language summaries of Python functions by utilizing Code2Seq and CodeGen.

## Team:
- Abdelrahman Abdalla
- Kiran Deol
- Nahome Wolde-Giorgis

### Cloning the repo:
- `git clone https://github.com/Cmput416F21/PyGlueTokenizer`
- `cd PyGlueTokenizer`

### Initial Setup:
0. if you don't have virtualenv installed
    - `python3 -m pip install virtualenv`
1. Create virtualenv
    - `python3 -m virtualenv venv`
2. activate virtualenv
    - `source venv/bin/activate`
3. run setup.sh
    - `sh setup.sh`
### Using the Program:
4. to run the program run glue.py while inside of the Virtual enviroment
    - `python glue.py`
5. choose the file you want to run the program on from the GUI, some sample files are provided in `CodeGen-main/codesamples`

<!-- This content will not appear in the rendered Markdown
run CodeGen-main/install_env.sh

`sh CodeGen-main/install_env.sh`

install requirments

`pip install -r requirements.txt`

*Use this instead if it gets killed* `pip install --no-cache-dir -r requirements.txt`

download the CodeGen Model

`wget https://dl.fbaipublicfiles.com/transcoder/pre_trained_models/translator_transcoder_size_from_DOBF.pth -P CodeGen-main`

download the Code2Seq Model

```
wget https://s3.amazonaws.com/code2seq/model/java-large/java-large-model.tar.gz -P code2seq
tar -xvzf code2seq/java-large-model.tar.gz -C code2seq
rm code2seq/java-large-model.tar.gz
```
-->
