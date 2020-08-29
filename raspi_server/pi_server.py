import Servomotor
import servomot
import servo_walk_3
from socket import *
from time import ctime
import RPi.GPIO as GPIO

#Servomotor.setup()
#servomot.setup()
servo_walk_3.setup()
ctrCmd = ['1','0', '3', '4']

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)
data1 = 'Up'

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
        print 'Waiting for connection'
        tcpCliSock,addr = tcpSerSock.accept()
        print '...connected from :', addr
        try:
                while True:
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE)
                        if not data:
                                #print("Not data")
                                break
                        if data == ctrCmd[0]:
                                print 'Up' 
                                #servomot.rotmul()
                                #Servomotor.ServoUp()
                                servo_walk_3.walking()
                                print 'Increase: '
                        if data == ctrCmd[1]:
                                print 'Down'
                                #servomot.rotmul()
                                #Servomotor.ServoDown()
                                print 'Decrease: '
                        if data == ctrCmd[2]:
                                print 'Left'
                                servo_walk_3.left()
                                print 'Turned Left'
                        if data == ctrCmd[3]:
                                print 'Right'
                                servo_walk_3.right()
                                print 'Turned Right'
        except KeyboardInterrupt:
                #Servomotor.close()
                #servomot.close()
                servo_walk_3.close()
                GPIO.cleanup()
tcpSerSock.close();
