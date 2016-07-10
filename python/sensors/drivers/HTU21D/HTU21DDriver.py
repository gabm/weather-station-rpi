# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import logging
import math


# Default I2C address for device.
HTU21D_I2CADDR_DEFAULT        = 0x40

# Register addresses.
HTU21D_READ_TEMP                = 0xE3
HTU21D_READ_HUMIDITY            = 0xE5
HTU21D_WRITE_REG                = 0xE6
HTU21D_READ_REG                 = 0xE7
HTU21D_READ_RESET               = 0xFE



class HTU21DDriver(object):

	def __init__(self, address=HTU21D_I2CADDR_DEFAULT, i2c=None, **kwargs):
		"""Initialize MCP9808 device on the specified I2C address and bus number.
		Address defaults to 0x18 and bus number defaults to the appropriate bus
		for the hardware.
		"""
		if i2c is None:
			import Adafruit_GPIO.I2C as I2C
			i2c = I2C
		self._device = i2c.get_i2c_device(address, **kwargs)


	def readTempC(self):
		"""Read sensor and return its value in degrees celsius."""
		# Read temperature register value.
		t = self._device.readU16BE(HTU21D_READ_TEMP)
		# Scale and convert to signed value.
		temperature = ((t / float(65536)) * 175.72 ) - 46.85
		return temperature
	
	def readRelativHumidity(self):
		h = self._device.readU16BE(HTU21D_READ_HUMIDITY)
		humidity = ((h / float(65536)) * 125) - 6
		return humidity

    
if __name__ == "__main__":
    sensor = HTU21DDriver()
    #print sensor.readTempC()
    print sensor.readRelativHumidity()
