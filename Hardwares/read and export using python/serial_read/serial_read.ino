
#define led 13
char value = '0';

void setup() { 
      Serial.begin(9600); 
      pinMode(led, OUTPUT);
      digitalWrite (led, LOW);
      Serial.println("Connection established...");
   }
 
void loop() {
     while (Serial.available())
        {
           value = Serial.read();
           Serial.print(value);
        }
     
     if (value == '1')
        digitalWrite (led, HIGH);
     
     else if (value == '0')
        digitalWrite (led, LOW);
   }
   
