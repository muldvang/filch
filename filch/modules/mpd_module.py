import time
import subprocess

def run(callback):
    text = current()
    if text:
        callback(text='🎜 ' + text)
    else:
        callback(text='')
    while True:
        text = current_wait()
        if text:
            callback(text='🎜 ' + text)
        else:
            callback(text='')

def current():
    return subprocess.run(["mpc", "current"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()

def current_wait():
    return subprocess.run(["mpc", "current", "--wait"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()

