# acessar https://apps.twitter.com para criar uma nova aplicação
# cada aplicação tem suas próprias chaves
from cmreslogging.handlers import CMRESHandler
import pandas as pd
import logging
import tweepy
import sys
import re
import os



# acessar a aba "Keys and Access Tokens"
# passa o Consumer Key e o Consumer Secret
auth = tweepy.OAuthHandler('PnDbc1eIqAnsDqS8yNWIKMRls', 'CEJuw59mJ3hZOgoARS2Z8GT6OhBnnxlylkNzDKx8rXMpjXWu2e')

# define o token de acesso
# para criar basta clicar em "Create my access token"
# passa o "Access Token" e o "Access Token Secret"
auth.set_access_token('1243273842845454338-OQhmg52U32DTMbtaj6sb1mc3Yu4uHm',
		'KOwORproGuGFrREs5jlIebq4jzZsRRu7VrJ7ZgQO0smpD')

# cria um objeto api
api = tweepy.API(auth)

# obtém tweets de um dado usuário
def obter_tweets_usuario(usuario, limite=50):
	resultados = api.user_timeline(screen_name=usuario, count=limite, tweet_mode='extended')
	tweets = [] # lista de tweets inicialmente vazia
	for r in resultados:
		# utiliza expressão regular para remover a URL do tweet
		# http pega o início da url
		# \S+ pega os caracteres não brancos (o final da URL) 
		tweet = re.sub(r'http\S+', '', r.full_text)
		tweets.append(tweet.replace('\n', ' ')) # adiciona na lista
	return tweets # retorna a lista de tweets

def procura_hashtag(hashtag, quantidade_procura=1 ):
    df = pd.DataFrame(columns=['tweet_id', 
                            'hashtag', 
                            'date', 
                            'text', 
                            'username', 
                            'name', 
                            'user_id', 
                            'followers_count', 
                            'location', 
                            'source', 
                            'source_url', 
                            'lang'])
    msgs = []
    msg =[]
    search_string = hashtag + ' -filter:retweets'
    for tweet in tweepy.Cursor(api.search, 
                            q=str(search_string), 
                            rpp=100, 
                            tweet_mode='extended', 
                            result_type='recent').items(quantidade_procura):
        print(tweet.full_text)
        print(tweet.lang)
        print("===============================[")
        msg = [tweet.id, 
                hashtag, 
                tweet.created_at, 
                tweet.full_text, 
                tweet.user.screen_name, 
                tweet.user.name, 
                tweet.user.id, 
                tweet.user.followers_count, 
                tweet.user.location, 
                tweet.source, 
                tweet.source_url, 
                tweet.lang] 
        msg = tuple(msg)                    
        msgs.append(msg)


        
    df = pd.DataFrame(list(msgs))
    print('------------------------------------------')
    print(msgs)
    print(df)
    return df


# escreve os tweets em um arquivo 'tweets.txt'
#tweets = obter_tweets_usuario(usuario='jairbolsonaro', limite=100)
#with open('tweets.txt', 'w') as f:
#	f.write('\n'.join(tweets))


hashtags = ["#openbanking", 
            "#remediation", 
            "#devops", 
            "#sre", 
            "#microservices", 
            "#observability", 
            "#oauth", 
            "#metrics", 
            "#logmonitoring", 
            "#opentracing"]
for x in hashtags:
    data = pd.DataFrame(columns=['tweet_id', 
                            'hashtag', 
                            'date', 
                            'text', 
                            'username', 
                            'name', 
                            'user_id', 
                            'followers_count', 
                            'location', 
                            'source', 
                            'source_url', 
                            'lang'])   
    data.append(procura_hashtag(x))

data.columns = ['tweet_id', 
                'hashtag', 
                'date', 
                'text', 
                'username', 
                'name', 
                'user_id', 
                'followers_count', 
                'location', 
                'source', 
                'source_url', 
                'lang']
print(data)
print(data.dtypes)
print(data.columns.values) 