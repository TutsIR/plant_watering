import paho.mqtt.client as mqtt

broker_address = 'rpi3a'
broker_port = 1883
client_id = "my-client"


# Callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("my/topic")


def on_message(client, userdata, msg):
    print("Received message: " + msg.payload.decode())


client = mqtt.Client(client_id=client_id,
                     clean_session=True)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("rpi3a", "mypassword")
client.connect(broker_address, port=broker_port, keepalive=60)
client.loop_start()

client.publish("my/topic", "Hello, MQTT!")

# Wait for messages
try:
    while True:
        pass
except KeyboardInterrupt:
    pass

# Disconnect from the broker
client.loop_stop()
client.disconnect()
