from flask import Flask, jsonify, request
from bson.json_util import dumps
from datetime import datetime
import logging_es
import twitter
import json
import conn

app = Flask(__name__)


##https://pypi.org/project/flask-prometheus-metrics/

@app.route('/relatorio/top5/', methods=['GET'])
def top5():
    try:
        mongo = conn.cria_conexao_mongo()   
        result = conn.busca_top5(mongo)
        logging_es.send_log('/relatorio/top5/ methods=[GET])')
    except:
        logging_es.send_log('api.py /relatorio/top5/ mongo get values error','error')
    followers_count = {}
    username = {}
    i = 0
    try:
        for doc in result:
            followers_count[i] = doc['followers_count']
            username[i] = doc['username']
            i = i + 1
        # a bit of modification to get the items list of dictionaries:
        keys = ['username', 'followers_count']
        items = [dict(zip(keys, [u, t])) for u, t in zip(username.values(), followers_count.values())]
    except:
        result = {"return" : "error"}
        logging_es.send_log('api.py /relatorio/top5/ build json error','error')
    d = {
        'Query': 'followers_count',
        'items': items
        }
    d = json.dumps(d, indent=4)
    print(d)
    return d, 200


@app.route('/relatorio/tweetbyhour/', methods=['GET'])
def tweetporhora():
    try:
        mongo = conn.cria_conexao_mongo()
        result = conn.busca_porhora(mongo)
        logging_es.send_log('/relatorio/tweetbyhour/, methods=[GET])')
    except:
        result = {"return" : "error"}
        logging_es.send_log('api.py /relatorio/tweetbyhour/ mongo get values error','error')
    d = {
    'Query': 'tweets_by_hour',
    'items': dumps(result)
    }
    return d


@app.route('/relatorio/tweetsbycountry/', methods=['GET'])
def hashtagbycountry():
    try:
        mongo = conn.cria_conexao_mongo()
        result = conn.busca_hashtagbycountry(mongo)
        logging_es.send_log('/relatorio/tweetsbycountry/ methods=[GET])')
    except:
        result = {"return" : "error"}
        logging_es.send_log('api.py /relatorio/tweetsbycountry/ mongo get values error','error')
    d = {
    'Query': 'tweets_by_country',
    'items': dumps(result)
    }
    return d


@app.route('/buscatweets', methods=['POST'])
def insert_data():
    try:
        twitter.busca_hashtag()
        logging_es.send_log('/buscatweets methods=[POST])')
    except:
        logging_es.send_log('api.py /buscatweets mongo get values error','error')
    

    body = {
        'jobStatus': 'done',
        'statusCode': 200,
        'timestamp': datetime.now()
    }
    return jsonify(body), 200

@app.route('/', methods=['GET'])
def index():
        return 'Saiba mais em https://github.com/jcnoliveira/TwitterAPI'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)