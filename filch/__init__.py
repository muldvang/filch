# Module
import sys
import time
from threading import Thread
from . import updater
from .modules import audio_module, time_module, dropbox_module, wlan_module, internet_module,\
     battery_module, load_module, mpd_module

def run():
    sys.stdout.write('{"version":1}\n')
    sys.stdout.write('[\n')
    sys.stdout.write('[]\n')

    MODULES = [dropbox_module, mpd_module, audio_module, wlan_module, internet_module, battery_module, load_module, time_module]
    MODULE_NAMES = {module:'Module of ' + str(module) for module in MODULES}

    UPDATER = updater.Updater(MODULE_NAMES.values())

    for module in MODULES:
        thread = Thread(name=MODULE_NAMES[module], target=lambda: module.run(UPDATER.updater_hook(MODULE_NAMES[module])), daemon=True)
        thread.start()

    while True:
        time.sleep(1)
