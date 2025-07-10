import cv2
import time
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    tracking_id = 0 

    results = model(frame)[0]

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        class_id = int(box.cls[0])
        label = model.names[class_id]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} ({conf:.2f}) - ID: {tracking_id}",
                    (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255), 2)

        tracking_id += 1

    cv2.imshow("YOLOv8 Object Detection", frame)

    if cv2.waitKey(1) == 27 or time.time() - start_time > 10:
        break

cap.release()
cv2.destroyAllWindows()
