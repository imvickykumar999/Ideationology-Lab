/*
 * 
 * All the resources for this project: https://www.hackster.io/Aritro
 * Modified by Aritro Mukherjee
 * 
 * 
 */
 
#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h> 

#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.
Servo Servo1; 

int counter = 0; // Counter for number of attempts
int buzzer = 8;
int servoPin = 3; 

void setup() 
{
  pinMode(buzzer, OUTPUT);
  Servo1.attach(servoPin); 

  Serial.begin(9600);   // Initiate a serial communication
  SPI.begin();      // Initiate  SPI bus
  mfrc522.PCD_Init();   // Initiate MFRC522
  
  Serial.println("Approximate your card to the reader...");
  Serial.println();
}

void loop() 
{
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }

  Serial.print("Number of Attempts : ");
  counter += 1;
  Serial.println(counter);
 
  //Show UID on serial monitor
  Serial.print("UID tag :");
  String content= "";
  byte letter;
  
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     Serial.print(mfrc522.uid.uidByte[i], HEX);
     content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  
  content.toUpperCase();
//  Serial.println(content);
  Serial.println();  
  Serial.print("Message : ");
  
  if (content.substring(1) == "DA 91 44 B3") //change here the UID of the card/cards that you want to give access
  {
    Serial.println("Authorized access ;)");
    Servo1.write(0); 

    tone(buzzer, 1000); // Send 1KHz sound signal...
    delay(1000);        // ...for 1 sec
    
    noTone(buzzer);     // Stop sound...
    delay(1000);        // ...for 1sec
    Servo1.write(90); 
  }
 
  else{
    Serial.println("!!! Access denied !!!");
    Servo1.write(90); 
    delay(3000);
  }

 Serial.println();
}
