from ultralytics import YOLOv10



if __name__ == '__main__':
    # 加载预训练模型
    model = YOLOv10('/home/zzh/yolov10/runs/detect/train_x_1.7_oral/weights/best.pt')
    # 训练模型cd
    model.val(data='/home/zzh/yolov10/data/daytime_foggy/data.yaml', batch=32)
    model.val(data='/home/zzh/yolov10/data/night_sunny/data.yaml', batch=32)
    model.val(data='/home/zzh/yolov10/data/dusk_rainy/data.yaml', batch=32)
    model.val(data='/home/zzh/yolov10/data/night_rainy/data.yaml', batch=32)
    model.val(data='/home/zzh/yolov10/data/daytime_clear/data.yaml', batch=32)

    # model.val(data='/home/zzh/yolov10/data/clipart/data.yaml', batch=32)
