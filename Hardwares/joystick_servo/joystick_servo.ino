
#include <Servo.h> 

Servo Servo1; 
int servoPin = 3; 

int VRx = A0;
int VRy = A1;
int SW = 2;

int xPosition = 0;
int yPosition = 0;
int SW_state = 0;
int mapX = 0;
int mapY = 0;

void setup() {
  Serial.begin(9600); 
  
  pinMode(VRx, INPUT);
  pinMode(VRy, INPUT);
  pinMode(SW, INPUT_PULLUP); 
  
  pinMode(LED_BUILTIN, OUTPUT);
  Servo1.attach(servoPin); 
}

void loop() {
  xPosition = analogRead(VRx);
  yPosition = analogRead(VRy);
  SW_state = digitalRead(SW);
  mapX = map(xPosition, 0, 1023, -512, 512);
  mapY = map(yPosition, 0, 1023, -512, 512);
  
  Serial.print("X: ");
  Serial.print(mapX);
  Serial.print(" | Y: ");
  Serial.print(mapY);
  Serial.print(" | Button: ");
  Serial.println(SW_state);

  if ((abs(mapX) > 100 and abs(mapY) > 100) or (abs(mapX) < 100 and abs(mapY) < 100)){
    Servo1.write(0);
  }
  else{
    Servo1.write(180); 
  }

// Push Joystick's Button to turn LED Off

  if (SW_state == 1){ 
    digitalWrite(LED_BUILTIN, HIGH);
  }
  else{
    digitalWrite(LED_BUILTIN, LOW);
  }
  
  delay(100);  
}
