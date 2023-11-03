import paho.mqtt.client as mqtt

# Definir los datos de conexión
broker_address = "broker.hivemq.com"
port = 1883  # Puerto predeterminado para MQTT
topic = "utpl"  # Cambia "mi_evento" al nombre de tu evento

# Función que se ejecuta cuando se conecta al broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker MQTT UTPL INTEROPERABILIDAD")
        client.subscribe(topic)
    else:
        print(f"Error al conectarse, código de retorno: {rc}")

# Función que se ejecuta cuando se recibe un mensaje
def on_message(client, userdata, message):
    print(f"Mensaje recibido en el tema '{message.topic}': {message.payload.decode()}")

# Configurar el cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conectarse al broker
client.connect(broker_address, port)


# Mantener el cliente en funcionamiento
client.loop_forever()