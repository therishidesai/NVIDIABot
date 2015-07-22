/*
 * rosserial Servo Control Example
 *
 * This sketch demonstrates the control of hobby R/C servos
 * using ROS and the arduiono
 * 
 * For the full tutorial write up, visit
 * www.ros.org/wiki/rosserial_arduino_demos
 *
 * For more information on the Arduino Servo Library
 * Checkout :
 * http://www.arduino.cc/en/Reference/Servo
 */
#define USE_USBCON
#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#include <Servo.h> 
#include <ros.h>
#include <std_msgs/UInt16.h>

ros::NodeHandle  nh;
//Since Arduino sees FRC Motor Controllers as servos they are set as Servo Objects
Servo motor1, motor2, motor3, motor4;

void servo_cb( const std_msgs::UInt16& cmd_msg){
  int motorSpeed = cmd_msg.data;
  //Since The motor controllers are servo objects thespeed is given in servo positions.
  //Motor Speeds: stopped=90, full forward =0 , full reverse = 180
  motor1.write(motorSpeed);
  motor2.write(motorSpeed);
  motor3.write(motorSpeed);
  motor4.write(motorSpeed);
  //digitalWrite(13, HIGH-digitalRead(13));  //toggle led  
}


ros::Subscriber<std_msgs::UInt16> sub("drive_motors", servo_cb);

void setup(){
//  pinMode(13, OUTPUT);

  nh.initNode();
  nh.subscribe(sub);
  
  motor1.attach(3); //attach it to pin 3
  motor2.attach(10);//attach it to pin 10
  motor3.attach(12);//attach it to pin 12
  motor4.attach(13);//attach it to pin 13
}

void loop(){
  nh.spinOnce();
  delay(1);
}
