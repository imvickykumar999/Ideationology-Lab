
//https://www.tinkercad.com/things/jifiCImBU2C

#include <IRremote.h>
int RECV_PIN = 11;

IRrecv irrecv(RECV_PIN);
decode_results results;

void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    irrecv.resume(); // Receive the next value 

    if(results.value==0xA78E696B){ // 1
      digitalWrite(13,HIGH);
    }
    else if(results.value==0xBF09EE05){ // 2
      digitalWrite(13,LOW);
    }

    if(results.value==0xBF09EE04){ // 3
      digitalWrite(2,HIGH);
    }
    else if(results.value==0xAF8B007B){ // 4
      digitalWrite(2,LOW);
    }

  }
  delay(100);
}
