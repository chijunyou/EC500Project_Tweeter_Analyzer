import tweepy
import json
from keys import getkeys
from tweepy import Stream
from tweepy.streaming import StreamListener
import time
import argparse
import gmaps
class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    def __init__(self):
        self.count = 0
        self.datalist = list()

    def on_data(self, data):
        try:
            tweet = json.loads(data)
            geolocation = tweet['user']['location']
            tweetext = tweet['text']
            if geolocation:
                #print(tweet)
                self.count = self.count + 1
                self.datalist.append((tweetext,geolocation))
            print(self.count)
            if self.count >= 25:
                return False
            
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

def getTweets(searchterm):
    keys = getkeys()
    auth = tweepy.OAuthHandler(keys[0], keys[1])
    auth.set_access_token(keys[2], keys[3])
    api = tweepy.API(auth, wait_on_rate_limit=True)
    termlength=len(searchterm)
    tweetlist=[]

    for tweets in api.search(q=searchterm, lang = 'en', result_type = 'recent', count = 10):
        tweetlist.append(tweets.text)


    return tweetlist





if __name__== '__main__':
    keys = getkeys()
    auth = tweepy.OAuthHandler(keys[0], keys[1])
    auth.set_access_token(keys[2], keys[3])
    listener = MyListener()
    twitterStream = Stream(auth,listener)
    twitterStream.filter(track=["obama"])
    print(listener.datalist)
    print("lisener done")
    #getTweets("Obama")
