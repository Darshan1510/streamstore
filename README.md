# StreamStore

A simple Kafka-based order tracking system demonstrating producer-consumer architecture using Confluent Kafka Python library.

## Overview

This project consists of:
- **producer.py**: Sends order messages to a Kafka topic.
- **tracker.py**: Consumes and processes order messages from the Kafka topic.
- **docker-compose.yaml**: Sets up a single-node Kafka broker using KRaft mode.

## Prerequisites

- Python 3.8 or higher
- Docker and Docker Compose
- Confluent Kafka Python library (install via pip)

## Setup

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/Darshan1510/streamstore.git
   cd streamstore
   ```

2. **Install Python dependencies**:
   ```bash
   pip install confluent-kafka
   ```

3. **Start Kafka**:
   ```bash
   docker-compose up -d
   ```

   This will start a Kafka broker on `localhost:9092`.

## Usage

### Running the Producer

The producer sends a sample order to the 'orders' topic.

```bash
python producer.py
```

**Example Output**:
```
Message delivered to orders [0] with message {"order_id": "123e4567-e89b-12d3-a456-426614174000", "user": "user_123", "item": "Pizza", "quantity": 2}
```

### Running the Consumer

The tracker consumes messages from the 'orders' topic and processes them.

```bash
python tracker.py
```

**Example Output**:
```
Starting order tracker...
Received order: {"order_id": "123e4567-e89b-12d3-a456-426614174000", "user": "user_123", "item": "Pizza", "quantity": 2}
Processing order 123e4567-e89b-12d3-a456-426614174000 for 2 x Pizza by user_123
```

Press `Ctrl+C` to stop the consumer.

### Checking Topics

To list all topics in Kafka:

```bash
docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092
```

## Configuration

- **Kafka Bootstrap Servers**: `localhost:9092`
- **Topic**: `orders`
- **Consumer Group**: `order-tracker`

## Stopping Kafka

```bash
docker-compose down
```

## Notes

- The Kafka setup uses KRaft mode for simplicity (no Zookeeper required).
- Orders are JSON objects with fields: `order_id`, `user`, `item`, `quantity`.
- The producer generates a random UUID for each order ID.
