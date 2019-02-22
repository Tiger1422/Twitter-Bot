import tweepy
import pprint
import datetime
import key

# Twitterに接続＆認証
auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
auth.set_access_token(key.access_token_key, key.access_token_secret)
api = tweepy.API(auth)

# 検索
for status in api.search(q='"アイカツ"', lang='ja', result_type='recent',count=100):
    print("-*-*-*-*-")
    print(f"name: {status.user.name}\n")    # ユーザ名を表示
    print(f"text: {status.text}\n")         # ツイートの内容を表示
    print(f"time: {status.created_at + datetime.timedelta(hours=9)}\n") # 時間を表示
    print("-*-*-*-*-\n\n")


