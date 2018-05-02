import os     
import time    
os.system ("sudo pigpiod") 
time.sleep(1) 
import pigpio 

ESC1 = 6
ESC2 = 5

pi = pigpio.pi()
pi.set_servo_pulsewidth(ESC1, 0)

maxVal = 2000
minVal = 500

print("Enter 'arm' to start the motors")

def control(): 
    time.sleep(1)
    speed = 1500    
    print("a -- decrease speed && d -- increase speed && q -- decrease a lot of speed && e -- for lot of speed")
    while True:
        pi.set_servo_pulsewidth(ESC1, speed)

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
        pi.set_servo_pulsewidth(ESC1, 0)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC1, maxVal)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC1, minVal)
        time.sleep(1)
        control()

def stop(): 
    pi.set_servo_pulsewidth(ESC1, 0)
    pi.stop()

inp = raw_input()
if inp == "arm":
    arm()
elif inp == "control":
    control()
elif inp == "stop":
    stop()
else :
    print("Restart the program")
