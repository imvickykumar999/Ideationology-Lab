// Include the Servo library 
#include <Servo.h> 

// Declare the Servo pin 
int servoPin = 3; 

int trigPin = 9;    //Trigger
int echoPin = 12;    //Echo
//int ledoff = 6;
long duration, cm, inches;

bool check;

// Create a servo object 
Servo Servo1; 

bool condition(long dis){
  if(dis < 30){
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)

     // Make servo go to 0 degrees 
     Servo1.write(0); 
     delay(1000); 
     return true;
  }
  else{
      digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW

     // Make servo go to 90 degrees 
     Servo1.write(90); 
     delay(1000); 
     return false;
  }
}

void setup() { 
  // We need to attach the servo to the used pin number 
  Servo1.attach(servoPin); 

  pinMode(LED_BUILTIN, OUTPUT);

  //Serial Port begin
  Serial.begin (9600);
  
  //Define inputs and outputs
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop(){ 

    
  // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
 
  // convert the time into a distance
  cm = (duration/2) / 29.1;
  inches = (duration/2) / 74; 

  check = condition(cm);
  Serial.println(check);
  
  Serial.print(inches);
  Serial.print("in, ");
  Serial.print(cm);
  Serial.print("cm");
  Serial.println();
  
  delay(250);
  
//   Make servo go to 180 degrees 
//   Servo1.write(180); 
//   delay(1000);
}
