# ANPR
Performing Automatic Number Plate Recognition (ANPR) using Ultralytics YOLOv8 and EasyOCR

## Summary

This project aims to develop an automated system for detecting and validating vehicle number plates in a private parking area. The system leverages a YOLO (You Only Look Once) model for number plate detection and EasyOCR for optical character recognition (OCR) to read the characters on the plates. The main objectives and components of the project are as follows:

Objectives:
- Efficient Number Plate Detection: Utilize the YOLO model to accurately and quickly identify vehicle number plates in real-time.
- Accurate Character Recognition: Implement EasyOCR to accurately extract and recognize the characters from the detected number plates.
- Automated Validation: Develop a system to automatically validate the recognized number plate characters against a pre-defined list of authorized vehicles.

A demo can be observed in **ANPR.py**. 

## Resources
- The model used in the one provided by Ultralytics, YOLOv8 [link](https://github.com/ultralytics/ultralytics)
- EasyOCR [link](https://github.com/JaidedAI/EasyOCR)
- The dataset used to train YOLOv8 for number plate detection can be obtained from this [link](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4). Make sure to format the dataset correctly in order to train the model (check Ultralytics YOLOv8 documentation).
