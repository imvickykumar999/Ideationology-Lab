
//https://www.tinkercad.com/things/jifiCImBU2C

#include <IRremote.h>
int RECV_PIN = 11;

IRrecv irrecv(RECV_PIN);
decode_results results;

void setup()
{
  Serial.begin(9600);
  digitalWrite(13,LOW);
  irrecv.enableIRIn(); // Start the receiver
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    irrecv.resume(); // Receive the next value 

    if(results.value==0x7F30BF54){ // 1
      digitalWrite(13,HIGH);
    }
    if(results.value==0xCD519016){ // 2
      digitalWrite(13,LOW);
    }
  }
  delay(100);
}
