import socket
import time
import math
import pickle
class Joystick:
    
    sessionStarted = False
    port = 8081
    s = socket.socket(socket.AF_INET, socket.Sock_DGRAM)
    def __init__():
        s.bind("", port)
        data, addr = s.recvfrom(1024)
        sessionStarted = pickle.load(data)
    def getJoyOneYAxis():
        data, addr = s.recvfrom(1024)
        return data[1]
    def getJoyTwoYAxis():
        data, addr = s.recvfrom(1024)
        return data[2] 
    def getButtonVal():
        data, addr = s.recvfrom(1024)
        return data[3]
    
