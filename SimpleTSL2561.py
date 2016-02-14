#!/usr/bin/python
#
# SimpleTSL2561.py by aike
# licenced under MIT License. 
#

import smbus
import time

class SimpleTSL2561:

    def __init__(self, address=0x39):
	self.bus = smbus.SMBus(1)
	self.address = address
        self.write8(0x80, 0x03)     # 0x03=PowerON 0x00=PowerOFF

    def write8(self, reg, value):
        try:
            self.bus.write_byte_data(self.address, reg, value)
        except IOError, err:
            print "IO Error"

    def readU16(self, reg):
        try:
            result = self.bus.read_word_data(self.address,reg)
            return result
        except IOError, err:
            print "IO Error"
            return 0

    def setParam(self, param):
	#  param   gain   integral
	#    0      x 1   13.7 ms
	#    1      x 1    101 ms
	#    2      x 1    402 ms  (default)
	#    3     x 16   13.7 ms
	#    4     x 16    101 ms
	#    5     x 16    402 ms
	if param >= 3:
	    param = param - 3 + 16
	self.write8(0x81, param)

    def readData(self):
        return self.readU16(0xAC)

if __name__ == "__main__":
	tsl = SimpleTSL2561()
	while True:
		print tsl.readData()
		time.sleep(1)

