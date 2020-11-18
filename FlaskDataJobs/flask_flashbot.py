from flask import Flask, render_template, url_for, request, session, redirect, jsonify
import json
from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
#client = MongoClient('localhost',27017)
app.config["MONGO_URI"] = "mongodb://localhost:27017/jobs_data"
app.config['MONGO_DBNAME'] = 'top_posts'
mongo = PyMongo(app)
db = mongo.db
col = mongo.db["top_posts"]
#print ("MongoDB Database:", mongo.db)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/search', methods = ['GET'])
def search():
    search = col
    output = []
    for q in search.find():
        output.append({'title' : q['title'], 'description' : q['description'],
        'link':q['link'],'pubDate':q['pubDate'],'guid':q['guid']})
    return jsonify({'result' : output})


if __name__ == '__main__':
     app.run(debug=True)