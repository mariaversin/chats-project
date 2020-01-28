FROM python:3

ADD . .

RUN pip3 install -r requirements.txt

RUN pip install nltk && \
    mkdir ~/nltk_data && \
    mkdir ~/nltk_data/chunkers && \
    mkdir ~/nltk_data/corpora && \
    mkdir ~/nltk_data/taggers && \
    mkdir ~/nltk_data/tokenizers && \
    python -c "import nltk; nltk.download(['punkt', 'averaged_perceptron_tagger', 'maxent_ne_chunker', 'words'])"

RUN adduser --disabled-password myuser

USER myuser 

CMD ["python3","-u","app.py"]