/*
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
*/
include <Servo.h> 
 
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
  //myservo1.attach(9);
  //myservo2.attach(3);
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
  int data[6];
  int i=0;
  while(Serial.available()>0){
        data[i]=Serial.read();
        i++;
  }
        
  
//  if(Serial.available()){ // only send data back if data has been sent
     //char inByte = Serial.read(); // read the incoming data
     // = Serial.read();
     myservo1.write(data[1])
     myservo2.write(data[2])
     if(data[3]==1){
       digitalWrite(shooter1,HIGH)
       delay(200)
       digitalWrite(shooter1,LOW)  
     }else if(data[3] == 2){
       digitalWrite(shooter1,HIGH)
       delay(300)
       digitalWrite(shooter1,LOW)
     }else if(data[3] == 3){
       digitalWrite(shooter1,HIGH)
       delay(400)
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
 // }
  
  delay(15);
} 
