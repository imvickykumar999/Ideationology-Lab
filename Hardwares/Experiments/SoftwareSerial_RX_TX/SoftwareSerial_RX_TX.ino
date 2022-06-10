
#include <SoftwareSerial.h>

// use 10, 11 pair in Arduino Mega
SoftwareSerial mySerial(10, 11); // RX, TX 
char inputByte;

void setup() {
 mySerial.begin(9600);
 Serial.begin(9600);
 Serial.println("Hello, world !");
 
 pinMode(13,OUTPUT);
 digitalWrite(13,HIGH);
}

void loop() {
  while(mySerial.available()>0){
    
      inputByte = mySerial.read();
//      Serial.println(inputByte);
      
      if (inputByte=='1'){
      digitalWrite(13,HIGH);
    }
    
    else if (inputByte=='0'){
      digitalWrite(13,LOW);
      } 
    }
}
