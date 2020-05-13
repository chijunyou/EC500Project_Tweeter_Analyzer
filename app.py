from flask import Flask, render_template, request, jsonify, Markup
import flask_restful
from dataprocess import bothpro
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/',methods=['GET','POST'])
def mainpage():
    if request.method == 'GET':
        print("method get")
        try:
	        return render_template('welcome.html')
        except:
            print("Fail to open welcome page")

@app.route('/search/',methods=['GET','POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        text = request.form["text"]    # get form text
        keyword = text.upper()  # process form text
        bothpro(keyword)
        return render_template('choice.html')


@app.route('/geolocation/',methods=['GET'])
def showheatmap():
    return render_template("heatmap.html")

@app.route('/chart/',methods=['GET'])
def showchart():
    return render_template("chart.html")


        




if __name__ == "__main__":
	app.run(debug=True)