#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Tweepyのインポート
import tweepy
import key

auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
auth.set_access_token(key.access_token_key, key.access_token_secret)
api = tweepy.API(auth)

message = input("text: ")
api.update_status(message)
