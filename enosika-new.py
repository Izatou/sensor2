import time
import sys
import RPi.GPIO as GPIO
import smbus
import struct
from gpiozero import LED
from commandi2c import rlyOn, rlyOff, start, stop, dataSensor

pompa = LED(24)
pompa.on() # memastikan pompa off
rlyOn()
print("pompa.on()")


while (1):
    data = bytearray()
    arr = dataSensor()    
    print(arr.tolist())
    for i in range (8):
        data += bytearray(struct.pack("f", int(arr[i])))
    data += bytearray(struct.pack("f", arr[9]))
    data += bytearray(struct.pack("f", arr[10]))
    print(data)
    sys.stdout.buffer.write(data)
    sys.stdout.flush()
    time.sleep(1)