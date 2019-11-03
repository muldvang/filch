from datetime import datetime
import time

def run(callback):
    while True:
        now = datetime.now()
        formatted = now.strftime("%a, %b %d, %H:%M")
        callback(formatted)
        time.sleep(60 - int(now.strftime("%S")))
