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
    mongo = conn.cria_conexao_mongo()
    result = conn.busca_top5(mongo)
    followers_count = {}
    username = {}
    i = 0
    for doc in result:
        followers_count[i] = doc['followers_count']
        username[i] = doc['username']
        i = i + 1

    # a bit of modification to get the items list of dictionaries:
    keys = ['username', 'followers_count']
    items = [dict(zip(keys, [u, t])) for u, t in zip(username.values(), followers_count.values())]

    # create the output dict
    d = {
        'Query': 'followers_count',
        'items': items
        }

    # make a pretty json string from the dict
    d = json.dumps(d, indent=4)
    print(d)
    return d, 200


@app.route('/relatorio/tweetbyhour/', methods=['GET'])
def tweetporhora():
    mongo = conn.cria_conexao_mongo()
    result = conn.busca_porhora(mongo)
    d = {
    'Query': 'tweets_by_hour',
    'items': dumps(result).replace('\\"', '"')
    }
    # make a pretty json string from the dict
    d = json.dumps(d, indent=4)
    return d
    #return dumps(result), 200  

@app.route('/relatorio/tweetsbycountry/', methods=['GET'])
def hashtagbycountry():
    mongo = conn.cria_conexao_mongo()
    result = conn.busca_hashtagbycountry(mongo)
    d = {
    'Query': 'tweets_by_country',
    'items': dumps(result).replace('\\"', '"')
    }
    # make a pretty json string from the dict
    d = json.dumps(d, indent=4)
    return d
    # return dumps(result), 200  

@app.route('/buscatweets', methods=['POST'])
def insert_data():
    #slug = request.form['slug']
    #title = request.form['title']
    #content = request.form['content']

    twitter.busca_hashtag()
    body = {
        'jobStatus': 'done',
        'statusCode': 200,
        'timestamp': datetime.now()
    }
    return jsonify(body), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)