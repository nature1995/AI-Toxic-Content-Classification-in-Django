from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from tensorflow import keras
from tqdm import tqdm
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
import spacy
import json
import ssl


def input_model():
    model = keras.models.load_model('/home/ubuntu/ziran/my_model.h5')
    return model


def process_words(model, text):
    max_length = 55
    nlp = spacy.load('/home/ubuntu/ziran/en_core_web_lg-2.2.5/en_core_web_lg/en_core_web_lg-2.2.5', disable=['parser', 'ner', 'tagger'])
    nlp.vocab.add_flag(lambda s: s.lower() in spacy.lang.en.stop_words.STOP_WORDS, spacy.attrs.IS_STOP)
    with open('/home/ubuntu/ziran/quora_dict.txt', 'r') as json_file:
        word_dict = json.load(json_file)
    s1 = text
    s1 = pd.Series(s1)
    s1 = nlp.pipe(s1)
    word_index = 1
    lemma_dict = {}
    word_sequences = []
    for doc in tqdm(s1):
        word_seq = []
        for token in doc:
            if (token.text not in word_dict) and (token.pos_ is not "PUNCT"):
                word_dict[token.text] = word_index
                word_index += 1
                lemma_dict[token.text] = token.lemma_
            if token.pos_ is not "PUNCT":
                word_seq.append(word_dict[token.text])
        word_sequences.append(word_seq)
    t = pad_sequences(word_sequences, maxlen=max_length)
    print(model.predict(t))
    result = model.predict(t)[0][0]
    return result


@login_required(login_url='/accounts/login/')
@csrf_exempt
def predict(request):
    # solve error “SSL: CERTIFICATE_VERIFY_FAILED”
    result = "  "
    ssl._create_default_https_context = ssl._create_unverified_context
    if request.method == 'POST':
        if request.POST.get("text"):
            text = request.POST.get("text")
            print(text)
            model = input_model()
            result = process_words(model, text)
            print("result:" + str(result))
    return render(request, "predict.html", {"result": str(result)})


