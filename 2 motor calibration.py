import os     
import time    
os.system ("sudo pigpiod") 
time.sleep(1) 
import pigpio 

ESC1 = 2
ESC2 = 4

pi1 = pigpio.pi()
pi2 = pigpio.pi()
pi1.set_servo_pulsewidth(ESC1, 0)
pi2.set_servo_pulsewidth(ESC2, 0)

maxVal = 2000
minVal = 500

print("Enter 'arm' to start the motors")

def control(): 
    time.sleep(1)
    speed = 1500    
    print("a -- decrease speed && d -- increase speed && q -- decrease a lot of speed && e -- for lot of speed")
    while True:
        pi1.set_servo_pulsewidth(ESC1, speed)
        pi2.set_servo_pulsewidth(ESC2, speed)

        inp = raw_input()
        
        if inp == "q":
            speed -= 100    
            print "speed = %d" % speed
        elif inp == "e":    
            speed += 100    
            print "speed = %d" % speed
        elif inp == "d":
            speed += 10      
            print "speed = %d" % speed
        elif inp == "a":
            speed -= 10     
            print "speed = %d" % speed
        elif inp == "stop":
            stop()          
            break
        elif inp == "arm":
            arm()
            break	
        else:
            print "Press a,q,d or e"

def arm():
    print("Connect the battery and press Enter")
    inp = raw_input()    
    if inp == '':
        pi1.set_servo_pulsewidth(ESC1, 0)
        pi2.set_servo_pulsewidth(ESC1, 0)
        time.sleep(1)
        pi1.set_servo_pulsewidth(ESC1, maxVal)
        pi2.set_servo_pulsewidth(ESC1, maxVal)
        time.sleep(1)
        pi1.set_servo_pulsewidth(ESC1, minVal)
        pi2.set_servo_pulsewidth(ESC1, minVal)
        time.sleep(1)
        control()

def stop(): 
    pi1.set_servo_pulsewidth(ESC1, 0)
    pi2.set_servo_pulsewidth(ESC2, 0)
    pi1.stop()
    pi2.stop()

inp = raw_input()
if inp == "arm":
    arm()
elif inp == "control":
    control()
elif inp == "stop":
    stop()
else :
    print("Restart the program")
