from time import sleep
from pyroute2 import IPDB, IPRoute
from netifaces import AF_INET

def interface():
    import pyudev
    context = pyudev.Context()
    devs = [x for x in context.list_devices(subsystem='net') if 'DEVTYPE' in x and x['DEVTYPE'] == 'wlan']
    if len(devs) > 1:
        raise Exception('Expected only a single wlan device')
    return devs[0]['INTERFACE']

ip = IPRoute()
ipdb = IPDB()
interface = interface()

def run(callback):
    connection_established = connected()
    callback(text = '', color = color(connection_established))

    def new_address_callback(ipdb, netlink_message, action):
        if action == 'RTM_NEWADDR' or action == 'RTM_DELADDR':
            connection_established = connected()
            callback(text = '', color = color(connection_established))

    ipdb.register_callback(new_address_callback)
    while True:
        sleep(1)

def connected():
    return not ip.get_addr(label=interface) == ()

def color(connection_established):
    return '#4E9A06' if connection_established else '#A52A2A'


