from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client['iot_db']
collection = db['parking_lots']

# API route to get parking data
@app.route("/api/parking")
def get_parking():
    slots = list(collection.find({}, {"_id": 0}))  # exclude _id
    return jsonify(slots)

# Route to serve HTML dashboard
@app.route("/")
def dashboard():
    return send_from_directory(os.getcwd(), "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
