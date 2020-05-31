# EC500 Project: Twitter Analyzer
Team Members: Junyou Chi, Hanchen Zhang

## Project Summary
The goal of this project is to use APIs to analyze Twitter feeds

## User Stories
- As a product designer, I want to know costomers' preference.
- As a businessman, I want to know the geolocation of the potential costomers.
- As someone who cares about news, I want to know the candidate's exposure.

## API Used in Project
1. tweepy -used to gethering twitter data
2. google.cloud.language -used to get sentimental score of twitter feeds
3. googleapis -used to get the latitude and longtitude of a adress given by name
4. gmplot -used to generate a heatmap

## Our API
In our project. We did 2 API in dataprocess.py. The first is chartapi which can be import by `from dataprocess import chartapi`. The second is mapapi which can be import by `from dataprocess import mapapi`. By the way there is an combination of those two which can be import by `from dataprocess import proboth`.

### chartapi
The chartapi can get a key word and path as input to generate a html page with a histogram of the sentiment distribution about the key word. Once user called the chartapi with a key word, the html page will be automaticly saved as the path in input. The format of input looks like `chartapi(keyword,path = "templates/chart.html")`. 
In the chart, negative means negative sentiment, positive means positive sentiment and magnitude means the tensity of sentiment. For example, 5 means most positve sentiment and 0 means neutral.

p align="center">   
<img src="https://github.com/chijunyou/EC500Project_Tweeter_Analyzer/blob/master/pictures/sentiment.png" /> 
</p> 

### mapapi
The mapapi can get a key word and path as input to generate a html page with a heatmap of tweeter feed about the key word. Once user called the mapapi with a key word, the html page will be automaticly saved as the path in input. The format of input looks like `mapapi(keyword,path = "templates/heatmap.html")`

p align="center">   
<img src="https://github.com/chijunyou/EC500Project_Tweeter_Analyzer/blob/master/pictures/heatmap.png" /> 
</p> 

### proboth
This api do both of the previous APIs. it get a keyword and a path as input. The format of input looks like `proboth(keyword,path = "templates")`. It will save `/chart.html` and `/heatmap.html` under path.



### UI
Once visit  `http://127.0.0.1:5000/` after deployed flask, there will be a welcome page

<p align="center">   
<img src="https://github.com/chijunyou/EC500Project_Tweeter_Analyzer/blob/master/pictures/welcome.png" /> 
</p> 

After click the "GO to Analyzer" button, there will be search page. You can type a key word into the blank and then click "Analyze" to generate chart and map.

<p align="center">   
<img src="https://github.com/chijunyou/EC500Project_Tweeter_Analyzer/blob/master/pictures/search.png" /> 
</p> 

Then, you can choose to see the chart or the heatmap by clicking "Sentimental Analyzing" or "Geolocation Analyzing". By the way, after you see one of the analyzed result, you can click backward bottun on browser and chooce the other one without wait for analyzing time.

<p align="center">   
<img src="https://github.com/chijunyou/EC500Project_Tweeter_Analyzer/blob/master/pictures/analyze%20choice.png" /> 
</p> 

## Chinese Version
1. For any reasons that makes the google and twitter related api not functioning (e.g: in China), we have a substitution:
  微博（weibo, "microblog") substitute Twitter
  百度地图 (baidu map）substitute Google Map
2. Most of the features are similar with the Twitter+Google model, but there are also some features that has little bit differences. Detailed description will be dicussed in the next section. There are buttons from the web frontend for user to choose the Chinses veriosn option.

## How to Run This Code
1. Type`git clone https://github.com/chijunyou/EC500Project_Tweeter_Analyzer.git` to your terminal to clone the repository.
2. Type `cd EC500Project_Tweeter_Analyzer` to navigate into the project folder.
3. Add your twitter API keys and Google map API key in to the `key`file.
(for Twitter API problems, please visit: https://developer.twitter.com/en/docs)
(for Google map API problem, please visit: https://developers.google.com/maps/documentation)
4. Save your own Cloud Natural Language API key as a json file.
5. For Windows user: type `set GOOGLE_APPLICATION_CREDENTIALS=[JSON_KEY_PATH]`; For Lunix or MacOS type `export GOOGLE_APPLICATION_CREDENTIALS="[JSON_KEY_PATH]"`.
(for Google Cloud Natural Language API problem, please visit: https://cloud.google.com/natural-language/docs/quickstarts)
6. Type `pip install -r requirements.txt` to run install modules.
7. Type `python app.py` to deploy flask
8. Navigate to `http://127.0.0.1:5000/`.

## References
* https://css-tricks.com/separate-form-submit-buttons-go-different-urls/
* https://blog.csdn.net/cakecc2008/article/details/79114456
* https://www.cnblogs.com/R0b1n/p/5225351.html#7geolocation-and-interactive-maps
* https://www.cnblogs.com/coolqiyu/p/7152786.html
* https://www.cnblogs.com/shuai7boy/p/9208857.html
* https://blog.csdn.net/guoweish/article/details/47171733
* https://jupyter-gmaps.readthedocs.io/en/latest/tutorial.html
* https://www.tutorialspoint.com/plotting-google-map-using-gmplot-package-in-python
* https://developer.twitter.com/en/docs
* https://developers.google.com/maps/documentation
* https://cloud.google.com/natural-language/docs/quickstarts)
