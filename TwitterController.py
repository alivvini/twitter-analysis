import keys.twitter
import twitter

class TwitterController:
    
    def __init__(self):
        self.api = twitter.Api(consumer_key=keys.twitter.API_KEY,
                  consumer_secret=keys.twitter.API_SECRET,
                  access_token_key=keys.twitter.ACCESS_TOKEN,
                  access_token_secret=keys.twitter.ACCESS_TOKEN_SECRET)

    def obtain_tweet(self, id):
        return self.api.GetStatus(id)

    def search(self, username, since, until, since_id, until_id = None):
        query = 'vertical=default&src=typd&qf=off&count=100&result_type=recent'
        params = []
        params.append('since_id='+str(since_id))
        params.append('q=to%3A'+username+' since%3A'+since+' until%3A'+until)
        if until_id!=None:
            params.append('until_id='+str(until_id))
        for param in params:
            query += ("&" + param)
        return self.api.GetSearch(raw_query=query)        
    