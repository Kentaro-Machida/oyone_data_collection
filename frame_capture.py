import cv2

from prepare import prepare
import os
import time
from check_cpu_temp import get_cpu_temp

# WIDTH: MAX 2592, default 640
# HEIGHT: MAX 1944, default 480
# ただし、画素数を最大値にすると色チャネルがおかしくなる
# (WIDTH, HEIGHT) = (1280, 960) までは正しく表示される

WIDTH = 1280
HEIGHT = 960

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
frame_id = 0

DIR_PATH = prepare(cap)

start_time = time.perf_counter()
while True:
    try:
        ret, frame = cap.read()
        img_name = "frame_" + str(frame_id) + ".jpg"
        img_path = str(os.path.join(DIR_PATH, img_name))
        cv2.imwrite(img_path, frame)
        frame_id += 1
        print(get_cpu_temp()) # cpu温度を表示
    except:
        # keyborad interupt でfpsを記録する
        end_time = time.perf_counter()
        execute_time = end_time - start_time
        fps = int(frame_id / execute_time)
        print(f"\n{fps=}")
        print(f"frame size: {frame.shape}")
        with open(os.path.join(DIR_PATH, "fps.txt"), "w") as f:
            f.write(str(fps))
        break
cap.release()