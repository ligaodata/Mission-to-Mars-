from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars 


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def home():
    Marsinfo_data = mongo.db.collection.find_one()
    print(Marsinfo_data)
    return render_template("index.html", mars_data = Marsinfo_data)

@app.route("/scrape")
def scraper():
    Marsinfo_data = scrape_mars.scrape_info() 
    mongo.db.collection.update({}, Marsinfo_data, upsert = True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

      
