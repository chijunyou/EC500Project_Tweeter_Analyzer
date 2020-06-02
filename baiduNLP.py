import requests
import ast
import json
from chart2 import savechar2
import numpy as np

API_KEY = ''
SECRET_KEY = ''

def sentiment(data):

	response = requests.get(
	    url='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
	        API_KEY, SECRET_KEY
	    ), headers={'Content-Type': 'application/json; charset=UTF-8'})

	allsentiment = []
	for d in data:
		single = '{"text":"'+d+'"}'
		r = requests.post(
		    url='https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token={}'.format(
		        ast.literal_eval(response.text)['access_token']),
		    headers={'Content-Type': 'application/json'},
		    data=single.encode('utf8')
		)

		allsentiment.append(r.text)
	return allsentiment


def plot(list):
	hist = [0,0,0,0,0,0,0,0,0,0]
	for stat in list:
		b = json.loads(stat)
		print(type(b))
		poscomp = int(10*b['items'][0]['positive_prob'])
		hist[poscomp] += 1
	for i in range(0,len(hist)):
		a = hist[i]/(len(list))
		hist[i] = a
	print(hist)
	return hist

if __name__ == '__main__':
	a = sentiment()
	b = plot(a)
	savechar2(b)
