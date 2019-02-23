import tweepy
import pprint, requests, json, time
from datetime import datetime, timedelta
import key


def get_followers(api):
    followers = []

    for follower in tweepy.Cursor(api.followers).items():
        followers.append(follower.screen_name)

    return followers

def get_tweets(api, users):
    tweets = []
    query = []

    for name in users:
        query = f'to:{name}'

        # 検索
        for status in api.search(q=query, lang='ja', result_type='recent'):
            tweet_day = status.created_at + timedelta(hours=9)
            today = datetime.today()
            a_hour_ago = today - timedelta(minutes=15)

            if tweet_day > a_hour_ago:
                tweets.append((status, name))

    return tweets

def run():
    auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
    auth.set_access_token(key.access_token_key, key.access_token_secret)
    api = tweepy.API(auth)

    followers = get_followers(api)

    tweets = get_tweets(api, followers)

    for tweet in tweets:
        tweet, name = tweet

        print(f"name: {name}\n")
        print(f"text: {tweet.text}\n")

        payload = {
            "type": "msg",
            "data": tweet.text,
            "name": tweet.user.screen_name,
            "service": "Twitter"
        }

        response = requests.post(
            'http://ik1-315-17678.vs.sakura.ne.jp/post',
            json.dumps(payload),
            headers={'Content-Type':'application/json'}
        ).json()

        if response['hit']:
            _id = tweet._json['id']
            url = f"https://twitter.com/{tweet.user.screen_name}/status/{_id}"
            message = f"@{name}\n危険なメッセージを発見しました。\n{url}"

            try:
                api.update_status(message)
            except:
                import traceback
                traceback.print_exc()

while True:
    print('run !\n')
    run()
    print('\nend !\n')
    time.sleep(60 * 15)

