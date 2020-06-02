import sinaweibopy3
import webbrowser
import json
import re
APP_KEY =''
APP_SECRET=''
REDIRECT_URL ='https://api.weibo.com/oauth2/default.html'


def weiboFilter(list1,username):
	a = 0
	list2 = []
	for i in list1:
		a = a + 1
		user = i['user']['screen_name']
		#print("第",a,"条微博, ","当前用户名："+user)
		if user == username:
			list2.append(i)
	return list2

def filter_text(text):
        re_tag = re.compile('</?\w+[^>]*>')  # HTML标签
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        #new_text = re.sub(r"http\S+", "", text)
        new_text = re.sub(re_tag, '', text)
        new_text = re.sub(pattern, '', new_text)
        new_text = re.sub(",+", ",", new_text)   # 合并逗号
        new_text = re.sub(" +", " ", new_text)   # 合并空格
        new_text = re.sub("[...|…|。。。]+", "...", new_text)  # 合并句号
        new_text = re.sub("-+", "--", new_text)  # 合并-
        new_text = re.sub("———+", "———", new_text)  # 合并-
        return new_text
# ————————————————This Regulation function mainly imported from the following:————————————————
# 版权声明：本文为CSDN博主「CS青雀」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/ztf312/article/details/87352580

def runWeibo(selectedname):
	client = sinaweibopy3.APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=REDIRECT_URL)
	url = client.get_authorize_url()
	webbrowser.open_new(url)
	result = client.request_access_token(input("please input code : "))
	client.set_access_token(result.access_token, result.expires_in)

	result = client.fs_friends()
	raw_statuses = result['statuses']

	statuses = weiboFilter(raw_statuses,selectedname)
	length = len(statuses)
	usertext=[]
	if length == 0:
		print("亲，你好像没关注"+selectedname)
		# This printout is to shown that user didn't subsribe the
		# channel that they searched
	else:
		alltext = []
		allgeo = []
		wfile = open('weibo.txt', 'w')
		jfile = open('weibo.json', 'w')
		gfile = open('geo.json', 'w')
		for i in statuses:
			geoloc = i['geo']
			if geoloc != None:
				latitude = geoloc['coordinates'][0]
				longitude = geoloc['coordinates'][1]
				print(type(latitude))
				geodict = { "lng": longitude, "lat": latitude, "count": 100 }
				allgeo.append(geodict)
			text = i['text']
			text_clean = filter_text(text)
			alltext.append(text_clean)

			wfile.write(text_clean+"\n")
		json.dump(alltext, jfile)
		json.dump(allgeo, gfile)

		
		print ('Done writing to the file')

		wfile.close()
		gfile.close()
		usertext = alltext
		usergeo = allgeo
	return usertext, usergeo


if __name__ == '__main__':
    #pass in the username of the account you want to download
    runWeibo('璇仔仔')#
