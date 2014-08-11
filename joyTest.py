from tegrabot.joystick import Joystick
from tegrabot.driver import Driver
from tegrabot.arduino import Arduino
from tegrabot.shooter import Shooter

joystick = Joystick()
driver = Driver()
motorPorts=[5, 6]
shooterPorts=[2,3]
magPorts=[9, 10]
arduino = Arduino(motorPorts, shooterPorts, magPorts)
ser = serial.Serial('/dev/ttyAMC0')
while(True):
        joystick.connect()
        while (joystick.isConnected()):
                joystick.setData()

                joy1= joystick.getJoyOneYAxis()
                joy2= joystick.getJoyTwoYAxis()
                joyButton= joystick.getButtonVal()
                #data=[]
                tank = driver.tankDrive(joy1, joy2)
                data=[tank[0], tank[1], 0, 0, 0, 0]
                arduino.sendData(data);
                
