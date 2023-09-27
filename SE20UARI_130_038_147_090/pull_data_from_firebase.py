import firebase_admin
from firebase_admin import credentials, db
import json 

cred = credentials.Certificate("Raspi/iot-ai4104-raspberrypi-firebase-adminsdk-r0e63-c6cddb140c.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-ai4104-raspberrypi-default-rtdb.asia-southeast1.firebasedatabase.app'
})

ref = db.reference('/')

data = ref.get()

file_path = "DHT_sensor_data.json"

with open(file_path, "w") as f:
    json.dump(data, f)