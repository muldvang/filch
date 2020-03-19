import time
from threading import Thread
import datetime
import pyudev


def run(callback):
    def c(battery):
        callback(text=text(battery), color=color(battery))

    Battery(c)
    while True:
        time.sleep(1)


def color(battery):
    if battery.state() == 'Charging':
        return '#4E9A06'
    if battery.pct() < 10:
        return '#A52A2A'
    return None


def text(battery):
    icon = {0: '',
            10: '',
            30: '',
            60: '',
            90: ''}
    approx_pct = max(k for k in icon if k <= battery.pct())

    time_remaining = battery.time_remaining()
    if not battery.state() == 'Charging' \
       and battery.pct() < 10 \
       and time_remaining:
        return icon[approx_pct] + ' ' + time_remaining
    return icon[approx_pct]


class Battery:
    def __init__(self, callback):
        self.callback = callback
        self.update()
        udev_thread = Thread(target=self.update_on_udev_change, daemon=True)
        udev_thread.start()
        time_thread = Thread(target=self.update_timely, daemon=True)
        time_thread.start()

    def update_on_udev_change(self):
        context = pyudev.Context()
        monitor = pyudev.Monitor.from_netlink(context)
        monitor.filter_by('power_supply')
        for device in iter(monitor.poll, None):
            if device.sys_name == 'BAT0':
                self.update()

    def update_timely(self):
        while True:
            self.update()
            if self.pct() < 10:
                time.sleep(10)
            else:
                time.sleep(60)

    def update(self):
        self.info = fetch_raw_values()
        self.callback(self)

    def state(self):
        return self.info['POWER_SUPPLY_STATUS']

    def pct(self):
        return self.info['POWER_SUPPLY_CAPACITY']

    def time_remaining(self):
        if "POWER_SUPPLY_POWER_NOW" in self.info:
            present_rate = self.info["POWER_SUPPLY_POWER_NOW"]
            if present_rate > 0:
                remaining_energy = self.info["POWER_SUPPLY_ENERGY_NOW"]
                time_in_secs = remaining_energy / present_rate * 3600
                return seconds_to_hms(time_in_secs)
        return None


def fetch_raw_values():
    raw_values = {}
    with open('/sys/class/power_supply/BAT0/uevent', mode='r') as f:
        for var in f.read().splitlines():
            k, v = var.split("=")
            try:
                raw_values[k] = int(v)
            except ValueError:
                raw_values[k] = v
    return raw_values


def seconds_to_hms(secs):
    return str(datetime.timedelta(seconds=secs)).split('.')[0]
