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
#include <Servo.h> 
 
Servo myservo1;  // create servo object to control a servo 
Servo myservo2;//pytyhon
Servo myservo3;
Servo myservo4;// a maximum of eight servo objects can be created 
 
int pos = 0;    // variable to store the servo position 
int shooter1=10;
int shooter2=9;
int mag1=8;
int mag2=7;
void setup() 
{ 
 myservo1.attach(11);
 myservo2.attach(12);
 pinMode(shooter1, OUTPUT);
 pinMode(shooter2, OUTPUT);
 pinMode(mag1, OUTPUT);
 pinMode(mag2, OUTPUT);
 /*
   MC2 and MC7 in arduino port 9
   MC6 and MC with no fan in arduino port 3
 */
  //myservo1.attach(9);
  //myservo2.attach(3);
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready");
  /*
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
  }*/
} 
 
 
void loop() 
{ 
  int data[6];
  while(Serial.available()>0){
        int d01= Serial.parseInt();
        if(d01==1){
          int d02 = Serial.parseInt();
          data[0]=d02;
        }else if(d01==2){
          int d02 = Serial.parseInt();
          int d03 =Serial.parseInt();
          data[0]=(d02*10)+d03;
        }else if(d01==3){
          int d02 = Serial.parseInt();
          int d03 =Serial.parseInt();
          int d04 =Serial.parseInt();
          data[0]=(d02*100)+(d03*10)+d04;
        }
        
        int d11= Serial.parseInt();
        if(d11==1){
          int d12 = Serial.parseInt();
          data[1]=d12;
        }else if(d11==2){
          int d12 = Serial.parseInt();
          int d13 =Serial.parseInt();
          data[1]=(d12*10)+d13;
        }else if(d11==3){
          int d12 = Serial.parseInt();
          int d13 =Serial.parseInt();
          int d14 =Serial.parseInt();
          data[1]=(d12*100)+(d13*10)+d14;
        }
        //data[1]=Serial.parseInt();
        data[2]=Serial.parseInt();
        data[3]=Serial.parseInt();
        data[4]=Serial.parseInt();
        data[5]=Serial.parseInt();
        myservo1.write(data[0]);
        myservo2.write(data[1]);
         if(data[2]==1){
           digitalWrite(shooter1,HIGH);
           delay(50);
           digitalWrite(shooter1,LOW);  
         }else if(data[2] == 2){
           digitalWrite(shooter1,HIGH);
           delay(75);
           digitalWrite(shooter1,LOW);
         }else if(data[2] == 3){
           digitalWrite(shooter1,HIGH);
           delay(100);
           digitalWrite(shooter1,LOW);
         }
         if(data[3]==1){
           digitalWrite(shooter2,HIGH);
           delay(50);
           digitalWrite(shooter2,LOW);  
         }else if(data[3] == 2){
           digitalWrite(shooter2,HIGH);
           delay(75);
           digitalWrite(shooter2,LOW);
         }else if(data[3] == 3){
           digitalWrite(shooter2,HIGH);
           delay(100);
           digitalWrite(shooter2,LOW);
         }
         if(data[4]==1){
           digitalWrite(mag1,HIGH);
           delay(1000);
           digitalWrite(mag1,LOW);
         }
         if(data[5]==1){
           digitalWrite(mag2,HIGH);
           delay(1000);
           digitalWrite(mag2,LOW);
         }

        Serial.flush();
  }
        
  
//  if(Serial.available()){ // only send data back if data has been sent
     //char inByte = Serial.read(); // read the incoming data
     // = Serial.read();
      // }
  
  //delay(15);
} 
