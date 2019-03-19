from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json


def load_json(tweetid):
    with open('data/data_' + str(tweetid) + '.json') as json_file:
        data = json.load(json_file)
        return data


def analyze_sentiment(tweet):
    analyzer = SentimentIntensityAnalyzer()
    for sentence in tweet['replies']:
        vs = analyzer.polarity_scores(sentence['text'])
        print("{:-<65} {}".format(sentence['text'], str(vs)))
        analyze_sentiment(sentence)


tweet_json = load_json(1105974640592281601)
analyze_sentiment(tweet_json)


