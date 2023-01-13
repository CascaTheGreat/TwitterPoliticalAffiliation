from flask import Flask, jsonify, request
import Scraper

app = Flask(__name__)

user = ""
lean = [
    {}
]

@app.route("/")
def hello():
    return Scraper.scrape("ASCTEAlabama")

@app.route("/polIdent")
def get_lean():
    return jsonify(lean)

@app.route("/polIdent", methods=["POST"])
def set_user():
    user = request.get_json()
    print(user)
    Scraper.scrape(user)
    return '', 204