from ultralytics import YOLOv10

import torch

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    raise Exception("CUDA is not")

model_path = r"/home/zzh/yolov10/runs/detect/train_x_11-6-VOC/weights/best.pt"
model = YOLOv10(model_path)
results = model(source=r'/home/zzh/yolov10/runs/detect/predict/ART/*',
                name='predict/exp_ART',
                conf=0.45,
                save=True,
                device='0'
                )