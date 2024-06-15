from kafka import KafkaProducer
import config
import json
import time

topic_name = "nhac_vang"

def get_partition(key, all, available):
    return 0

p = KafkaProducer(
    bootstrap_servers = [config.kafka_ip],
    partitioner = get_partition    
)

json_mess = json.dumps({"name": "son"}) 
while True:
    p.send(topic_name, json_mess.encode("utf-8"))
    p.flush()

    print("Da gui")
    time.sleep(5)