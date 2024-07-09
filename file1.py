import random
import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9094')
n=0
while n<10:
    keys = f"{random.randrange(999)}".encode()
    valu= f'{{"URL": "URL{random.randrange(999)}"}}'.encode()
    producer.send(
        topic='pageview',
        key=keys,
        value=valu
    )
    print(keys,valu)
    n=n+1
    time.sleep(2)
    

