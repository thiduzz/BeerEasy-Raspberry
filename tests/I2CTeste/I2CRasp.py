# -*- coding: utf-8 -*-
import smbus
import time
import pigpio


address = 0x04
count = 0;
bus = smbus.SMBus(1)
pi = pigpio.pi()


def writeData(value):	
	for i in value:
		bus.write_byte(address, ord(i))	
		
	bus.write_byte(address, ord('\n'))	
	return -1

#precisa inicializar sudo pigpiod

def readData():
	handle = pi.i2c_open(1, address)
	(count, byteArray) = pi.i2c_read_device(handle,32)
	pi.i2c_close(handle)
	string = ""
	for b in byteArray:
		if(b < 128 and b != None):
			string += chr(b)
	#string = ""
	#data = 1
	#while data != 10 and data != 32 and data != 0:
	#	data = bus.read_byte(address)
	#	if(data < 128):
	#		string += chr(data)
	return string
	
	
while True:
	var = raw_input("Enter something:")
	if not var:
		continue
	writeData(var)
	#readData()
	string = readData()
	print string
