from checker.detector import FaceDetector
from checker.encoder import FaceEncoder
from checker.database import FaceDatabase
import cv2
import os
import re

MARGIN = 50
face_detector = FaceDetector()
face_encoder = FaceEncoder()
face_db = FaceDatabase()

data_path = "dataset"
os.makedirs(data_path, exist_ok=True)

existing_ids = []
for folder in os.listdir(data_path):
    match = re.match(r"person_.*_(\d+)", folder)
    if match:
        existing_ids.append(int(match.group(1)))

next_id = max(existing_ids) + 1 if existing_ids else 1

user_name = input("Please type name : ").strip()
safe_name = "".join(c for c in user_name if c.isalnum() or c in ['_', ' ']).strip().replace(" ", "_")
if not safe_name:
    safe_name = f"user_{next_id}"

folder = os.path.join(data_path, f"person_{safe_name}_{next_id}")
os.makedirs(folder, exist_ok=True)
print(f"\n[INFO] บันทึกภาพที่: {folder}")

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

if not cap.isOpened():
    print("[ERROR] Fails to Open Camera")
    exit()

count = 0
MAX_IMAGES = 30
print(f"\n[INFO] เริ่มจับภาพใบหน้า (สูงสุด {MAX_IMAGES} รูป)\n... Press ESC to quit early.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Can't read picture from Camera")
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

        if count < MAX_IMAGES:
            file_path = os.path.join(folder, f"{next_id}_{count}.jpg")
            cv2.imwrite(file_path, face_img)
            print(f"[Saved] {count+1}/{MAX_IMAGES} → {file_path}")

            try:
                face_resized = cv2.resize(face_img, (112, 112))
                face_rgb = cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB)  # ✅ แปลงเป็น RGB
                embedding = face_encoder.get_embedding(face_rgb)
                if embedding is not None:
                    face_db.add_embedding(f"person_{safe_name}_{next_id}", embedding)
                    print("  [→] Save embedding success")
                else:
                    print("  [×] Face not found. encoding Fails")
            except Exception as e:
                print(f"  [!] Error encoding: {e}")

            count += 1

        cv2.rectangle(frame, (x1m, y1m), (x2m, y2m), (255, 0, 0), 2)

    cv2.imshow(f"Register {user_name} - Press ESC to Exit", frame)
    k = cv2.waitKey(100) & 0xff
    if k == 27 or count >= MAX_IMAGES:
        break

cap.release()
cv2.destroyAllWindows()
print("\n[INFO] เสร็จสิ้นการจับภาพใบหน้าและสร้าง embeddings แล้ว")
