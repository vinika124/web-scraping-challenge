from flask import Flask, render_template, redirect, url_for
from flask_pymongo import Pymongo
import scrape_mars

app = Flask(__name__)

# Flask set up connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = Pymongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find.one()
    return render_template("index2.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars

    mars_data = scraping.scrape_all()

    mars.update({},mars_data, upsert=True)
    
    return redirect('/', code=302)
    
if __name__ == "__main":
    app.run(debug=True)