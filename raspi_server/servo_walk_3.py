import RPi.GPIO as GPIO
import time

def setup():
    global p1, p2, p3, p4, p5, p6, p7, p8
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT) #32
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(29, GPIO.OUT) #36
    GPIO.setup(31, GPIO.OUT)

    p1=GPIO.PWM(11, 50)
    p2=GPIO.PWM(13, 50)
    p3=GPIO.PWM(15, 50)
    p4=GPIO.PWM(16, 50)
    p5=GPIO.PWM(18, 50)
    p6=GPIO.PWM(22, 50)
    p7=GPIO.PWM(29, 50)
    p8=GPIO.PWM(31, 50)

    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0)
    p5.start(0)
    p6.start(0)
    p7.start(0)
    p8.start(0)

def setangle1(angle1):
    duty1=(angle1/18)+2
    GPIO.output(11, True)
    p1.ChangeDutyCycle(duty1)
    time.sleep(0.5)
    GPIO.output(11, False)
    p1.ChangeDutyCycle(0)
    return 1

def setangle2(angle2):
    duty2=(angle2/18)+2
    GPIO.output(13, True)
    p2.ChangeDutyCycle(duty2)
    time.sleep(0.5)
    GPIO.output(13, False)
    p2.ChangeDutyCycle(0)
    return 1

def setangle3(angle3):
    duty3=(angle3/18)+2
    GPIO.output(15, True)
    p3.ChangeDutyCycle(duty3)
    time.sleep(0.5)
    GPIO.output(15, False)
    p3.ChangeDutyCycle(0)
    return 1

def setangle4(angle4):
    duty4=(angle4/18)+2
    GPIO.output(16, True)
    p4.ChangeDutyCycle(duty4)
    time.sleep(0.5)
    GPIO.output(16, False)
    p4.ChangeDutyCycle(0)
    return 1

def setangle5(angle5):
    duty5=(angle5/18)+2
    GPIO.output(18, True)
    p5.ChangeDutyCycle(duty5)
    time.sleep(0.5)
    GPIO.output(18, False)
    p5.ChangeDutyCycle(0)
    return 1

def setangle6(angle6):
    duty6=(angle6/18)+2
    GPIO.output(22, True)
    p6.ChangeDutyCycle(duty6)
    time.sleep(0.5)
    GPIO.output(22, False)
    p6.ChangeDutyCycle(0)
    return 1

def setangle7(angle7):
    duty7=(angle7/18)+2
    GPIO.output(29, True)
    p7.ChangeDutyCycle(duty7)
    time.sleep(0.5)
    GPIO.output(29, False)
    p7.ChangeDutyCycle(0)
    return 1

def setangle8(angle8):
    duty8=(angle8/18)+2
    GPIO.output(31, True)
    p8.ChangeDutyCycle(duty8)
    time.sleep(0.5)
    GPIO.output(31, False)
    p8.ChangeDutyCycle(0)
    return 1

def initiate():
    GPIO.output(11, True)
    p1.ChangeDutyCycle(duty1_45)
    time.sleep(0.5)
    GPIO.output(15, True)
    p3.ChangeDutyCycle(duty2_135)
    time.sleep(0.5)
    GPIO.output(18, True)
    p5.ChangeDutyCycle(duty3_45)
    time.sleep(0.5)

def walk1():
    global duty1_0, duty1_45, duty1_90, duty1_135, duty1_180, duty1_75 
    duty1_0=(0/18)+2
    duty1_45=(45/18)+2
    duty1_75=(75/18)+2
    duty1_90=(90/18)+2
    duty1_135=(135/18)+2
    duty1_180=(180/18)+2
    GPIO.output(13, True)
    p2.ChangeDutyCycle(duty1_135)
    time.sleep(0.1)
    GPIO.output(11, True)
    p1.ChangeDutyCycle(duty1_45)
    time.sleep(0.25)
    GPIO.output(13, False)
    p2.ChangeDutyCycle(0)
    GPIO.output(11, False)
    p1.ChangeDutyCycle(0)
    GPIO.output(13, True)
    p2.ChangeDutyCycle(duty1_90)
    time.sleep(0.1)
    #GPIO.output(11, True)
    #p1.ChangeDutyCycle(duty1_90)
    #time.sleep(0.5)
    #GPIO.output(13, False)
    #GPIO.output(11, False)
    #p2.ChangeDutyCycle(0)
    #p1.ChangeDutyCycle(0)
    return 1

def walk2():
    global duty2_0, duty2_45, duty2_90, duty2_135, duty2_180
    duty2_0=(0/18)+2
    duty2_45=(45/18)+2
    duty2_90=(90/18)+2
    duty2_135=(135/18)+2
    duty2_180=(180/18)+2
    GPIO.output(16, True)
    p4.ChangeDutyCycle(duty2_45)
    time.sleep(0.1)
    GPIO.output(15, True)
    p3.ChangeDutyCycle(duty2_135)
    time.sleep(0.25)
    GPIO.output(16, False)
    p4.ChangeDutyCycle(0)
    GPIO.output(15, False)
    p3.ChangeDutyCycle(0)
    GPIO.output(16, True)
    p4.ChangeDutyCycle(duty2_90)
    time.sleep(0.1)
    #GPIO.output(15, True)
    #p3.ChangeDutyCycle(duty2_90)
    #time.sleep(0.5)
    #GPIO.output(16, False)
    #GPIO.output(15, False)
    #p4.ChangeDutyCycle(0)
    #p3.ChangeDutyCycle(0)
    return 1

def walk3():
    global duty3_0, duty3_45, duty3_90, duty3_135, duty3_180
    duty3_0=(0/18)+2
    duty3_45=(45/18)+2
    duty3_90=(90/18)+2
    duty3_135=(135/18)+2
    duty3_180=(180/18)+2
    GPIO.output(22, True)
    p6.ChangeDutyCycle(duty3_45)
    time.sleep(0.1)
    GPIO.output(18, True)
    p5.ChangeDutyCycle(duty3_135)
    time.sleep(0.25)
    GPIO.output(22, False)
    p6.ChangeDutyCycle(0)
    GPIO.output(18, False)
    p5.ChangeDutyCycle(0)
    GPIO.output(22, True)
    p6.ChangeDutyCycle(duty3_90)
    time.sleep(0.1)
    #GPIO.output(18, True)
    #p5.ChangeDutyCycle(duty3_90)
    #time.sleep(0.5)
    #GPIO.output(22, False)
    #GPIO.output(18, False)
    #p6.ChangeDutyCycle(0)
    #p5.ChangeDutyCycle(0)
    return 1

def walk4():
    global duty4_0, duty4_45, duty4_90, duty4_135, duty4_180, duty4_60
    duty4_0=(0/18)+2
    duty4_45=(45/18)+2
    duty4_60=(60/18)+2
    duty4_90=(90/18)+2
    duty4_135=(135/18)+2
    duty4_180=(180/18)+2
    GPIO.output(31, True)
    p8.ChangeDutyCycle(duty4_135)
    time.sleep(0.1)
    GPIO.output(29, True)
    p7.ChangeDutyCycle(duty4_60)
    time.sleep(0.25)
    GPIO.output(31, False)
    p8.ChangeDutyCycle(0)
    GPIO.output(29, False)
    p7.ChangeDutyCycle(0)
    GPIO.output(31, True)
    p8.ChangeDutyCycle(duty4_90)
    time.sleep(0.1)
    #GPIO.output(29, True)
    #p7.ChangeDutyCycle(duty4_90)
    #time.sleep(0.5)
    #GPIO.output(31, False)
    #GPIO.output(29, False)
    #p8.ChangeDutyCycle(0)
    #p7.ChangeDutyCycle(0)
    return 1

def walk_reset():
    global duty_45, duty_90, duty_135
    duty_45=(45/18)+2
    duty_135=(135/18)+2
    duty_90=(90/18)+2
    GPIO.output(29, True)
    p7.ChangeDutyCycle(duty_90)
    time.sleep(0.25)
    #GPIO.output(31, True)
    #p8.ChangeDutyCycle(duty)
    GPIO.output(18, True)
    p5.ChangeDutyCycle(duty_90)
    time.sleep(0.25)
    #GPIO.output(22, True)
    #p6.ChangeDutyCycle(duty)
    GPIO.output(15, True)
    p3.ChangeDutyCycle(duty_90)
    time.sleep(0.25)
    #GPIO.output(16, True)
    #p4.ChangeDutyCycle(duty)
    GPIO.output(11, True)
    p1.ChangeDutyCycle(duty_90)
    time.sleep(0.25)
    #GPIO.output(13, True)
    #p2.ChangeDutyCycle(duty)
    GPIO.output(31, False)
    GPIO.output(29, False)
    GPIO.output(22, False)
    GPIO.output(18, False)
    GPIO.output(16, False)
    GPIO.output(15, False)
    GPIO.output(13, False)
    GPIO.output(11, False)
    time.sleep(0.5)
    p8.ChangeDutyCycle(0)
    p7.ChangeDutyCycle(0)
    p6.ChangeDutyCycle(0)
    p5.ChangeDutyCycle(0)
    p4.ChangeDutyCycle(0)
    p3.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)
    p1.ChangeDutyCycle(0)
    time.sleep(0.5)
    
def initialise_90():
    global duty
    duty=(90/18)+2
    GPIO.output(36, True)
    p7.ChangeDutyCycle(duty)
    time.sleep(0.25)
    GPIO.output(31, True)
    p8.ChangeDutyCycle(duty)
    GPIO.output(32, True)
    p5.ChangeDutyCycle(duty)
    time.sleep(0.25)
    GPIO.output(22, True)
    p6.ChangeDutyCycle(duty)
    GPIO.output(15, True)
    p3.ChangeDutyCycle(duty)
    time.sleep(0.25)
    GPIO.output(16, True)
    p4.ChangeDutyCycle(duty)
    GPIO.output(11, True)
    p1.ChangeDutyCycle(duty)
    time.sleep(0.25)
    GPIO.output(13, True)
    p2.ChangeDutyCycle(duty)
    GPIO.output(31, False)
    GPIO.output(36, False)
    GPIO.output(22, False)
    GPIO.output(32, False)
    GPIO.output(16, False)
    GPIO.output(15, False)
    GPIO.output(13, False)
    GPIO.output(11, False)
    time.sleep(0.5)
    p8.ChangeDutyCycle(0)
    p7.ChangeDutyCycle(0)
    p6.ChangeDutyCycle(0)
    p5.ChangeDutyCycle(0)
    p4.ChangeDutyCycle(0)
    p3.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)
    p1.ChangeDutyCycle(0)
    time.sleep(0.5)
    
def left():
    global dutyl_0, dutyl_45, dutyl_90, dutyl_135, dutyl_180, cntl
    cntl=0
    while(cntl<5):
      dutyl_0=(0/18)+2
      dutyl_45=(45/18)+2
      dutyl_90=(90/18)+2
      dutyl_135=(135/18)+2
      dutyl_180=(180/18)+2
      GPIO.output(13, True)
      p2.ChangeDutyCycle(dutyl_135)
      time.sleep(0.25)
      GPIO.output(11, True)
      p1.ChangeDutyCycle(dutyl_45)
      time.sleep(0.25)
      GPIO.output(31, True)
      p8.ChangeDutyCycle(dutyl_135)
      time.sleep(0.25)
      GPIO.output(29, True)
      p7.ChangeDutyCycle(dutyl_45)
      time.sleep(0.25)
      GPIO.output(13, True)
      p2.ChangeDutyCycle(dutyl_90)
      time.sleep(0.25)
      GPIO.output(11, True)
      p1.ChangeDutyCycle(dutyl_90)
      time.sleep(0.25)
      GPIO.output(31, True)
      p8.ChangeDutyCycle(dutyl_90)
      time.sleep(0.25)
      GPIO.output(29, True)
      p7.ChangeDutyCycle(dutyl_90)
      time.sleep(0.25)
      GPIO.output(13, False)
      GPIO.output(11, False)
      GPIO.output(31, False)
      GPIO.output(29, False)
      p2.ChangeDutyCycle(0)
      p1.ChangeDutyCycle(0)
      p8.ChangeDutyCycle(0)
      p7.ChangeDutyCycle(0)
      time.sleep(0.5)
      cntl+=1
    
def right():
    global dutyr_0, dutyr_45, dutyr_90, dutyr_135, dutyr_180, cntr
    cntr=0
    while(cntr<5):
      dutyr_0=(0/18)+2
      dutyr_45=(45/18)+2
      dutyr_90=(90/18)+2
      dutyr_135=(135/18)+2
      dutyr_180=(180/18)+2
      GPIO.output(16, True)
      p4.ChangeDutyCycle(dutyr_45)
      time.sleep(0.25)
      GPIO.output(15, True)
      p3.ChangeDutyCycle(dutyr_135)
      time.sleep(0.25)
      GPIO.output(22, True)
      p6.ChangeDutyCycle(dutyr_45)
      time.sleep(0.25)
      GPIO.output(18, True)
      p5.ChangeDutyCycle(dutyr_135)
      time.sleep(0.25)
      GPIO.output(15, True)
      p4.ChangeDutyCycle(dutyr_90)
      time.sleep(0.25)
      GPIO.output(15, True)
      p3.ChangeDutyCycle(dutyr_90)
      time.sleep(0.25)
      GPIO.output(22, True)
      p6.ChangeDutyCycle(dutyr_90)
      time.sleep(0.25)
      GPIO.output(18, True)
      p5.ChangeDutyCycle(dutyr_90)
      time.sleep(0.25)
      GPIO.output(16, False)
      GPIO.output(15, False)
      GPIO.output(22, False)
      GPIO.output(18, False)
      p4.ChangeDutyCycle(0)
      p3.ChangeDutyCycle(0)
      p6.ChangeDutyCycle(0)
      p5.ChangeDutyCycle(0)
      time.sleep(0.5)
      cntr+=1
    
def walking():
  global cnt  
  cnt=0
  while(cnt<5):
     walk1()
     walk2()
     walk3()
     walk4()
     walk_reset()
     cnt+=1

#p1a=input('Enter first angle to rotate the servo 1a accordingly: ')
#p1b=setangle1(p1a)
#p2a=input('Enter first angle to rotate the servo 1b accordingly: ')
#p2b=setangle2(p2a)
#p3a=input('Enter first angle to rotate the servo 2a accordingly: ')
#p3b=setangle3(p3a)
#p4a=input('Enter first angle to rotate the servo 2b accordingly: ')
#p4b=setangle4(p4a)
#p5a=input('Enter first angle to rotate the servo 3a accordingly: ')
#p5b=setangle5(p5a)
#p6a=input('Enter first angle to rotate the servo 3b accordingly: ')
#p6b=setangle6(p6a)
#p7a=input('Enter first angle to rotate the servo 4a accordingly: ')
#p7b=setangle7(p7a)
#p8a=input('Enter first angle to rotate the servo 4b accordingly: ')
#p8b=setangle8(p8a)
   
def close():
   p1.stop()
   p2.stop()
   p3.stop()
   p4.stop()
   p5.stop()
   p6.stop()
   p7.stop()
   p8.stop()


#GPIO.cleanup()



