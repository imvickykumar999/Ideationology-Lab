
int IRSensor = 2; // connect ir sensor to arduino pin 2
int LED = 13; // conect Led to arduino pin 13


void setup() 
{
  pinMode (IRSensor, INPUT); // sensor pin INPUT
  pinMode (LED, OUTPUT); // Led pin OUTPUT

  Serial.begin (9600);
}

void loop()
{
  int statusSensor = digitalRead (IRSensor);
  
  if (statusSensor == 1){
    digitalWrite(LED, LOW); // LED LOW
    Serial.println("Low");
  }
  
  else{
    digitalWrite(LED, HIGH); // LED High
    Serial.println("High");
  }  

  delay(1000);
}
