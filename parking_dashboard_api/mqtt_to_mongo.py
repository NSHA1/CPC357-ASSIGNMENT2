import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client['iot_db']
collection = db['parking_lots']

# MQTT setup
broker = "localhost"  # or your broker IP
port = 1883
topic = "parking/sensors"

# Called when connected to MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with code", rc)
    client.subscribe(topic)
    print("Subscribed to topic:", topic)

# Called when a message is received
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Received from MQTT:", data)           # 🔹 debug: see the message
    collection.insert_one(data)                  # insert into MongoDB
    print("Inserted into MongoDB:", data)        # 🔹 confirm insertion

# Create MQTT client and attach callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to broker and start listening
client.connect(broker, port)
client.loop_forever()
