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
import time
import math
import pickle
class Joystick:
    
    sessionStarted = False
    port = 8081
    joyData=[]
    #s = socket.socket(socket.AF_INET, socket.Sock_DGRAM)
    def __init__(self, s=None):
        if s is None:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.bind(("", Joystick.port))
        else:
            self.s = s
    def connect(self):
        data, addr = self.s.recvfrom(1024)
        Joystick.sessionStarted = pickle.loads(data)
    def isConnected(self):
        return Joystick.sessionStarted
    def setData(self):
        data, addr = self.s.recvfrom(1024)
        Joystick.joyData = pickle.loads(data)

    def getJoyOneYAxis(self):
        #data, addr = s.recvfrom(1024)
	#print Joystick.joyData[0]
	return Joystick.joyData[0]
    def getJoyTwoYAxis(self):
        #data, addr = s.recvfrom(1024)
        return Joystick.joyData[1] 
    def getButtonVal(self):
        #data, addr = s.recvfrom(1024)
        return Joystick.joyData[2]
    
