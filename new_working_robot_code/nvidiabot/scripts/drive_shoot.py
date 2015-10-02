#!/usr/bin/env python

import rospy
from diggerbot.msg import JoyVals, ArduinoVals

left_is_pressed = False
right_is_pressed = False
def main():
    rospy.init_node('drive_shoot_controller')
    joy = rospy.Subscriber('joyvals', JoyVals, drive_shoot_callback)
    try:
        rospy.spin()
    except rospy.ROSInterruptException:pass

def drive_shoot_callback(joy):
    aduino_value_pub = rospy.Publisher('arduinovals', ArduinoVals)
    arduino_vals = ArduinoVals()
    
    throttle = joy.joystick_vals[0]
    turn = joy.joystick_vals[1]

    shots = shooter(joy.button_vals)
    speeds = arcade_drive(throttle, turn)
    arduino_vals.speeds = speeds
	arduino_vals.shots = shots
    arduino_value_pub.publish(arduino_vals)

def shooter(buttons_pressed):
	fire = []
    left_button = 10     
    right_button = 11
    left_pressed = left_button in buttons_pressed
    right_pressed = right_button in buttons_pressed
	
	if left_pressed == True and left_is_pressed == False:
		left_is_pressed = True
	elif left_pressed == False and left_is_pressed == True:
		fire.append(1)
		left_is_pressed = False
	else:
		fire.append(0)
	
	if right_pressed == True and right_is_pressed == False:
		right_is_pressed = True
	elif right_pressed == False and right_is_pressed == True:
		fire.append(1)
		right_is_pressed = False
	else:
		fire.append(0)

def arcade_drive(throttle, turn):
    speeds = []
    
    left_speed = throttle + turn
    right_speed = throttle - turn
    
    skimmed_left_speed = left_speed + skim(left_speed)
    skimmed_right_speed = right_speed + skim(right_speed)

    speeds.append(get_arduino_speed(skimmed_left_speed))
    speeds.append(get_arduino_speed(skimmed_right_speed))
    
    return speeds

def skim(speed):
    gain = 0.1

    if speed > 1.0:
        return -((speed - 1.0) * gain)
    elif speed < -1.0:
        return -((speed + 1.0) * gain)
    else:
        return 0.0

def get_arduino_speed(speed):
    if speed > 0.0:
        motor_speed = 90-int(speed*90.0)
        return motor_speed
    elif speed < 0.0:
        motor_speed = 90 + int(abs(speed)*90.0)
        return motor_speed
    elif speed == 0.0:
        motor_speed=90
        return motor_speed
    else:
        motor_speed=-1
        return motor_speed

if __name__ == '__main__':
    main()
