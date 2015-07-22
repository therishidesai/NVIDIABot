'''
Copyright (c) 2014, Rishi Desai
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
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
          
  
        
