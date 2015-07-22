void setup()
{
  Serial.begin(9600);
  Serial.println("Ready");
}

void loop(){
  int red,red1, green, blue=0;
  while (Serial.available()>0){
    red1 = Serial.parseInt();
    int red2=Serial.parseInt();
    int red = (red1 * 10)+red2 ;
    green = Serial.parseInt();
    blue = Serial.parseInt();
    int colors = red+blue+green;
    Serial.println(colors);
    //Serial.flush();
  }
  
  
}
