from TwitterController import TwitterController
from datetime import datetime, timedelta
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
import time


class Tweet:
    controller = TwitterController()

    def __init__(self, status):
        self.status = status
        self.replies = []
        self.created_at = datetime.strptime(self.status.created_at, '%a %b %d %H:%M:%S %z %Y')
        self.max_date = self.created_at + timedelta(days=1)
        check = True
        current_id = 1
        while check:
            tweets = []
            if current_id != 1:
                tweets = Tweet.controller.search(self.status.user.screen_name,
                                                 self.created_at.strftime('%Y-%m-%d'),
                                                 self.max_date.strftime('%Y-%m-%d'),
                                                 self.status.id - 1,
                                                 current_id - 1)
            else:
                tweets = Tweet.controller.search(self.status.user.screen_name,
                                                 self.created_at.strftime('%Y-%m-%d'),
                                                 self.max_date.strftime('%Y-%m-%d'),
                                                 self.status.id - 1)

            tweets.reverse()
            print(len(tweets))
            first = True
            for tweet in tweets:
                if first:
                    first = False
                    current_id = tweet.id
                if tweet.in_reply_to_status_id == self.status.id:
                    self.replies.append(Tweet(tweet))
            check = len(tweets) > 0

    @classmethod
    def from_id(self, id):
        return Tweet(Tweet.controller.obtain_tweet(id))

    def save(self):
        with open("data/data_" + str(self.status.id) + ".json", "w") as file:
            file.write(json.dumps(self.tweet_to_json(self)))

    def get_sentiment(self, tweet):
        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(tweet.status.text)
        return vs['compound']

    def tweet_to_json(self, tweet):
        json_replies = []
        for reply in tweet.replies:
            json_replies.append(self.tweet_to_json(reply))
        root = {
            "id": tweet.status.id,
            "screen_name": tweet.status.user.screen_name,
            "text": tweet.status.text,
            "num_replies": len(tweet.replies),
            "replies": json_replies,
            "sentiment": self.get_sentiment(tweet),
            "num_retweet": tweet.status.retweet_count,
            "num_fav": tweet.status.favorite_count
        }
        return root
