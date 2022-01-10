import io
import time
import picamera
import os
from PIL import Image
import sys
import cv2
import numpy as np
from adafruit_servokit import ServoKit
kits = [ServoKit(channels = 16, address = 0x40),
        ServoKit(channels = 16, address = 0x41),
        ServoKit(channels = 16, address = 0x42),
        ServoKit(channels = 16, address = 0x43),
        ServoKit(channels = 16, address = 0x44),
        ServoKit(channels = 16, address = 0x45),
        ServoKit(channels = 16, address = 0x46),
        ServoKit(channels = 16, address = 0x47),
        ServoKit(channels = 16, address = 0x48),
        ServoKit(channels = 16, address = 0x49)]
# kit1 = ServoKit(channels = 16, address = 0x40)
# kit3 = ServoKit(channels = 16, address = 0x42)
#pwm = PWM(0x40)

counter = 0
size = 50, 50
gridsize = 10
res = size[0]/gridsize

servoData = np.zeros((10,10))

def manageServos():
    for kitIdx in range(len(kits)):
        for x in range(10):
            kits[kitIdx].servo[x].angle = servoData[kitIdx][x]
#             kit2.servo[x].angle = servoData[1][x]
#         kit4.servo[x].angle = 
#         kit5.servo[x].angle = angle
#         kit6.servo[x].angle = angle
#         kit7.servo[x].angle = angle
#         kit8.servo[x].angle = angle

def gray2pixelate(gry):
    pixdata = gry.load()
    for x in range(gridsize):
        for y in range(gridsize):
            r = 0
            b = 0
            g = 0
            
            avg = 0
            for x1 in range(int(gry.size[0]/gridsize)):
                for y1 in range(int(gry.size[1]/gridsize)):
                    posx = res*x + x1
                    posy = res*y + y1
                    r = r + pixdata[posx, posy][0]
                    b = b + pixdata[posx, posy][1]
                    g = g + pixdata[posx, posy][2]
            r = int(r/(size[0]/gridsize*size[0]/gridsize))
            b = int(b/(size[0]/gridsize*size[0]/gridsize))
            g = int(g/(size[0]/gridsize*size[0]/gridsize))
            avg = int((r+b+g)/3)
            if(int(avg/255 * 150) + 15 > 95):
                servoData[x][y] = 15
            else:
                servoData[x][y] = 165
#            elif (int(avg/255 * 150) + 15 < 85):
#                servoData[x][y] = 15
#            else:
#                servoData[x][y] = 90
#             servoData[x][y] = int(avg/255 * 150) + 15
    manageServos()   
    return gry

def rgb2gray(rgb):
    pixdata = rgb.load()
    for x in range(rgb.size[0]):
        for y in range(rgb.size[1]):
            avg = int((pixdata[x, y][0] + pixdata[x, y][1] + pixdata[x, y][2])/3)
            pixdata[x, y] = (avg, avg, avg)
    return rgb

def process(frame):
    stream = io.BytesIO(frame.getvalue())
    img = Image.open(stream).convert("RGB")
    gray = rgb2gray(img)
    pixels = gray2pixelate(gray)
#     for i in servoData:
#         for j in i:
#             print(j, end=" ")
#         print()
    temp = np.array(pixels)
    temp = temp[:, :, ::-1].copy() 
#     print(type(temp))
    cv2.imshow("output", temp)
#     cv2.imshow("pair", frame)
#     key = cv2.waitKey(1) & 0xFF
    pixels = img.save('/home/pi/Desktop/contCapture/pixels.jpg')
    #print("saved")
    #image = Image.open(stream).convert("RGBA")
    
with picamera.PiCamera() as camera:
    # Let the camera warm up for 2 seconds.
    camera.resolution = (size)
    time.sleep(2)
    #camera.start_preview()
    stream = io.BytesIO()
    for frame in camera.capture_continuous(stream, format="jpeg", resize = size):
#    for foo in camera.capture_continuous(stream, format="jpeg"):
        counter+=1
        #print("Captured " + str(counter) + " frame(s)")
        process(frame)
        stream.truncate(0)
        stream.seek(0)
        #print(counter)
#         if counter == 10:
#              break
    print("done")
    #camera.stop_preview()
    camera.close()
    
