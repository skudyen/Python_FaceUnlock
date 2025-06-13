from ultralytics import YOLO

class FaceDetector:
    def __init__(self, model_path='weights/yolov8l_100e.pt', conf=0.3):
        self.model = YOLO(model_path)
        self.conf = conf

    def detect_faces(self, image):
        results = self.model.predict(image, conf=self.conf, verbose=False)
        boxes = []
        for r in results:
            for box in r.boxes.xyxy:
                x1, y1, x2, y2 = map(int, box)
                boxes.append((x1, y1, x2, y2))
        return boxes