

//https://github.com/imvickykumar999/hackathon-iot-car-parking/blob/main/esp8266_firebase_led/esp8266_firebase_led.ino


int LED = 5; // Assign LED pin i.e: D1 on NodeMCU

void setup() {

// initialize GPIO 5 as an output

pinMode(LED, OUTPUT);

}

// the loop function runs over and over again forever

void loop() {

digitalWrite(LED, HIGH); // turn the LED on
delay(1000); // wait for a second
digitalWrite(LED, LOW); // turn the LED off
delay(1000); // wait for a second

}



/*

//https://console.firebase.google.com/u/0/project/home-automation-336c0/database/home-automation-336c0-default-rtdb/data/~2FA~2FB~2FC~2FSwitch

#include <WiFi.h>
#include "FirebaseESP32.h"
//#include <Servo.h>

int servoPin = 2; // D2 PIN
//Servo Servo1;

#define WIFI_SSID "Vicky"
#define WIFI_PASSWORD "oyevicks"

#define FIREBASE_HOST "home-automation-336c0-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "lBCCsWbzfCC6Q9jbJRXVlV0siAahBsnPuA3Ba2KM"

FirebaseData firebaseData;

void setup() {
//  Servo1.attach(servoPin);

  Serial.begin(115200);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");

  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(300);
  }

  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);

  //Set database read timeout to 1 minute (max 15 minutes)
  Firebase.setReadTimeout(firebaseData, 1000 * 60);

  pinMode(servoPin, OUTPUT);
}

void loop() {

    if (Firebase.getInt(firebaseData,"/A/B/C/Switch"))
    {
      int val2 = (firebaseData.intData());
      
      if(val2==1){
        digitalWrite(servoPin, HIGH);
        Serial.println("HIGH");
      }
      
      else{
        digitalWrite(servoPin, LOW);
        Serial.println("LOW");
      }

//      if (0<=val2<=180)
//      {
//        Servo1.write(val2);
//        delay(1000);
//      }
//
//      else{
//        Serial.println("enter valid position");
//      }

    }

    delay(200);
  // put your main code here, to run repeatedly:
}

*/
