import Adafruit_DHT
import time
import pyrebase

config = {
    "apiKey": "AIzaSyCSEfZRXcqnR2m0xDEMteYWgSCjb2Z3_dY",
    "authDomain": "iot-ai4104-raspberrypi.firebaseapp.com",
    "databaseURL": "https://iot-ai4104-raspberrypi-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "iot-ai4104-raspberrypi",
    "storageBucket": "iot-ai4104-raspberrypi.appspot.com",
    "messagingSenderId": "768493352904",
    "appId": "1:768493352904:web:64fa5c11ff34098087f2fd"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
sensor = Adafruit_DHT.DHT11
pin = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        data = {"Temperature" : temperature, "Humidity" : humidity}
        db.child("Status").push(data)
        db.update(data)
        print("Sent to Firebase")
    else:
        print('Failed to get reading. Try again!')
    time.sleep(1)