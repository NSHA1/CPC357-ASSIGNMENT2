import paho.mqtt.client as mqtt
import json
import time
import random

# Replace with your VM External IP
BROKER_IP = "localhost"
TOPIC = "parking/sensors"

client = mqtt.Client()
client.connect(BROKER_IP, 1883, 60)

parking_slots = ["P1", "P2", "P3"]

while True:
    for slot in parking_slots:
        payload = {
            "slot_id": slot,
            "status": random.choice(["Occupied", "Available"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        client.publish(TOPIC, json.dumps(payload))
        print(f"Sent: {payload}")
    time.sleep(10)
