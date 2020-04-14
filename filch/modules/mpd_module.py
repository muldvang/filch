import time
import subprocess

def run(callback):
    while True:
        text = current()
        if text:
            callback(text='🎵 ' + text, color='#A52A2A')
        else:
            callback(text='')
        time.sleep(10)

def current():
    return subprocess.run(["mpc", "current"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
