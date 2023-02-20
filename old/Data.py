import can
from multiprocessing import Process, freeze_support
from time import sleep

interface = 'pcan'
channel = 'PCAN_USBBUS1'
bitrate = 250000
try:
    bus = can.interface.Bus(bustype=interface, channel=channel, bitrate=bitrate)
except Exception as e:
    print(f"Error while setting up the Interface! [{e}]")


def data(bus):
    try:
        e = True
        nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X10,00,00,00,00,00,00], is_extended_id=True)
        bus.send(nachricht)
        while True:
            bus.send(nachricht)
            msg = bus.recv(timeout=1)
            if msg.arbitration_id == 0x18EFCC03:
                print(f"{msg}" )
    except:
        print("ERROR!")

data(bus)