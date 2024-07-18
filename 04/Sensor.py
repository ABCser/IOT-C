import adafruit_dht
import logging
import board

dht_device = adafruit_dht.DHT11(board.D4)

def fetch_data():
  try:
    humidity = dht_device.humidity
    temperature = dht_device.temperature
    # print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
    return humidity, temperature
  except Exception as e:
    logging.error(e) 
    raise e