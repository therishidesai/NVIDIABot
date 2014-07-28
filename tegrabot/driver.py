import serial
import time
import math

class Driver:
    ser = serial.Serial("/dev/ttyACM0", 9600)
    #motorPorts=[]
    #sets up the motor ports
    def __init__(motorPort1, motorPort2, motorPort3, motorPort4):
        motorPorts = [motorPort1, motorPort2, motorPort3, motorPort4]
        for i in range(motorPorts):
            if(i==0):
                ser.write(motorPorts[i])
            elif(ser.readline()=="Y"):
                ser.write(motorPorts[i])
            else:
                print "An Error Occurred"
                break
    
                
    def driveMotor(motorPort, speed):
        ser.write('M')
        if(ser.readline()=='Y'):
            ser.write(chr(motorPort))
        else:
            return 0
            print "Error"
        motorSpeed =90
        if(speed > 0):
            motorSpeed = speed*90
            motorSpeed+=90
        else:
            motorSpeed = speed*90
            motorSpeed +=90
        ser.write(chr(int(motorSpeed))
    
    def tankDrive(leftSide, rightSide, leftSpeed, rightSpeed):
        ser.write('T')
        motorSpeed = 90
        if(leftSpeed > 0.05):
            motorSpeed = leftSpeed*90
            motorSpeed+=90
        elif(leftSpeed<-0.05):
            motorSpeed = leftSpeed*90
            motorSpeed +=90
        if(rightSpeed > 0.05):
            motorSpeed = rightSpeed*90
            motorSpeed+=90
        elif(rightSpeed<-0.05):
            motorSpeed = rightSpeed*90
            motorSpeed +=90
        if(ser.readline()=='Y'):
            ser.write(chr(int(motorSpeed)))
        else:
            print "Error"
    
    
