from tegrabot.joystick from Joystick

joystick = Joystick()

joystick.connect()

while (joystick.isConnected()):
    joystick.setData()
    
    print joystick.getJoyOneYAxis()
    print joystick.getJoyTwoYAxis()
    print joystick.getButtonVal()
    
