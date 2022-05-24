
#include "SoftwareSerial.h"

SoftwareSerial mySerial(2, 3);

String cmd = "";

void setup()
{
  mySerial.begin(9600);
  Serial.begin(9600);
  Serial.println("Initializing...");
  delay(1000);

  mySerial.println("AT");                 // Sends an ATTENTION command, reply should be OK
  updateSerial();
  mySerial.println("AT+CMGF=1");          // Configuration for sending SMS
  updateSerial();
  mySerial.println("AT+CNMI=1,2,0,0,0");  // Configuration for receiving SMS
  updateSerial();
}

void loop()
{
  updateSerial();
}

void updateSerial()
{
  delay(500);
  while (Serial.available()) 
  {

    cmd+=(char)Serial.read();
 
    if(cmd!=""){
      cmd.trim();  // Remove added LF in transmit
      if (cmd.equals("S")) {
        sendSMS();
      } else {
        mySerial.print(cmd);
        mySerial.println("");
      }
    }
  }
  
  while(mySerial.available()) 
  {
    Serial.write(mySerial.read());//Forward what Software Serial received to Serial Port
  }
}

void sendSMS(){
  mySerial.println("AT+CMGF=1");
  delay(500);
  
//  mySerial.println("AT+CMGS=\"+918239957923\"\r");
  mySerial.println("AT+CMGS=\"+919987488458\"\r");
  
  delay(500);
  mySerial.print("Hi, Vicks!");
  
  delay(500);
  mySerial.write(26);
}
