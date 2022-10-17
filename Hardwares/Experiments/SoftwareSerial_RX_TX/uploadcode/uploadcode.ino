
//https://stackoverflow.com/a/19720372/11493297
#include <SoftwareSerial.h>

#define rxPin 8
#define txPin 7

SoftwareSerial mySerial(rxPin, txPin); // RX, TX
char inputByte;

void setup() {
  pinMode(13,OUTPUT);
  digitalWrite(13,HIGH);

  mySerial.begin(9600);
  mySerial.print("Hello, world?;");
}

void loop(){
   while(mySerial.available()>0){
    inputByte = mySerial.read();
    
//    mySerial.print(inputByte);
//    mySerial.print(";");

    if (inputByte=='1'){
      digitalWrite(13,HIGH);
      mySerial.print("Turned ON;");
      }
  
    else if (inputByte=='0'){
      digitalWrite(13,LOW);
      mySerial.print("Turned OFF;");
      } 

    else
      mySerial.print("Enter either 1 or 0;");
  }
}
