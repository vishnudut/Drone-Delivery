import pigpio
import time
import os
os.system("sudo pigpiod")
time.sleep(1)

mot1 = 17
mot2 = 27

pi = pigpiod.pi()

pi.set_servo_pulsewidth(mot1, 0)
pi.set_servo_pulsewidth(mot2, 0)

maxVal = 2000
minVal = 500

print("Press 1 to start motor 1 and 2 to start motor 2")

while(True):
    speed = 1500
    time.sleep(1)
    inp = raw_input()
    if inp == "1":
        pi.set_servo_pulsewidth(mot1, speed)
    if inp == "2":
        pi.set_servo_pulsewidth(mot2, speed)
    if inp == "":
        pi.set_servo_pulsewidth(mot1, 0)
        pi.set_servo_pulsewidth(mot2, 0)
        pi.stop()