import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit


'''GPIO.setmode(GPIO.BCM)
GPIO.setup(11,GPIO.OUT)
servo1=GPIO.PWM(11,50)
servo1.start(2)'''

h = ServoKit(channels=16)

#servo1.ChangeDutyCycle(12)
#kit.servo[0].angle 

init = [0,90,20,0,180,160,170,180,60,0,0,150]
limitLo = [0,0,20,0,0,40,0,0,60,0,0,30]
limitHi = [35,180,180,180,180,160,170,180,180,180,180,150]

cur = init

def changeDeg(pin1,new1,pin2,new2,pin3,new3):
    now1 = cur[pin1]
    now2 = cur[pin2]
    now3 = cur[pin3]
    len = max(max(abs(now1-new1),abs(now2-new2)),abs(now3-new3))
    for deg in range(0,len,5):
        if now1<new1:
            now1=now1+5
        elif now1>new1:
            now1=now1-5
        if now2<new2:
            now2=now2+5
        elif now2>new2:
            now2=now2-5
        if now3<new3:
            now3=now3+2
        elif now3>new3:
            now3=now3-2
        h.servo[pin1].angle=now1
        h.servo[pin2].angle=now2
        h.servo[pin3].angle=now3
        time.sleep(0.1)
    cur[pin1]=now1
    cur[pin2]=now2
    cur[pin3]=now3
for i in range(0,12):
    h.servo[i].angle=init[i]
for i in range(0,26,5):
    h.servo[0].angle=i
    time.sleep(0.05)
while True:
    changeDeg(3,90,4,180,1,60)
    changeDeg(3,0,4,90,1,120)
