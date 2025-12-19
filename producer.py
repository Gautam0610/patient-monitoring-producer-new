
import os
import time
import json
import random
from kafka import KafkaProducer

# Read configuration from environment variables
KAFKA_BROKER = os.environ.get("KAFKA_BROKER")
KAFKA_TOPIC = os.environ.get("KAFKA_TOPIC")
SASL_USERNAME = os.environ.get("SASL_USERNAME")
SASL_PASSWORD = os.environ.get("SASL_PASSWORD")
GENERATION_INTERVAL = int(os.environ.get("GENERATION_INTERVAL", 1))

# Configure Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    sasl_mechanism='PLAIN',
    security_protocol='SASL_SSL',
    sasl_plain_username=SASL_USERNAME,
    sasl_plain_password=SASL_PASSWORD,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


def generate_vitals():
    # Generate realistic vital signs with occasional extreme values
    heart_rate = random.randint(60, 100)
    breaths_per_minute = random.randint(12, 20)
    temperature = round(random.uniform(36.5, 37.5), 1)
    spo2 = random.randint(95, 100)

    # Randomly inject extreme values
    if random.random() < 0.01:  # 1% chance of extreme heart rate
        heart_rate = random.randint(120, 180)  # Tachycardia
    elif random.random() < 0.005: # 0.5% chance of extremely low heart rate
        heart_rate = random.randint(30, 50)

    if random.random() < 0.01:  # 1% chance of extreme breaths per minute
        breaths_per_minute = random.randint(25, 40)  # Tachypnea
    
    vitals = {
        "heart_rate": heart_rate,
        "breaths_per_minute": breaths_per_minute,
        "temperature": temperature,
        "spo2": spo2,
        "timestamp": time.time()
    }
    return vitals


if __name__ == "__main__":
    while True:
        vitals_data = generate_vitals()
        print(f"Sending: {vitals_data}")
        producer.send(KAFKA_TOPIC, value=vitals_data)
        time.sleep(GENERATION_INTERVAL)
