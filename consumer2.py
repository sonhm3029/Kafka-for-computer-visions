import json
from kafka import KafkaConsumer
import config

c = KafkaConsumer(
    "nhac_vang",
    bootstrap_servers = [config.kafka_ip],
    auto_offset_reset = "earliest",
    group_id="consumer-group-a"
)

for message in c:
    print("Da nhan", message.value)