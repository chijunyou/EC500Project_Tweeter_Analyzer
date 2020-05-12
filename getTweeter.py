import tweepy
from keys import getkeys
def getTweets(searchterm):
    keys = getkeys()
    print(keys)
    auth = tweepy.OAuthHandler(keys[0], keys[1])
    auth.set_access_token(keys[2], keys[3])
    api = tweepy.API(auth, wait_on_rate_limit=True)
    termlength=len(searchterm)
    tweetlist=[]

    for tweets in api.search(q=searchterm, lang = 'en', result_type = 'recent', count = 10):
        tweetlist.append(tweets.text) 
    return tweetlist

if __name__== '__main__':

	print(getTweets("Obama"))
