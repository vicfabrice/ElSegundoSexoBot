# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 22:29:03 2020

@author: VicFabrice
"""
from config import consumer_key,consumer_secret,access_token,access_token_secret 

import tweepy

from tweepy.auth import OAuthHandler


try:
    import urllib3.contrib.pyopenssl
    urllib3.contrib.pyopenssl.inject_into_urllib3()
except ImportError:
    pass


# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumerKey = consumer_key
consumerSecret = consumer_secret

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
accessToken = access_token
accessTokenSecret = access_token_secret

auth = tweepy.auth.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

#def countingChars(quote):
    



def tweetQuote(quote):
    api.update_status(status=quote)
    print(quote)
# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
#api.update_status(status='NOTA: Este libro ha sido escrito durante los años 1948-1949. Cuando empleo las palabras ahora, recientemente, etc., me refiero a ese período. Ello explica también que no cite ninguna obra publicada después de 1949. ')
 
quote = "La discusión sobre el feminismo ha hecho correr bastante tinta; actualmente está punto menos que cerrada: no hablemos más de ello."

tweetQuote(quote)