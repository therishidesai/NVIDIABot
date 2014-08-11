// Sweep
// by BARRAGAN <http://barraganstudio.com> 
// This example code is in the public domain.


#include <Servo.h> 
 
Servo myservo1;  // create servo object to control a servo 
Servo myservo2;//pytyhon
Servo myservo3;
Servo myservo4;// a maximum of eight servo objects can be created 
 
int pos = 0;    // variable to store the servo position 
int shooter1, shooter2, mag1, mag2;
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
  
  if(Serial.available()){
    int ports[] = Serial.read()
    for(int i=0; i<6; i++){
       if(i==0){
         myservo1.attach(ports[i]);
       }else if(i==1){
         myservo2.attach(ports[i]);
       }else{
         pinMode(ports[i], OUTPUT)
       }
    }
    shooter1=ports[2]
    shooter2=ports[3]
    mag1 = ports[4]
    mag2 = ports[5]
  }
} 
 
 
void loop() 
{ 
  if(Serial.available()){ // only send data back if data has been sent
     //char inByte = Serial.read(); // read the incoming data
     int data[] = Serial.read();
     myservo1.write(data[1])
     myservo2.write(data[2])
     if(data[3]==1){
       digitalWrite(shooter1,HIGH)
       delay(1000)
       digitalWrite(shooter1,LOW)  
     }else if(data[3] == 2){
       digitalWrite(shooter1,HIGH)
       delay(2500)
       digitalWrite(shooter1,LOW)
     }else if(data[3] == 3){
       digitalWrite(shooter1,HIGH)
       delay(5000)
       digitalWrite(shooter1,LOW)
     }
     if(data[4]==1){
       digitalWrite(mag1,HIGH)
       delay(1000)
       digitalWrite(mag1,LOW)
     }
     if(data[5]==1){
       digitalWrite(mag2,HIGH)
       delay(1000)
       digitalWrite(mag2,LOW)
     }
  }
  
  delay(15);
} 
