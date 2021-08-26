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

i=0

while(1):
    data = bytearray()
#    time.sleep(1)

#        BytesToSend = ConvertStringsToBytes("A") 
#        bus.write_i2c_block_data(0x62, 0x00, BytesToSend) 
        
        #data += bytearray(bus.read_i2c_block_data(0x62, 0x00, 22))
        #data += bytearray(bus.read_i2c_block_data(0x62, 0x01, 22))
        
        #Convert bytearray ke float
        #arr = array.array('f', data)
        #print(arr.tolist())
#        print(i)
        
        #sys.stdout.buffer.write(data)
        #sys.stdout.flush()
#        i=i+1
#    time.sleep(1)
    BytesToSend = ConvertStringsToBytes("D") 
    bus.write_i2c_block_data(0x62, 0x00, BytesToSend) 
#        time.sleep(1)
#        BytesToSend = ConvertStringsToBytes("C") 
#        bus.write_i2c_block_data(0x62, 0x00, BytesToSend) 
#        time.sleep(1)
#        BytesToSend = ConvertStringsToBytes("D") 
#        bus.write_i2c_block_data(0x62, 0x00, BytesToSend) 
#        time.sleep(1)
#        BytesToSend = ConvertStringsToBytes("E") 
#        bus.write_i2c_block_data(0x62, 0x00, BytesToSend) 
#        time.sleep(1)
#        BytesToSend = ConvertStringsToBytes("F") 
#        bus.write_i2c_block_data(0x62, 0x00, BytesToSend) 
#        time.sleep(1)
#        BytesToSend = ConvertStringsToBytes("G") 
#        bus.write_i2c_block_data(0x62, 0x00, BytesToSend) 
    break




