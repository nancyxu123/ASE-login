from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
from flask_pymongo import PyMongo
app = Flask(__name__)


app.config['MONGO_DBNAME']='toydb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/toydb'

mongo = PyMongo(app)
"""
1.  Programming languages: Python, HTML, JavaScript
2.  Web Development Application Framework: Flask
3.  Build tool: pip/virtualenv
4.  Static analysis bug finder tool: pylint
5.  Unit testing tool: pytest
6.  Persistent Data Source: MySQL
7.  Continuous integration tool: Travis-CI
"""

@app.route("/")
@app.route("/index")
def index():
    usernames = mongo.db.usernames # create a collection called usernames
    output = [username["ticker"] for username in usernames.find()]
    return render_template("index.html", usernames=output)

@app.route("/add_user", methods=["POST"])
def add_user():
    usernames = mongo.db.usernames
    user = request.form["user"]
    ticker_id = usernames.insert({"user": user})

    for username in usernames.find():
	if user == username:
	    continue;
	else:
	    ticker_id = usernames.insert({"user": user")
    

def check_username(s):
    usernames = mongo.db.usernames
    for username in usernames.find():
        if s == username:
            return "Username Exists!"
    return "Username does not exist"




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
