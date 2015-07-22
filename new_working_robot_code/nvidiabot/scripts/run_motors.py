#!/usr/bin/env python

import rospy
from std_msgs.msg import String, UInt16
import pygame 

pygame.init()

def get_motor_speed(direction):
    forward_motor_speed = 85
    reverse_motor_speed = 105
    stopped_motor_speed = 90
    if direction == 'f':
        return forward_motor_speed
    elif direction == 'r':
        return reverse_motor_speed
    elif direction == 's':
        return stopped_motor_speed
    else:
        motor_speed =-1
        return motor_speed

def set_motor_speed(speed):
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

def main():
    #pygame.event.pump()
    pygame.joystick.init()
    if pygame.joystick.get_count()>0:
        print pygame.joystick.get_count()
        joy = pygame.joystick.Joystick(0)
        joy.init()   
        
    else:
        print
        return
    rospy.init_node('run_motors')
    cmd_publisher = rospy.Publisher('drive_motors', UInt16)
    while True:
        '''try:
            cmd = raw_input('Movement command ("f", "r","s"): ')
            if cmd != 'f' and cmd != 'r' and cmd != 's':
                continue
            # TODO: Publish cmd onto the 'move_command' topic.
            motor_speed = get_motor_speed(cmd)
            cmd_publisher.publish(motor_speed)
        except EOFError: # Exit the program on Ctrl-D.
            print
            return
        '''
        '''try:
            cmd = float(raw_input('Move Forward=0.0-1.0 Move Reverse=0.0- -1.0:  '))
            if cmd>1.0 or cmd<-1.0:
                continue
            motor_speed=set_motor_speed(cmd)
            cmd_publisher.publish(motor_speed)
        except EOFError:
            print
            return
        '''
        try:
            pygame.event.pump()         
            cmd=joy.get_axis(1)
            if cmd>0.5:
                cmd=0.5
            elif cmd<-0.5:
                cmd=-0.5
            elif cmd<0.2 and cmd>0.0 :
                cmd=0.0           
            elif cmd>-0.2 and cmd<0.0:
                cmd=0.0
            for i in range(joy.get_numbuttons()):
                if joy.get_button(i)==True:
                    if i == 1:
                        cmd=1.0
                        motor_speed=set_motor_speed(cmd)
                        cmd_publisher.publish(motor_speed)
                    else:
                        cmd=1.0
                        motor_speed=set_motor_speed(cmd)
                        cmd_publisher.publish(motor_speed)
                        print
                        return
                            
            motor_speed=set_motor_speed(cmd)
            cmd_publisher.publish(motor_speed)
            
        except EOFError:
            print
            return
if __name__ == '__main__':
    main()
