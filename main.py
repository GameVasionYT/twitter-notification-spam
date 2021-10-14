import tweepy, time, sys
from tweepy import OAuthHandler
import logging
import random
import os
from flask import Flask
from threading import Thread

sentences = ('you\'re a nerd', 'You\'re a nerd', 'I don\'t know if I said this already but... you\'re a nerd') # Doing random so tweepy doesn't block it
sentence = random.choice(sentences)


auth = tweepy.OAuthHandler("CONSUMER_KEY", 
    "CONSUMER_SECRET_KEY")
auth.set_access_token("ACCESS_TOKEN", 
    "ACCESS_TOKEN_SECRET")
toReply = "USERNAME" #user to get most recent tweet
api = tweepy.API(auth)


tweets = api.user_timeline(screen_name = toReply, count=100) # The ammount of tweets you want to check (Set to 100 for 100 notifs)

for tweet in tweets:
    api.update_status("@" + toReply + " " + sentence, in_reply_to_status_id = tweet.id)
    #time.sleep(5) # You can remove the "#" from before time.sleep if you want a delay
