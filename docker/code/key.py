import tweepy
import os

def autentica_twitter():
    auth = tweepy.OAuthHandler('PnDbc1eIqAnsDqS8yNWIKMRls', 
                            'CEJuw59mJ3hZOgoARS2Z8GT6OhBnnxlylkNzDKx8rXMpjXWu2e')
    auth.set_access_token('1243273842845454338-OQhmg52U32DTMbtaj6sb1mc3Yu4uHm',
                        'KOwORproGuGFrREs5jlIebq4jzZsRRu7VrJ7ZgQO0smpD')
    return tweepy.API(auth)