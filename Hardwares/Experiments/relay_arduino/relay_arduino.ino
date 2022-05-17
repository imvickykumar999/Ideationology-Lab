
int RelayPin = 6;


void setup() {
  // Set RelayPin as an output pin
  pinMode(RelayPin, OUTPUT);
}


void loop() {
  // Let's turn on the relay...
  digitalWrite(RelayPin, LOW);
  delay(1000);
  
  // Let's turn off the relay...
  digitalWrite(RelayPin, HIGH);
  delay(1000);
}
