import time
import subprocess

def run(callback):
    while True:
        text = current()
        if text:
            callback(text='🎜 ' + text)
        else:
            callback(text='')

def current():
    return subprocess.run(["mpc", "current", "--wait"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
