# PyGlueTokenizer
A tool for obtaining natural language summaries of Python functions.

Steps

#if you don't have it installed
python3 -m pip install virtualenv

#Create virtualenv
python3 -m virtualenv venv

#activate virtualenv
source virtual/bin/activate

#run CodeGen-main/install_env.sh
sh CodeGen-main/install_env.sh

#install requirments
pip install -r requirements.txt

#Use this instead if it gets killed ```pip install --no-cache-dir -r requirements.txt```

#download the CodeGen Model
wget https://dl.fbaipublicfiles.com/transcoder/pre_trained_models/translator_transcoder_size_from_DOBF.pth -P CodeGen-main

#download the Code2Seq Model
wget https://s3.amazonaws.com/code2seq/model/java-large/java-large-model.tar.gz -P code2seq
tar -xvzf code2seq/java-large-model.tar.gz -C code2seq
rm code2seq/java-large-model.tar.gz