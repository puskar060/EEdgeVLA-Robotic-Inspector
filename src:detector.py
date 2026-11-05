import cv2
from ultralytics import YOLO
import numpy as np

class StructuralInspector:
    def __init__(self, model_path="yolov8n.pt"):
        """
        YOLOモデルの初期化（初期状態では軽量なyolov8nを使用。
        現場の要件に応じて、ひび割れや異常検知用のカスタム学習モデルに変更可能）
        """
        self.model = YOLO(model_path)

    def detect_anomalies(self, image: np.ndarray):
        """
        画像から構造上の異常や欠陥を検出し、バウンディングボックスを描画する
        """
        results = self.model(image)
        annotated_image = results[0].plot()
        
        detections = []
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = self.model.names[cls_id]
            detections.append({"label": label, "confidence": conf})

        return annotated_image, detections