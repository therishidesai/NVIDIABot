NVIDIABot
=========
Currently I have been working with Nvidia's Jetson Tk1 board to convert a FIRST FRC robot into a fully custom robot. This robot uses the Jetson board and an Arduino as it's main processor. This robot uses ROS(Robot Operating System) for all of the file handling. 

Check out the video here: https://www.youtube.com/watch?v=AkMDzctFkO0

In the new working bot folder there are 2 sub directories:

nvidiabot ROS Package
=====================
This is the ROS package that has the main python scripts for this project.

FRCMotorControl Arduino Sketchbook
==================================
This is the code that constantly runs on the Arduino and sends motor values to the motor controllers.
