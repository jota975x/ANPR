from ultralytics import YOLO

def main():
    model = YOLO('yolov8n.pt')
    results = model.train(data="datasets/roboflow2/data.yaml", epochs=10, imgsz=640, batch=16, device=0, amp=False)

    return results

if __name__ == '__main__':
    main()