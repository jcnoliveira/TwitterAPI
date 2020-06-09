# acessar https://apps.twitter.com para criar uma nova aplicação
# cada aplicação tem suas próprias chaves
from cmreslogging.handlers import CMRESHandler
from pymongo import MongoClient
from datetime import datetime
import pandas as pd
import logging
import tweepy
import json
import conn
import sys
import re
import os

def autentica_twitter():
    auth = tweepy.OAuthHandler('PnDbc1eIqAnsDqS8yNWIKMRls', 
                            'CEJuw59mJ3hZOgoARS2Z8GT6OhBnnxlylkNzDKx8rXMpjXWu2e')
    auth.set_access_token('1243273842845454338-OQhmg52U32DTMbtaj6sb1mc3Yu4uHm',
                        'KOwORproGuGFrREs5jlIebq4jzZsRRu7VrJ7ZgQO0smpD')
    return tweepy.API(auth)


def procura_hashtag(api, hashtag, mongo, quantidade_procura=100 ):
    print(hashtag)
    for tweet in tweepy.Cursor(api.search, 
                               q=str(hashtag + ' -filter:retweets'), 
                               rpp=100, 
                               tweet_mode='extended', 
                               result_type='recent').items(quantidade_procura):
        #date = datetime.datetime.strptime(string, "%d %b %Y  %H:%M:%S.%f")
        date = tweet.created_at
        print(tweet)
        msg = {"id"                 : tweet.id, 
               "hashtag"            : hashtag, 
               "created_at_year"    : date.year,
               "created_at_month"   : date.month,
               "created_at_day"     : date.day,
               "created_at_hour"    : date.hour,
               "created_at_minute"  : date.minute,
               "full_text"          : tweet.full_text, 
               "username"           : tweet.user.screen_name, 
               "name"               : tweet.user.name, 
               "user_id"            : tweet.user.id, 
               "followers_count"    : tweet.user.followers_count, 
               "location"           : tweet.user.location, 
               "source"             : tweet.source, 
               "source_url"         : tweet.source_url, 
               "lang"               : tweet.lang}
        
        conn.grava_dados(msg, mongo)
        print(msg)
    
    return msg


def busca_hashtag(hashtag):
    for x in hashtags:
       procura_hashtag(autentica_twitter(), x, conn.cria_conexao_mongo())



if __name__ == "__main__":
    hashtags = ["#openbanking"]#, 
#                "#remediation",
#                "#devops", 
#                "#sre", 
#                "#microservices",
#                "#observability", 
#                "#oauth", 
#                "#metrics", 
#                "#logmonitoring", 
#                "#opentracing"]
    busca_hashtag(hashtags)