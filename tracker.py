from confluent_kafka import Consumer
import json

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'order-tracker', "auto.offset.reset": 'earliest'}

consumer = Consumer(consumer_config) # bootstrap servers is used to connect to kafka cluster

consumer.subscribe(['orders']) # Subscribe to the 'orders' topic

print("Starting order tracker...")

try:
    while True:
        msg = consumer.poll(1.0)  # Poll for messages

        if msg is None:
            continue  # No message received, continue polling
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        value = msg.value().decode('utf-8')
        print(f"Received order: {value}")  # Print the received message

        order = json.loads(value)

        print(f"Processing order {order['order_id']} for {order['quantity']} x {order['item']} by {order['user']}")
except KeyboardInterrupt:
    print("\n Stopping order tracker...")
finally:
    consumer.close()  # Close the consumer to commit final offsets