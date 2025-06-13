from checker.detector import FaceDetector
from checker.matcher import find_best_match
from checker.encoder import FaceEncoder
import cv2
import os
import pickle
import numpy as np

MARGIN = 50 

face_detector = FaceDetector()
face_encoder = FaceEncoder()
db_path = "data/encodings.pkl"

if not os.path.exists(db_path):
    print("[ERROR] encodings.pkl database not found")
    exit()

with open(db_path, "rb") as f:
    face_db = pickle.load(f)

print("\n[INFO] Starting camera for face verification... Press ESC to exit")

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

if not cap.isOpened():
    print("[ERROR] Unable to open camera")
    exit()

identified_name = None

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to read from camera")
        break

    frame = cv2.flip(frame, 1)
    boxes = face_detector.detect_faces(frame)

    for (x1, y1, x2, y2) in boxes:
        h, w = frame.shape[:2]
        x1m = max(0, x1 - MARGIN)
        y1m = max(0, y1 - MARGIN)
        x2m = min(w, x2 + MARGIN)
        y2m = min(h, y2 + MARGIN)
        face_img = frame[y1m:y2m, x1m:x2m]

        face_rgb = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
        embedding = face_encoder.get_embedding(face_rgb)

        if embedding is not None:
            name, score = find_best_match(embedding, face_db)
        else:
            name, score = "Unknown", 0.0

        short_name = name.split("_")[1] if "_" in name else name
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (x1m, y1m), (x2m, y2m), color, 2)
        cv2.putText(frame, f"{short_name} ({score:.2f})", (x1m, y1m - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

        if name != "Unknown" and identified_name is None:
            identified_name = short_name
            print(f"[✓] Identity confirmed: {identified_name}")

    cv2.imshow("Face Unlock - Press ESC to Exit", frame)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
print("\n[INFO] Camera closed and exited unlock system")