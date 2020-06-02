import getWeibo
import baiduNLP
import json
import urllib
from urllib.request import urlopen
import gmplot
from chart2 import savechar2

def getdata(keyword):
    datalist, geolist = getWeibo.runWeibo(keyword)
    return datalist, geolist

def chartdata(keyword):
    dlist, glist = getdata(keyword)
    sentiment = baiduNLP.sentiment(dlist)
    yaxis = baiduNLP.plot(sentiment)
    return yaxis


def twopro(keyword):
    data = chartdata(keyword)
    savechar2(data)

if __name__ == '__main__':
    twopro('alanniuniu')



