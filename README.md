# リポジトリ概要
雑草検知水上ドローンoyoneの学習データを集めるためのプログラム

# コード
* camera_test.py  
カメラが正常に動作するかを確認
* frame_capture.py  
ラズパイカメラで得た画像を保存するプログラム
* video_capture.py  
ラズパイカメラで得た画像を動画形式(mp4)で保存するプログラム
* prepare.py  
実行時刻のフォルダを作成後、カメラパラメータをjson形式で保存する。
* check_cpu_temp.py  
cpu温度を返す関数を格納したファイル

# 実行コマンド
画像で保存する場合
```
python frame_capture.py
```
動画で保存する場合
```
python videoi_capture.py
```