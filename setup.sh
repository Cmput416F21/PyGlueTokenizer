cd CodeGen-main
sh install_env.sh
cd ..
pip install -r requirements.txt
wget https://dl.fbaipublicfiles.com/transcoder/pre_trained_models/translator_transcoder_size_from_DOBF.pth -P CodeGen-main
wget https://s3.amazonaws.com/code2seq/model/java-large/java-large-model.tar.gz -P code2seq
tar -xvzf code2seq/java-large-model.tar.gz -C code2seq
rm code2seq/java-large-model.tar.gz
python glue.py
