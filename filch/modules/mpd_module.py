import time
import subprocess

def run(callback):
    while True:
        text = current()
        if text:
            callback(text='🎜 ' + text)
        else:
            callback(text='')
        time.sleep(10)

def current():
    return subprocess.run(["mpc", "current"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
