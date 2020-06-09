from cmreslogging.handlers import CMRESHandler
from pymongo import MongoClient
from datetime import datetime
import pandas as pd
from bson.json_util import dumps
import logging
import tweepy
import json
import sys
import re
import os


def cria_conexao_mongo(host='localhost', port=27017, username='root', password='example'): 
#def cria_conexao_mongo():
    cliente = MongoClient(host,
                          port=port,
                          username=username,
                          password=password)
    banco = cliente['twitter']
    return banco['tweets']


def grava_dados(data, mongo):
    result = mongo.insert_one(data).inserted_id
    print("linha inserida: " + str(result))

def busca_top5(mongo):
    return mongo.find().sort([('followers_count', -1)]).limit(5) # returns cursor

def busca_porhora(mongo):
    return mongo.aggregate([
        {"$group": 
            { "_id": "$created_at_hour",
                   "soma": { "$sum" : 1 } } 
        },
        {"$sort": {"soma": -1}}
        ])

def busca_hashtagbycountry(mongo):
    return mongo.aggregate([
        {"$group": 
            { "_id": {"hashtag" : "$hashtag", "lang":"$lang"},
                   "soma": { "$sum" : 1 } } 
        },
        {"$sort": {"soma": -1}}
        ])


def busca_hashtagbycountry2(mongo):
    return mongo.aggregate([
            {
                "$group": {
                    "_id": {
                        "hashtag": "$hashtag",
                        "lang": "$lang"
                    },
                    "count": {
                        "$sum": 1
                    }
                }
            }, {
                "$group": {
                    "_id": "$_id.hashtag",
                    "lang": {
                        "$push": {
                            "lang": "$_id.lang",
                            "count": "$count"
                        }
                    }
                }
            }
        ])




#######busca_porhora
mongo = cria_conexao_mongo()
result = busca_hashtagbycountry2(mongo)

print(result)
for doc in result:
    print(doc['lang'])
    #print(doc['sum'])
    print('\n')
    





###### TOP 5
#mongo = cria_conexao_mongo()
#result = busca_top5(mongo)
#print(result)
#followers_count = {}
#username = {}
#i = 0
#for doc in result:
#    followers_count[i] = doc['followers_count']
#    username[i] = doc['username']
#    i = i + 1
#    
#
#follow = [followers_count[0], followers_count[1], followers_count[2], followers_count[3], followers_count[4]]
#user = [username[0], username[1], username[2], username[3], username[4]]
#
#
## a bit of modification to get the items list of dictionaries:
#keys = ['username', 'followers_count']
#items = [dict(zip(keys, [u, t])) for u, t in zip(user, follow)]
#
## create the output dict
#d = {
#      'Query': 'followers_count',
#      'items': items
#    }
#
## make a pretty json string from the dict
#d = json.dumps(d, indent=4)
#print(d)
## write the string to a txt file
##with open(file, 'w') as fobj:
##    fobj.write(d)