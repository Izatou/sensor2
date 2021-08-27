import smbus
import struct
import sys
import time
import array

bus = smbus.SMBus(1)


def ConvertStringsToBytes(src):
  converted = []
  for b in src:
    converted.append(ord(b))
  return converted


def rlyOn():
    data = bytearray()
    BytesToSend = ConvertStringsToBytes("B") 
    bus.write_i2c_block_data(0x62, 0x00, BytesToSend) 


def rlyOff():
    data = bytearray()
    BytesToSend = ConvertStringsToBytes("A") 
    bus.write_i2c_block_data(0x62, 0x00, BytesToSend)
    
    
def start():
    data = bytearray()
    BytesToSend = ConvertStringsToBytes("D") 
    bus.write_i2c_block_data(0x62, 0x00, BytesToSend)
    
def dataSensor():
    data = bytearray()
#        data += bytearray(bus.read_i2c_block_data(0x62))
    data += bytearray(bus.read_i2c_block_data(0x62, 0x00, 22))
    data += bytearray(bus.read_i2c_block_data(0x62, 0x01, 22))
    arr = array.array('f', data)
    arr[10]=arr[9]
    arr[9]=arr[8]        
    arr[8] = 0
    return arr
                             
def stop():
    data = bytearray()
    BytesToSend = ConvertStringsToBytes("C") 
    bus.write_i2c_block_data(0x62, 0x00, BytesToSend)