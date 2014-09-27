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
from tegrabot.joystick import Joystick
from tegrabot.driver import Driver
from tegrabot.arduino import Arduino
from tegrabot.shooter import Shooter

joystick = Joystick()
driver = Driver()
shooter = Shooter()
motorPorts=[9, 12]
shooterPorts=[2,3]
magPorts=[11, 10]
arduino = Arduino()
#ser = serial.Serial('/dev/ttyAMC0')

while(True):
  joystick.connect()
    while (joystick.isConnected()):
                joystick.setData()
		            #print joystick.isConnected()
                joy1= joystick.getJoyOneYAxis()
                joy2= joystick.getJoyTwoYAxis()
                joyButton= joystick.getButtonVal()
                #data=[]
                tank = driver.tankDrive(joy1, joy2)
            	  if(joyButton==0):
            			shootPos=1
            		elif(joyButton==1):
            			shootPos=2
            		elif(joyButton==2):
            			shootPos=3
            		else:
            			shootPos=0             	
            		data=[90, 90, shooter.shootLeft(shootPos),0, 0, 0]
                #print data
            		arduino.sendData(data)
  data=[90,90,0,0,0,0]
  arduino.sendData(data)                           
