import json
import time

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BCM)

broker_address = 'rpi3a'
broker_port = 1883
client_id = "my-client"
soil_sensor_pin = 17
GPIO.setup(soil_sensor_pin, GPIO.IN)


# Callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("watering")


def on_message(client, userdata, msg):
    try:
        decoded_message = json.loads(msg.payload.decode())
        # {"gpio_pin": 21, "activated": true}
        relay_pin = decoded_message["gpio_pin"]
        activated = decoded_message["activated"]

        if activated:
            print("activating the relay...")
            GPIO.setup(relay_pin, GPIO.OUT)
            GPIO.output(relay_pin, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(relay_pin, GPIO.LOW)
            time.sleep(3)
        else:
            print("deactivating the relay...")
            GPIO.output(relay_pin, GPIO.LOW)

        print("Received message: " + str(decoded_message))

    except():
        print("Unable to process message!")


client = mqtt.Client(client_id=client_id, clean_session=True)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("rpi3a", "mypassword")
client.connect(broker_address, port=broker_port, keepalive=60)
client.loop_start()

# Wait for messages
try:
    while True:
        needsWater = GPIO.input(soil_sensor_pin)
        msg = {
            "needs_water": needsWater
        }
        soil_sensor_message = json.dumps(msg)
        client.publish("watering", soil_sensor_message)
        time.sleep(5)


except KeyboardInterrupt:
    pass

# Disconnect from the broker
client.loop_stop()
client.disconnect()
