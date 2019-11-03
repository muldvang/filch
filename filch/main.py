import sys
import time
from threading import Thread
from updater import Updater
from modules import audio_module, time_module, dropbox_module, wlan_module, internet_module,\
    battery_module, load_module

if __name__ == '__main__':
    sys.stdout.write('{"version":1}\n')
    sys.stdout.write('[\n')
    sys.stdout.write('[]\n')

    MODULES = [audio_module, dropbox_module, wlan_module, internet_module, battery_module, load_module, time_module]
    MODULE_NAMES = {module:'Module of ' + str(module) for module in MODULES}

    UPDATER = Updater(MODULE_NAMES.values())

    for module in MODULES:
        thread = Thread(name=MODULE_NAMES[module], target=lambda: module.run(UPDATER.updater_hook(MODULE_NAMES[module])), daemon=True)
        thread.start()

    while True:
        time.sleep(1)
