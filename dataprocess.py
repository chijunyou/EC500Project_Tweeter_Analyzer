from getTweeter import MyListener
from keys import getkeys,getgooglekey
from tweepy import Stream
from tweepy.streaming import StreamListener
from NLP import sample_analyze_sentiment
import tweepy
import json
import urllib
from urllib.request import urlopen
import gmplot
from chart import savechar
def getdata(keyword):
    keys = getkeys()
    auth = tweepy.OAuthHandler(keys[0], keys[1])
    auth.set_access_token(keys[2], keys[3])
    listener = MyListener()
    twitterStream = Stream(auth,listener)
    twitterStream.filter(track=keyword)
    datalist = listener.datalist
    return datalist

def processdata(data):
    rtn = []
    for tw in data:
        text = tw[0]
        location = tw[1]
        latitude = None
        longitude = None
        geoloc = address(location)
        if geoloc:
            lat = geoloc[0]
            lng = geoloc[1]
        senti = 0
        try:
            senti = int(sample_analyze_sentiment(text)*5)
        except:
            senti = 0
        if senti is not None and geoloc is not None:
            rtn.append((lat,lng,senti))

    print(rtn)
    return rtn

def address(location):
    items = location.split()
    location = items[0]
    for i in range(1,len(items)):
        location = location + "%20" + items[i]

    try:
        my_googlekey = getgooglekey()
        addressUrl = "https://maps.googleapis.com/maps/api/geocode/json?address="+location+"&key="+my_googlekey
        response = urlopen(addressUrl).read().decode('utf-8')
        responseJson = json.loads(response)
        result = responseJson['results'][0]['geometry']['location']
        lat = result['lat']
        lng = result['lng']
        return (lat,lng)
    except:
        return None

def heatmap(data):
    lat = list()
    lng = list()
    for item in data:
        lat.append(item[0])
        lng.append(item[1])
    gmap = gmplot.GoogleMapPlotter(27, -96, 3)
    gmap.heatmap(lat, lng, radius=30)
    gmap.apikey = getgooglekey()
    gmap.draw("templates/heatmap.html")

def chartdata(data):

    rtn = [0,0,0,0,0,0,0,0,0,0,0]
    count = 0
    for item in data:
        try:
            senti = item[2]
            rtn[senti+5] = rtn[senti+5] + 1
            count = count + 1
        except:
            count = count
    for i in range(0,11):
        rtn[i] = rtn[i] *100 / count
        rtn[i] = int(rtn[i])
        rtn[i] = str(rtn[i]) + '%'
    return rtn

def bothpro(keyword):
    rawdata = getdata("trade war")
    data = processdata(rawdata)
    heatmap(data)
    data = chartdata(data)
    savechar(data)

if __name__== '__main__':
    all("trade war")
    #print(address('asdfsaf'))
