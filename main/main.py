import machine
import time
import network


ssid_name = 'OUTATIME'
ssid_pwrd = '2712271227'

nic = network.WLAN(network.STA_IF)
nic.active(True)
wifi_data = nic.scan()

nic.connect(ssid_name, ssid_pwrd)

for x in range(1,10):
    print('sleep cycle1', x)
    print(nic.isconnected())
    time.sleep(1)
if nic.isconnected() == True:
    print('Wifi Connected Successfully')

def start():
     # This program prints Hello, world!
    print('Hello, world!')

pin=machine.Pin(2, machine.Pin.OUT)
pin.on()
time.sleep(2)
pin.off()
print('Hello, world - v.1.0.0')

start()
