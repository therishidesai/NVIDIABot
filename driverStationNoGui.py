#import Tkinter
#import tkMessageBox
import socket
import pickle
import pygame
import sys
import time
#top = Tkinter.Tk()
#joyFrame = Tkinter.Frame(top)
#noJoyFrame = Tkinter.Frame(top)
port = 8081
host999 = "10.99.99.7"
host = "192.168.1.81"
pygame.init()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#j =0;
s.bind(("", 0))
started = False

def startSession():
    sarted = True
def endSession():
    started = False
    s.close()
def isJoystick():
    return pygame.joystick.get_count()>0      
def sendJoystickVal():
    j = pygame.joystick.Joystick(0)
    j.init()
    while(isJoystick()):
        #pygame.joystick.init()
        pygame.event.pump()
        xAxis = j.get_axis(1)
        yAxis=j.get_axis(3)
        i=1
        button =0;
        
        for i in range(j.get_numbuttons()):
            if(j.get_button(i)==True):
                button = i
                break
                
        data = [xAxis, yAxis, button]
        #s.sendto(pickle.dumps(data), (host, port))
        print data
        time.sleep(5)

while(1): 
    if(isJoystick()==True):
        answer = input("Welcome to the Jetson Tegra K1 Driver Station. To Enable the robot type 1. To Disable the robot press select on the joystick or disconnect the joystick. Press 2 to exit the program.")
        if(answer==1):
            if(started == False):
                startSession()
            sendJoystickVal()
        else:
            endSession()
            sys.exit(0)
    else:
        print "Please connect a Joystick"
        sys.exit(0)
          
  
        
