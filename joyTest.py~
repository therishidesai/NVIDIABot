from tegrabot.joystick import Joystick

joystick = Joystick()

while(True):
        joystick.connect()
        while (joystick.isConnected()):
                joystick.setData()

                print joystick.getJoyOneYAxis()
                print joystick.getJoyTwoYAxis()
                print joystick.getButtonVal()
