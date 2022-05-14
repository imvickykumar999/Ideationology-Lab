int led_red = 0; // the red LED is connected to Pin 0 of the Arduino

void setup() {
  // set up all the LEDs as OUTPUT
  pinMode(led_red, OUTPUT);
}

void loop() {
  // turn the green LED on and the other LEDs off
  digitalWrite(led_red, LOW); 
  delay(2000);    // wait 2 seconds 
  digitalWrite(led_red, HIGH); 
  delay(2000);    // wait 2 seconds 
}