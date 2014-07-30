import serial
import time
import math

class Shooter:
    ser = serial.Serial("/dev/ttyACM0", 9600)
    
    def __init__(shooterPort1, shooterPort2, magPort1, magPort2):
        ser.write("S");
        shooterMagPorts =[shooterPort1, shooterPort2, magPort1, magPort2] 
        if(ser.readline()="Y"):
            for i in range(motorPorts):
                if(i==0):
                    ser.write(shooterMagPorts[i])
                elif(ser.readline()=="Y"):
                    ser.write(shotterMagPorts[i])
                else:
                    print "An Error Occurred"
                    break
                    

    def shootLeft(leftShooterPort, distance):
        distanceWaits = [5, 10, 15]
        ser.write("Sh")
        if(ser.readline()=="Y"):
            ser.write(leftShooterPort)
            ser.write(distanceWaits[distance-1]
        else:
            print "An Error Occurred"

     def shootRight(rightShooterPort, distance):
        distanceWaits = [5, 10, 15]
        ser.write("Sh")
        if(ser.readline()=="Y"):
            ser.write(rightShooterPort)
            ser.write(distanceWaits[distance-1]
        else:
            print "An Error Occurred"
    
    def reloadLeft(leftReloadPort):
        #distanceWaits = [5, 10, 15]
        ser.write("R")
        if(ser.readline()=="Y"):
            ser.write(leftReloadPort)
            #ser.write(distanceWaits[distance-1]
        else:
            print "An Error Occurred"
    
     def reloadRight(rightReloadPort):
        #distanceWaits = [5, 10, 15]
        ser.write("R")
        if(ser.readline()=="Y"):
            ser.write(rightReloadPort)
            #ser.write(distanceWaits[distance-1]
        else:
            print "An Error Occurred"
