"""
画像データ収集の準備を行う
- データ記録用のフォルダの準備
- カメラパラメータの記録
"""
import cv2
import os
import datetime
import json

def prepare(cap)->str:
    """
    cap: cv2.VideoCapture()の戻り値
    作成したディレクトリへのパスを返す
    """
    dt_now = datetime.datetime.now()
    dir_path = "./data/" +\
            str(dt_now.year) + "_" + \
            str(dt_now.month) + "_" + \
            str(dt_now.day) + "_" + \
            str(dt_now.hour) + "_" + \
            str(dt_now.minute)
    os.makedirs(dir_path, exist_ok=True)
    print('data is saved to ' + dir_path)

    # カメラパラメータの保存
    parameters = {
        "CAP_PROP_FRAME_WIDTH": cap.get(cv2.CAP_PROP_FRAME_WIDTH),  # 縦画素数
        "CAP_PROP_FRAME_HEIGHT": cap.get(cv2.CAP_PROP_FRAME_HEIGHT),  # 横画素数
        "CAP_PROP_FOURCC": cap.get(cv2.CAP_PROP_FOURCC)  # 圧縮フォーマット
    }

    with open(os.path.join(dir_path, "camera_parameters.json"), "w") as f:
        json.dump(parameters, f)

    return dir_path