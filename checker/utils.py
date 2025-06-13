import cv2

def crop_faces(image, boxes, margin=50):
    faces = []
    h, w = image.shape[:2]
    for (x1, y1, x2, y2) in boxes:
        x1m = max(0, x1 - margin)
        y1m = max(0, y1 - margin)
        x2m = min(w, x2 + margin)
        y2m = min(h, y2 + margin)
        face = image[y1m:y2m, x1m:x2m]
        faces.append(face)
    return faces

def draw_boxes(image, boxes, labels=None):
    for i, (x1, y1, x2, y2) in enumerate(boxes):
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        if labels:
            cv2.putText(image, labels[i], (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    return image