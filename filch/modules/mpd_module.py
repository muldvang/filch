import time
import subprocess

def run(callback):
    update(callback)
    while True:
        wait_for_change()
        update(callback)


def update(callback):
    if is_playing():
        text = current()
        callback(text='🎜 ' + text)
    else:
        callback(text='')

def is_playing():
    return '[playing]' in subprocess.run(["mpc"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()

def current():
    return subprocess.run(["mpc", "current"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()


def wait_for_change():
    subprocess.run(["mpc", "idle"])
