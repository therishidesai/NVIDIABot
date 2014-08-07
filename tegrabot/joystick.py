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
            self.s.bind("", port)
        else:
            self.s = s
    def connect(self):
        data, addr = self.s.recvfrom(1024)
        sessionStarted = pickle.load(data)
    def isConnected():
        return sessionStarted
    def setData(self):
        data, addr = self.s.recvfrom(1024)
        joyData = pickle.load(data)

    def getJoyOneYAxis():
        #data, addr = s.recvfrom(1024)
        return joyData[1]
    def getJoyTwoYAxis():
        #data, addr = s.recvfrom(1024)
        return joyData[2] 
    def getButtonVal():
        #data, addr = s.recvfrom(1024)
        return joyData[3]
    
