import machine
import time

from ota_updater import OTAUpdater

def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/edblagg/hello-world')
    o.install_update_if_available_after_boot('OUTATIME', '2712271227')


def start():
     # This program prints Hello, world!
    print('Hello, world!')


def boot():
    download_and_install_update_if_available()
    start()

pin=machine.Pin(2, machine.Pin.OUT)
pin.on()
time.sleep(2)
pin.off()
time.sleep(2)
pin.on()
time.sleep(2)
pin.off()
print('Hello, world, v1.0.1')

boot()
