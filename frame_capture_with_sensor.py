"""
フレーム単位で画像を記録し，フレームIDに紐づいたセンサー値を記録する
"""

import cv2
from src.save_sensor_img import Data_Saver
from src.prepare import prepare
import os

FRAME_WIDTH = 640  # MAX 2592
FRAME_HEIGHT = 480 # MAX 1944

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

dir_path = prepare(cap)


data_saver = Data_Saver(
    save_video=True, 
    save_sensor=True, 
    output_video_dir=os.path.join(dir_path, "video"),
    output_sensor_dir=os.path.join(dir_path, "sensor"),
    )

while True:
    ret, frame = cap.read()
    # cv2.imshow('test', frame)
    key = cv2.waitKey(27)
    sensor_dict = None
    data_saver.save(frame, sensor_dict, '-')
