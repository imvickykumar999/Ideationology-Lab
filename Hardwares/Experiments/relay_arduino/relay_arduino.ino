
//Home Automation using Relay DPDT and IR Remote
//https://www.tinkercad.com/things/9jgopMlHDS2

// ------------------(Hybrid Code)-------------------

#include <IRremote.h>

int RECV_PIN = 11;

IRrecv irrecv(RECV_PIN);
decode_results results;

void setup() {
 Serial.begin(9600);
  
 pinMode(13,OUTPUT);
 digitalWrite(13,HIGH);

 irrecv.enableIRIn(); // Start the receiver
}

void loop() {
  if (irrecv.decode(&results)) {
    
    Serial.println(results.value, HEX);
    irrecv.resume(); // Receive the next value
    
    if(results.value==0xFD08F7){ // for button 1
      digitalWrite(13,LOW);
    }
       else if(results.value==0xFD8877){ // for button 2
      digitalWrite(13,HIGH);
    }
  }
  delay(100);
}

// -------------------(Serial read)----------------------

/*

char inputByte;

void setup() {
 Serial.begin(9600);
 pinMode(13,OUTPUT);
 digitalWrite(13,HIGH);
}

void loop() {
  while(Serial.available()>0){
    
      inputByte = Serial.read();
      Serial.println(inputByte);
      
      if (inputByte=='1'){
      digitalWrite(13,HIGH);
    }
    
    else if (inputByte=='0'){
      digitalWrite(13,LOW);
      } 
    }
}

*/

// ------------------(IR Remote)----------------------

/*

#include <IRremote.h>

int red=9;
int green=13;
int blue=10;
int RECV_PIN = 11;

IRrecv irrecv(RECV_PIN);
decode_results results;

void setup()
{
  pinMode(red,OUTPUT);
  pinMode(blue,OUTPUT);
  pinMode(green,OUTPUT);

  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    irrecv.resume(); // Receive the next value
    
    if(results.value==0xFD08F7){
      digitalWrite(red,HIGH);
      digitalWrite(green,LOW);
      digitalWrite(blue,LOW);
    }
       else if(results.value==0xFD48B7){
      digitalWrite(red,LOW);
      digitalWrite(green,LOW);
      digitalWrite(blue,HIGH);
    }
       else if(results.value==0xFD8877){
      digitalWrite(red,LOW);
      digitalWrite(green,HIGH);
      digitalWrite(blue,LOW);
    }
  }
  delay(100);
}

*/
