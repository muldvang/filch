import multiprocessing
import time

CPU_COUNT = multiprocessing.cpu_count()

def run(callback):
    while True:
        loadavg = load()
        if CPU_COUNT < float(loadavg):
            callback(text=' ' + loadavg, color='#A52A2A')
            time.sleep(1)
        else:
            time.sleep(10)

def load():
    with open('/proc/loadavg', mode='r') as fp:
        all_of_it = fp.read()
        load_within_past_minute = float(all_of_it.split()[0])
        formatted = '{0:.1f}'.format(load_within_past_minute)
        return formatted
