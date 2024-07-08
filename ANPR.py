import cv2
import matplotlib.pyplot as plt
import pandas as pd
from utils import filter_plate, sharp_kernel
import time

from ultralytics import YOLO
import easyocr

# read number plate database
plate_df = pd.read_csv('number_plate_database.csv')

# Load easyOCR module
reader = easyocr.Reader(['en'], gpu=True)

# Import YOLO model
model = YOLO('models/license_detect.pt')

# start checking video
video_path = 'test_videos/test_video1080.mp4'
cap = cv2.VideoCapture(video_path)

if cap.isOpened() == False:
    print("Error with VIdeo")

counter = 0
frame_skip = 30

while cap.isOpened():
    ret, frame = cap.read()
    success = 0

    # check that a frame is extracted
    if not ret:
        break
    
    if (counter % frame_skip) == 0:

        # reset counter
        counter = 0

        # make prediction
        results = model.predict(frame, conf=0.5, verbose=False, show=False)
        for result in results:
            boxes = result.boxes # get bounding boxes
            for box in boxes:    # take care of multiple boxes (just in case)
                if box.cls.cpu().numpy() == [0]: # check for license
                    license_box = box.xyxy.cpu().numpy().astype(int)[0]
                    license = frame[license_box[1]:license_box[3], license_box[0]:license_box[2], :]
                    
                    # resize - test with scaling and standard sizing
                    # scale = 2
                    #height = int(license.shape[0] / scale)
                    #width = int(license.shape[1] / scale)
                    height = 200
                    width = 350
                    license = cv2.resize(license, (width, height), interpolation=cv2.INTER_AREA)

                    # NEW TASK - attempt more image processing (grayscale, convolution)
                    license = cv2.cvtColor(license, cv2.COLOR_BGR2GRAY)

                    cv2.imshow('frame detection', license)

                    # easyOCR
                    plate_text = reader.readtext(license, detail=0)
                    plate_number = filter_plate(plate_text)
                    
                    # check for plate in database
                    for text in plate_number:
                        if text in plate_df['number_plate'].values:
                            print("Access Granted")
                            success = 1
                            break
                        else:
                            print("Detection in process...")

    if success == 1:
        print("Door opening")
        start = time.time()
        for i in range(2000):
            ret, frame = cap.read()
            if cv2.waitKey(5) == ord('q'):
                break
        end = time.time()
        elapsed = end - start
        print(elapsed)

    counter += 1

    if cv2.waitKey(5) == ord('q'):
        break
            