import cv2
from ultralytics import YOLO
import time
import os

# Get the path to the Downloads folder
downloads_folder = os.path.expanduser('~/Downloads')

model = YOLO('yolov8n.pt') # pass any model type
results = model(source=0,show = True, conf=0.4,save=True)