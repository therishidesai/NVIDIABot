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
import Tkinter
import tkMessageBox
import socket
import pickle
import pygame

top = Tkinter.Tk()
joyFrame = Tkinter.Frame(top)
noJoyFrame = Tkinter.Frame(top)
port = 8081
host = "10.99.99.2"
#host = "192.168.1.83"
pygame.init()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#j =0;
s.bind(("", 0))
started = False
def startSession():
    global started 
    started= True
    s.sendto(pickle.dumps(started), (host, port))
    # change wait to 2 after done testing
    top.after(200, sendJoystickVal)
def endSession():
    global started 
    started= False
    #s.bind(("", 0))
    s.sendto(pickle.dumps(started), (host, port))
    #top.destroy()
def closeProgram():
    s.close()
    top.destroy()
sessionStart = Tkinter.Button(top, text ="Start Session", command = startSession)
sessionEnd = Tkinter.Button(top, text="End Session", command=endSession)
programClose= Tkinter.Button(top, text="Close Program", command=closeProgram)
def isJoystick():
    return pygame.joystick.get_count()>0

def whileJoyCon():
    if(isJoystick()):
        sessionStart.config(state="normal")
        sessionStart.pack()
        sessionEnd.config(state="normal")
        sessionEnd.pack()
        programClose.config(state="normal")
        programClose.pack()
        howTo = Tkinter.Text(top)
        howTo.insert(Tkinter.INSERT, "Press Start on the Joystick or end session to stop the program")
        howTo.pack()
    else:
        print isJoystick()
        sessionStart.config(state="disable")
        sessionStart.pack()
        sessionEnd.config(state="disable")
        sessionEnd.pack()
        programClose.config(state="normal")
        programClose.pack()
        noJoy = Tkinter.Text(top)
        noJoy.insert(Tkinter.INSERT, "No Joystick Connected. Please connect a Joystick and Restart the program")
        noJoy.pack()        
def sendJoystickVal():
    #print isJoy
    #if(isJoystick):
        pygame.event.pump()
        j = pygame.joystick.Joystick(0)
        j.init()
        xAxis = j.get_axis(1)
        yAxis=j.get_axis(3)
        i=1
        button =-1;
        
        for i in range(j.get_numbuttons()):
            if(j.get_button(i)==True):
                button = i
                break
        
        data = [started, xAxis, -yAxis, button]
        s.sendto(pickle.dumps(data), (host, port))
        print data
        #change wait to 2 after done testing
        top.after(200, sendJoystickVal)
whileJoyCon()
#rint started
#f(started):
#top.after(2000, sendJoystickVal)
top.mainloop()
