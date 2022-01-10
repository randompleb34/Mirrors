from adafruit_servokit import ServoKit
import time

kit1 = ServoKit(channels = 16, address = 0x40)
kit2 = ServoKit(channels = 16, address = 0x41)
kit3 = ServoKit(channels = 16, address = 0x42)
kit4 = ServoKit(channels = 16, address = 0x43)
kit5 = ServoKit(channels = 16, address = 0x44)
kit6 = ServoKit(channels = 16, address = 0x45)
kit7 = ServoKit(channels = 16, address = 0x46)
kit8 = ServoKit(channels = 16, address = 0x47)
kit9 = ServoKit(channels = 16, address = 0x48)
kit10 = ServoKit(channels = 16, address = 0x49)
    
def manageServos(angle):
    for x in range(10):
        kit1.servo[x].angle = angle
        kit2.servo[x].angle = angle
        kit3.servo[x].angle = angle
        kit4.servo[x].angle = angle
        kit5.servo[x].angle = angle
        kit6.servo[x].angle = angle
        kit7.servo[x].angle = angle
        kit8.servo[x].angle = angle
        kit9.servo[x].angle = angle
        kit10.servo[x].angle = angle

while True:
    manageServos(15)
    time.sleep(1)
    manageServos(90)
    time.sleep(1)
    manageServos(165)
    time.sleep(1)
    manageServos(90)
    time.sleep(1)