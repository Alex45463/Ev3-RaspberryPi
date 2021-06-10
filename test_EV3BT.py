#! /usr/bin/env python3
import serial
import time
import EV3BT

EV3 = serial.Serial('/dev/rfcomm0')

s = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'message', "RaspberryPi4!")
EV3.write(s)
print(s)
EV3.close()
