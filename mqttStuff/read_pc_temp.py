# MQTT_PORT = 1883 or 9001
# MQTT_TOPIC = "Pi5/Temperature"
# cmd Script to Post to mqtt.
# /etc/systemd/pub_temp.service is the location for the service that runs the script # pub_temp.py

import wmi
import paho.mqtt.client as mqtt
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

MQTT_BROKER = "192.168.1.19"
MQTT_PORT = 1883
MQTT_TOPIC = "pc/temperature"

def get_cpu_temperature():
    try:
        w = wmi.WMI(namespace="root\\wmi")
        temperature_info = w.MSAcpi_ThermalZoneTemperature()
        if not temperature_info:
            return None
        
        for temp in temperature_info:
            temperature_celsius = temp.CurrentTemperature / 10.0 - 273.15
            temperature_fahrenheit = temperature_celsius * 9 / 5 + 32
            return round(temperature_fahrenheit, 3)
    except Exception as e:
        logging.error(f"Error getting temperature: {e}")
        return None

def on_connect(client, userdata, flags, rc):
    logging.info(f"Connected with result code {rc}")

def on_publish(client, userdata, mid):
    logging.info("Message Published")

# Create MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()

    while True:
        temperature = get_cpu_temperature()
        if temperature:
            client.publish(MQTT_TOPIC, temperature)
            logging.info(f"Published temperature: {temperature}°F")
        time.sleep(60)  # Publish temperature every 60 seconds

except KeyboardInterrupt:
    logging.info("Script interrupted by user")

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    client.loop_stop()
    client.disconnect()
    logging.info("MQTT client disconnected")
