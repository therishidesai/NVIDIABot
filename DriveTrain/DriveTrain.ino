// Sweep
// by BARRAGAN <http://barraganstudio.com> 
// This example code is in the public domain.


#include <Servo.h> 
 
Servo myservo1;  // create servo object to control a servo 
Servo myservo2;//pytyhon
Servo myservo3;
Servo myservo4;// a maximum of eight servo objects can be created 
 
int pos = 0;    // variable to store the servo position 
 
void setup() 
{ 
 // myservo1.attach(8);
 // myservo2.attach(9);
 /*
   MC2 and MC7 in arduino port 9
   MC6 and MC with no fan in arduino port 3
 */
  myservo1.attach(9);
  myservo2.attach(3);
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready");
 //Serial.begin(9600); 
  //Serial.println("Ready"); // attaches the servo on pin 9 to the servo object 
} 
 
 
void loop() 
{ 
  if(Serial.available()){ // only send data back if data has been sent
     //char inByte = Serial.read(); // read the incoming data
     int motorSpeed = Serial.read();
     Serial.println(motorSpeed); 
     myservo1.write(motorSpeed);
     myservo2.write(motorSpeed);
     //myservo3.write(motorSpeed);
   //  myservo4.write(motorSpeed);// send the data back in a new line so that it is not all one long line
  }
  
  delay(15);
} 
