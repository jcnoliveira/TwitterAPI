from flask import Flask, jsonify, request
import json
import conn
import logging_es
import twitter
from bson.json_util import dumps
app = Flask(__name__)




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



@app.route('/top5/', methods=['GET'])
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

@app.route('/tweetporhora/', methods=['GET'])
def tweetporhora():
    mongo = conn.cria_conexao_mongo()
    result = conn.busca_porhora(mongo)
    
    hora = {}
    soma = {}
    i = 0
    for doc in result:
        hora[i] = doc['_id']
        soma[i] = doc['soma']
        i = i + 1

    # a bit of modification to get the items list of dictionaries:
    keys = ['hour', 'value']
    items = [dict(zip(keys, [u, t])) for u, t in zip(hora.values(), soma.values())]

    # create the output dict
    d = {
        'Query': 'tweets_by_hour',
        'items': items
        }

    # make a pretty json string from the dict
    d = json.dumps(d, indent=4)
    print(d)
    return d, 200


@app.route('/hashtagbycountry/', methods=['GET'])
def hashtagbycountry():
    mongo = conn.cria_conexao_mongo()
    result = conn.busca_hashtagbycountry(mongo)
    
    hashtag = {}
    lang = {}
    soma = {}
    i = 0
    for doc in result:
        hashtag[i] = doc['_id']['hashtag']
        lang[i] = doc['_id']['lang']
        soma[i] = doc['soma']
        i = i + 1

    # a bit of modification to get the items list of dictionaries:
    keys = ['hashtag', 'lang', 'soma']
    items = [dict(zip(keys, [u, t, v])) for u, t, v in zip(hashtag.values(), lang.values(), soma.values())]

    # create the output dict
    d = {
        'Query': 'tweets_by_hour',
        'items': items
        }

    # make a pretty json string from the dict
    d = json.dumps(d, indent=4)
    print(d)
    return d, 200

@app.route('/hashtagbycountry2/', methods=['GET'])
def hashtagbycountry2():
    mongo = conn.cria_conexao_mongo()
    result = conn.busca_hashtagbycountry(mongo)
    
    hashtag = {}
    lang = {}
    soma = {}
    i = 0
    for doc in result:
        print(doc)
        hashtag[i] = doc['_id']
        lang[i] = doc['lang']
        i = i + 1

    # a bit of modification to get the items list of dictionaries:
    keys = ['hashtag', 'lang']
    items = [dict(zip(keys, [u, t])) for u, t in zip(hashtag.values(), lang.values())]

    # create the output dict
    d = {
        'Query': 'tweets_by_hour',
        'items': items
        }

    # make a pretty json string from the dict
    d = json.dumps(d, indent=4)
    print(d)
    return d, 200

@app.route('/hashtagbycountry3/', methods=['GET'])
def hashtagbycountry3():
    mongo = conn.cria_conexao_mongo()
    result = conn.busca_hashtagbycountry2(mongo)
    return dumps(result), 200

@app.route('/contact')
def contact():
    return "Contact page"
@app.route('/teapot/')
def teapot():
    return "Would you like some tea?", 418


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)