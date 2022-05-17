
//https://www.programmingboss.com/2021/04/esp32-arduino-serial-communication-with-code.html?m=1

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Hello Boss");
  delay(1500);
}
