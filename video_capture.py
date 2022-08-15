import cv2
import numpy as np
from prepare import prepare
from check_cpu_temp import get_cpu_temp
import os

cap = cv2.VideoCapture(0)

DIR_PATH = prepare(cap)

fps = int(cap.get(cv2.CAP_PROP_FPS))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter(os.path.join(DIR_PATH, "output.mp4"), fourcc, fps, (w, h))

while True:
    try:
        ret, frame = cap.read()
        out.write(frame)
        print(get_cpu_temp())
    except:
        print(f"frame size: {frame.shape}")
        break
cap.release()
out.release()