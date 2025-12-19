# Patient Monitoring Data Producer

This project generates realistic patient vital signs data and publishes it to a Kafka topic.

## Prerequisites

-   Kafka broker
-   Python 3.9
-   `kafka-python` library

## Configuration

The following environment variables must be set:

-   `KAFKA_BROKER`: Kafka broker address (e.g., `localhost:9092`)
-   `KAFKA_TOPIC`: Kafka topic to publish to
-   `SASL_USERNAME`: SASL username for Kafka authentication
-   `SASL_PASSWORD`: SASL password for Kafka authentication
-   `GENERATION_INTERVAL`: Interval (in seconds) between data generation (default: 1)

## Usage

1.  Clone the repository:

    ```bash
    git clone https://github.com/Gautam0610/patient-monitoring-producer-new.git
    cd patient-monitoring-producer-new
    ```

2.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Set environment variables (example):

    ```bash
    export KAFKA_BROKER="your_kafka_broker"
    export KAFKA_TOPIC="your_kafka_topic"
    export SASL_USERNAME="your_sasl_username"
    export SASL_PASSWORD="your_sasl_password"
    export GENERATION_INTERVAL=2
    ```

4.  Run the producer:

    ```bash
    python producer.py
    ```

## Docker

1.  Build the Docker image:

    ```bash
    docker build -t patient-monitoring-producer .
    ```

2.  Run the Docker container (example):

    ```bash
docker run -d -e KAFKA_BROKER="your_kafka_broker" -e KAFKA_TOPIC="your_kafka_topic" -e SASL_USERNAME="your_sasl_username" -e SASL_PASSWORD="your_sasl_password" -e GENERATION_INTERVAL=2 patient-monitoring-producer
    ```