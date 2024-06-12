import json
from kafka import KafkaConsumer
import config
import cv2
import numpy as np

c = KafkaConsumer(
    "camera",
    bootstrap_servers = [config.kafka_ip],
    auto_offset_reset = "latest",
    fetch_max_bytes=9000000,
    fetch_max_wait_ms=10000,
    group_id="camera-consumer-group"
)

for message in c:
    stream = message.value
    stream = np.frombuffer(stream, dtype=np.uint8)
    image = cv2.imdecode(stream, cv2.IMREAD_COLOR)
    cv2.imshow("frame", image)
    cv2.waitKey(1)