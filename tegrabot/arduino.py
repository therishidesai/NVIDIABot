import serial

class Arduino:
    
    ser = serial.Serial('/dev/ttyACM0')
    
    def __init__(motorPorts, shooterPorts, magPorts):
        ports=[]
        for x in range motorPorts:
            ports.append(x)
        
        for x in range shooterPorts:
            ports.append(x)
        
        for x in range magPorts:
            ports.append(x)
            
        ser.write(ports)
    
    def sendData(data):
        ser.write(data)
