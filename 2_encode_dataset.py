import os
import cv2
import pickle
from checker.encoder import FaceEncoder

encoder = FaceEncoder()
data_path = "dataset"
save_path = "data/encodings.pkl"
os.makedirs("data", exist_ok=True)

face_db = {}

print("\n[INFO] เริ่ม encode โดยใช้ InsightFace ตรวจจับ + encode เองแบบเร็วสุด...\n")

for folder_name in os.listdir(data_path):
    folder_path = os.path.join(data_path, folder_name)
    if not os.path.isdir(folder_path):
        continue

    name = folder_name
    face_db[name] = []
    count_success = 0

    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)
        img = cv2.imread(img_path)
        if img is None:
            print(f"[WARN] อ่านภาพไม่ได้: {img_path}")
            continue

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        faces = encoder.app.get(rgb)

        if not faces:
            print(f"[WARN] ❌ ไม่พบใบหน้าใน {img_path}")
            continue

        for face in faces:
            embedding = face.embedding
            face_db[name].append(embedding)
            count_success += 1

    print(f"[OK] ✅ ได้ embedding {count_success} รูปจาก {name}")

with open(save_path, "wb") as f:
    pickle.dump(face_db, f)

print(f"\n[INFO] 🧠 บันทึกฐานข้อมูลลงที่ {save_path}")