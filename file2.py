from kafka import KafkaConsumer

# Define the Kafka consumer
consumer = KafkaConsumer('pageview',
#                        auto_offset_reset='earliest',
                        group_id='pageview-group1',
                        bootstrap_servers=['localhost:9094'])  # Ensure the bootstrap server is correct

# Start consuming messages
consumer.subscribe(['pageview'])
for message in consumer:
    print(message.value,message.key)

