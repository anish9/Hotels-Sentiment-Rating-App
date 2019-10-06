from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tqdm import tqdm
import pandas as pd
import tensorflow as tf
import numpy as np
from flask import abort, Flask, jsonify, request
app = Flask(__name__)

dataset = pd.read_csv("yelp.csv")
texts = dataset["text"].tolist()

counter_list = []
for words in tqdm(texts):
    lsito = words.split()
    for word in lsito:
        counter_list.append(word)   
lower = [k.lower() for k in counter_list]
max_word = len(list(set(lower)))

tokenizer = Tokenizer(num_words=max_word)

tokenizer.fit_on_texts(texts)

seq = tokenizer.texts_to_sequences(texts)
s = [len(q) for q in seq]
pad_max = max(s)
padded_seq = pad_sequences(seq,maxlen=pad_max,padding="post")


global graph
graph = tf.get_default_graph()
model = load_model('pred.h5')

def text_analyze(picks):
    pk = [picks]
    sentence = pk
    toks = tokenizer.texts_to_sequences(sentence)
    pads = pad_sequences(toks,maxlen=pad_max,padding="post")
    with graph.as_default():
    	output = model.predict(pads)
    output_ = "The rating for the hotel based on review - "+str(np.argmax(output))
    return output_




@app.route('/analyzetext', methods=['POST'])
def analyze():
    if not request.json or not 'message' in request.json:
        abort(400)
    message = request.json['message']
    prediction = text_analyze(message)
    print(prediction)
    response = {'result': prediction}
    return jsonify(response["result"]), 200



if __name__ == "__main__":
    app.run()