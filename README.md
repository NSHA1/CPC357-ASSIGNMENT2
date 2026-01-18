==============================================
Development Environment Setup 
==============================================
The development environment for this IoT Smart Parking System was deployed on Google Cloud Platform (GCP) using a Linux-based virtual machine. The setup process is described step-by-step to ensure reproducibility.

Step 1: Google Cloud Platform Setup
- A GCP project was created using Google Cloud Console.
- A Compute Engine Virtual Machine (VM) was launched.
- VM configuration:
    -Operating System: Ubuntu Linux
    -Machine Type: e2-micro (sufficient for lightweight IoT workloads)
    -SSH access was enabled to allow remote development through the GCP browser-based terminal.

Step 2: System and Development Tools Installation
After accessing the VM via SSH, the system was updated and required tools were installed:
- Python 3 – main programming language for sensor simulation, middleware, and backend
- pip – Python package manager
- MongoDB – NoSQL database for storing parking data
- Mosquitto MQTT Broker – message broker for IoT communication

Python libraries install:
- paho-mqtt – for MQTT publish/subscribe communication
- pymongo – for MongoDB interaction
- flask – for backend web server and REST API
- flask-cors – to enable cross-origin requests from the frontend

Step 3: Code Repository Structure
The IoT application was organized into a structured code repository hosted on the GCP VM:

parking_dashboard_api/
-parking_sensor.py (virtual sensor)      
-mqtt_to_mongo.py  (MongoDB)
-app.py (flask backed API)     
-index.html (frontend)             

Step 4: Application Execution Flow
- parking_sensor.py simulates parking slot status and publishes data to MQTT topics.
- mqtt_to_mongo.py subscribes to the MQTT topic and stores incoming data into MongoDB.
- app.py runs a Flask server that retrieves data from MongoDB and exposes RESTful API endpoints.
- index.html pick up data from the Flask API and displays parking slot status in a web-based table.

Step 5: Testing and Verification
- MongoDB data was verified using the MongoDB shell.
- MQTT message flow was validated through live terminal outputs.
- The web dashboard was accessed via browser to confirm real-time data display.

A detailed step by stepguide is avaialble in the report.
