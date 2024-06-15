from kafka import KafkaProducer
import config
import json
import cv2
import time

topic_name = "camera"
vid_capture = cv2.VideoCapture(0)
p = KafkaProducer(
    bootstrap_servers = [config.kafka_ip],
)

while True:
    ret, frame = vid_capture.read()
    frame = cv2.resize(frame, dsize=None, fx=0.2, fy=0.2)
    
    _, buffer = cv2.imencode('.jpg', frame)
    p.send(topic_name, buffer.tobytes())
    p.flush()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print("Da gui frame")
    # time.sleep(0.1)

vid_capture.release()
cv2.destroyAllWindows()