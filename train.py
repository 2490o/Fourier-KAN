from ultralytics import YOLOv10


# 模型配置文件
model_yaml_path = "/home/zzh/yolov10/ultralytics/cfg/models/v10/yolov10x-KAN-P5.yaml"
#数据集配置文件
data_yaml_path = '/home/zzh/yolov10/data/daytime_clear/data.yaml'
# data_yaml_path = '/home/zzh/yolov10/ultralytics/cfg/datasets/VOC.yaml'
#预训练模型
pre_model_name = 'yolov10x.pt'

if __name__ == '__main__':
    #加载预训练模型
    model = YOLOv10(model_yaml_path).load(pre_model_name)
    #训练模型
    results = model.train(data=data_yaml_path,
                          epochs=300,
                          batch=6,
                          name='train_x_1.12_noaug_KAN_P5')