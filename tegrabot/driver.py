import serial
import time
import math

class Driver:
    #ser = serial.Serial("/dev/ttyACM0", 9600)
    #motorPorts=[]
    #motor setup 2
    def __init__(self):
                 
    def driveMotor(self, speed):
        motorSpeed =90
        if(speed > 0):
            motorSpeed = speed*90
            motorSpeed+=90
        else:
            motorSpeed = speed*90
            motorSpeed +=90
        
        return motorSpeed
    def tankDrive(self, leftJoy, rightJoy):
        rightSpeed = 90
        leftSpeed = 90
        if(leftJoy > 0.05):
            leftSpeed = leftSpeed*90
            leftSpeed+=90
        elif(leftJoy<-0.05):
            leftSpeed = leftSpeed*90
            leftSpeed +=90
        if(rightJoy > 0.05):
            rightSpeed = rightSpeed*90
            rightSpeed+=90
        elif(rightJoy<-0.05):
            rightSpeed = rightSpeed*90
            rightSpeed +=90
        
        speeds = [rightSpeed,leftSpeed]
        return speeds
    
    
