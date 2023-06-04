from flask import Flask, flash, send_file, render_template, session, redirect, request, url_for, jsonify
from py4j.java_gateway import JavaGateway
from pymongo import MongoClient, collection
import json


app = Flask(__name__)
gateway = JavaGateway()
my_java_object = gateway.entry_point
text_combiner = gateway.jvm.TextCombiner

client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']
collection = db['test_collection']


###MAIN ROUTE
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        datas = request.get_json()['texts']
        java_texts = gateway.new_array(gateway.jvm.java.lang.String, len(datas))
        for i in range(len(datas)):
            java_texts[i] = datas[i]
        result = text_combiner.combineTexts(java_texts)

        # collectiona eklemek icin dictionary olustur
        data = {'inputs': datas, 'output': result}

        #datayi collectiona eklemek
        collection.insert_one(data)

        return jsonify({'result': result})
    else:
        return render_template('index.html')

###TEST ROUTE
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        datas = request.get_json()['texts']
        java_texts = gateway.new_array(gateway.jvm.java.lang.String, len(datas))
        for i in range(len(datas)):
            java_texts[i] = datas[i]
        result = text_combiner.combineTexts(java_texts)
        return jsonify({'result': result})
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
