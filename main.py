import smbus
import time
import pigpio
import os
import glob
from bluetooth import *

address = 0x04
count = 0;
bus = smbus.SMBus(1)
#precisa inicializar sudo pigpiod
pi = pigpio.pi()


server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("",1))
server_sock.listen(1)
port = server_sock.getsockname()[1]
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
advertise_service( server_sock, "AquaPiServer", service_id = uuid,
	service_classes = [ uuid, SERIAL_PORT_CLASS ],
	profiles = [ SERIAL_PORT_PROFILE ]
	)




def writeData(value):	
	for i in value:
		bus.write_byte(address, ord(i))	
		
	bus.write_byte(address, ord('\n'))	
	return -1


def readData():
	handle = pi.i2c_open(1, address)
	(count, byteArray) = pi.i2c_read_device(handle,32)
	pi.i2c_close(handle)
	string = ""
	for b in byteArray:
		if(b < 128 and b != None):
			string += chr(b)
	return string
	
	
#while True:
	######I2C TEST
	#var = raw_input("Enter something:")
	#if not var:
	#	continue
	#writeData(var)
	#readData()
	#string = readData()
	#print string
	
	#####BT TEST
	#print "Waiting for connection..."
	#client_sock, client_info = server_sock.accept()
	#print "Accepted connection from ", client_info
	#try:
	#	data = client_sock.recv(1024)
	#	if len(data) == 0: break
	#	print "received [%s]" % data
	#	client_sock.send("FAZ CERTO!")
	#except IOError:
	#	pass
	#except KeyboardInterrupt:
	#	print "disconnected!"
	#	client_sock.close()
	#	server_sock.close()
	#	print "all done"
	#	break