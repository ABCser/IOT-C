import paho.mqtt.client as paho
import time
import logging
import Sensor as dht11



client = paho.Client()
client.username_pw_set("IoT", "student")

if client.connect("192.168.1.34", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    exit(1)

while True:
    try:
        humidity, temperature = dht11.fetch_data()
        datetime = time.strftime("%Y-%m-%d %H:%M:%S")
        message = "{0} Temp: {1:0.1f}*C Humidity: {2:0.1f}%".format(datetime, temperature, humidity)
        print(message)
        client.publish("sensor data", message)
        client.publish("humidity", humidity)
        client.publish("temperature", temperature)
        time.sleep(5)
    except KeyboardInterrupt:
        print("KeyboardInterrupt, exiting...")
        break
    except Exception as e:
        logging.error(e)
    continue