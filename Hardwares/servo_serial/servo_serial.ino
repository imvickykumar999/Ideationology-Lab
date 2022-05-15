
// Include the Servo library 
#include <Servo.h> 

// Declare the Servo pin 
int servoPin = 3; 

const int led=13;
int value=0;

// Create a servo object 
Servo Servo1; 

void setup() { 
  // We need to attach the servo to the used pin number 
  Servo1.attach(servoPin); 

  Serial.begin(9600); 
  pinMode(led, OUTPUT);
  digitalWrite (led, LOW);
  Serial.println("Connection established...");
}

void loop(){ 

   while (Serial.available()){
       value = Serial.read();
    }
   
   if (value == '0'){
      Servo1.write(0); 
      digitalWrite (led, LOW);
   }

   else if (value == '1'){
      Servo1.write(180); 
      digitalWrite (led, HIGH);
   }
}
