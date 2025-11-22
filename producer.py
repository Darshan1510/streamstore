from confluent_kafka import Producer
import uuid
import json

producer_config = {
    'bootstrap.servers': 'localhost:9092'}

producer = Producer(producer_config) # bootstrap servers is used to connect to kafka cluster

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] with message {msg.value().decode('utf-8')}")

order = {
    "order_id": str(uuid.uuid4()),
    "user" : "user_123",
    "item": "Pizza",
    "quantity": 2
}

# Kafka requires messages to be in bytes
value = json.dumps(order).encode('utf-8')

producer.produce(topic='orders', value=value, callback=delivery_report) # If topic does not exist, it will be created automatically, produce will run in batch mode for efficiency
producer.flush() # Ensure all messages are sent before exiting