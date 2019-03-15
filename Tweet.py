from TwitterController import TwitterController
from datetime import datetime, timedelta


class Tweet:

    controller = TwitterController()

    def __init__(self, status):
        self.status = status
        self.replies = []
        self.created_at = datetime.strptime(self.status.created_at, '%a %b %d %H:%M:%S %z %Y')
        self.max_date = self.created_at + timedelta(days=1)
        check = True
        current_id=1
        while check:
            tweets = []
            if current_id !=1:
                tweets = Tweet.controller.search(self.status.user.screen_name, 
                        self.created_at.strftime('%Y-%m-%d'),
                        self.max_date.strftime('%Y-%m-%d'),
                        self.status.id-1,
                        current_id-1)
            else:
                tweets = Tweet.controller.search(self.status.user.screen_name, 
                        self.created_at.strftime('%Y-%m-%d'),
                        self.max_date.strftime('%Y-%m-%d'),
                        self.status.id-1)
            tweets.reverse()
            print(len(tweets))
            first = True
            for tweet in tweets:
                if first:
                    first = False
                    current_id = tweet.id
                if tweet.in_reply_to_status_id==self.status.id:
                    self.replies.append(Tweet(tweet))
            check = len(tweets) > 0
        
        # TODO: Obtain the replies and save them and obtain

    @classmethod
    def from_id(self, id):
        return Tweet(Tweet.controller.obtain_tweet(id))


    def save(self):
        # TODO: create a method that saves the current tweet (and all its replies into a json file)
        pass
        