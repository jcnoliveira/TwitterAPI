from flask import Flask, jsonify, request
from bson.json_util import dumps
from datetime import datetime
import logging_es
import twitter
import json
import conn

app = Flask(__name__)


##https://pypi.org/project/flask-prometheus-metrics/

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)


@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name

@app.route('/person/')
def hello2():
    return jsonify({'name':'Jimit',
                    'address':'India'})



@app.route('/relatorio/top5/', methods=['GET'])
def top5():
    mongo = conn.cria_conexao_mongo()
    result = conn.busca_top5(mongo)
    return dumps(result), 200  

@app.route('/relatorio/tweetporhora/', methods=['GET'])
def tweetporhora():
    mongo = conn.cria_conexao_mongo()
    result = conn.busca_porhora(mongo)
    return dumps(result), 200  

@app.route('/relatorio/hashtagbycountry/', methods=['GET'])
def hashtagbycountry():
    mongo = conn.cria_conexao_mongo()
    result = conn.busca_hashtagbycountry2(mongo)
    return dumps(result), 200  

@app.route('/buscatweets', methods=['POST'])
def insert_data():
    #slug = request.form['slug']
    #title = request.form['title']
    #content = request.form['content']

    twitter.busca_hashtag()
    body = {
        'jobStatus': 'iniciado',
        'statusCode': 200,
        'timestamp': datetime.now()
    }

    return jsonify(body), 200


@app.route('/contact')
def contact():
    return "Contact page"
@app.route('/teapot/')
def teapot():
    return "Would you like some tea?", 418


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)