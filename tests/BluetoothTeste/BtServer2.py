import os
import glob
import time
import RPi.GPIO as GPIO
from bluetooth import *


server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"


while True:
    print "Waiting for connection on RFCOMM channel %d" % port

    client_sock, client_info = server_sock.accept()
    print "Accepted connection from ", client_info

    try:
            client_sock.send("Hello!")


    except IOError:
        pass

    except KeyboardInterrupt:

        print "disconnected"

        client_sock.close()
        server_sock.close()
        print "all done"

        break