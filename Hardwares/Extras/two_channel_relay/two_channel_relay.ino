
char inputByte;

void setup() {
 Serial.begin(9600);
 Serial.println("Hello, world !");
 
 pinMode(13,OUTPUT);
 pinMode(12,OUTPUT);
 digitalWrite(13,LOW);
 digitalWrite(12,LOW);
}

void loop() {
  while(Serial.available()>0){
    
      inputByte = Serial.read();
      Serial.print(inputByte);
      
      if (inputByte=='1'){
      digitalWrite(13, HIGH);
    }
    
    else if (inputByte=='0'){
      digitalWrite(13, LOW);
      } 

    else if (inputByte=='2'){
      digitalWrite(12, HIGH);
      }

    else if (inputByte=='3'){
      digitalWrite(12, LOW);
      }
    }
}
