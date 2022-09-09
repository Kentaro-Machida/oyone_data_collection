import subprocess
import re

def get_cpu_temp():
    # 実行コマンド
    cmd = "vcgencmd measure_temp"

    # pythonからシェル呼び出し
    temp = subprocess.check_output(cmd.split())

    # 文字列として取得
    temp = temp.decode("utf-8")
    temp = re.sub('\n', '', temp)
    return temp

if __name__=='__main__':
    print(get_cpu_temp())
