from flask import Flask, render_template, request, jsonify, Markup
import flask_restful

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/',methods=['GET'])
def welcome():
	return render_template('welcome.html')



if __name__ == "__main__":
	app.run(debug=True)