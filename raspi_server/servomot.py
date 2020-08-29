import RPi.GPIO as GPIO
import time

def setup():
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(11, GPIO.OUT)
   global p
   p=GPIO.PWM(11, 50)
   p.start(0)
   p.ChangeDutyCycle(0)

def setangle_up():
    global duty
    duty=(90/18)+2
    GPIO.output(11, True)
    p.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(11, False)
    p.ChangeDutyCycle(0)
    print('Degrees the Servo was rotated by: ')
    print('90')
    
def setangle_down():
    global duty
    duty=(180/18)+2
    GPIO.output(11, True)
    p.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(11, False)
    p.ChangeDutyCycle(0)
    print('Degrees the Servo was rotated by: ')
    print('180')

def rotmul():
    global i
    i=0
    for i in range (5):
       global duty1, duty2
       duty1=(90/18)+2
       duty2=(180/18)+2
       GPIO.output(11, True)
       p.ChangeDutyCycle(duty1)
       time.sleep(0.5)
       GPIO.output(11, False)
       p.ChangeDutyCycle(0)
       GPIO.output(11, True)
       p.ChangeDutyCycle(duty2)
       time.sleep(0.5)
       GPIO.output(11, False)
       p.ChangeDutyCycle(0)

def close():
    p.stop()

#GPIO.cleanup()
