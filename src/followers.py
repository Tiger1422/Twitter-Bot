import tweepy
import time
import key

auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
auth.set_access_token(key.access_token_key, key.access_token_secret)
api = tweepy.API(auth)

followers = []

for follower in tweepy.Cursor(api.followers).items():
    print( follower.screen_name )

    followers.append(follower.screen_name)
    time.sleep(5)


print(followers)
