
// Sensor pins
#define sensorPower 7
#define sensorPin A0

const int buzzer = 12; //buzzer to arduino pin 12

// Value for storing water level
int val = 0;

void setup() {

  // Set buzzer - pin 12 as an output
  pinMode(buzzer, OUTPUT);

  //led indicator when singing a note
  pinMode(13, OUTPUT);

  // Set D7 as an OUTPUT
  pinMode(sensorPower, OUTPUT);
  
  // Set to LOW so no power flows through the sensor
  digitalWrite(sensorPower, LOW);
  
  Serial.begin(9600);
}

void loop() {
  //get the reading from the function below and print it
  int level = readSensor();
  
  Serial.print("Water level: ");
  Serial.println(level);

  if (level > 50){
      tone(buzzer, 1000); // Send 1KHz sound signal...
      delay(1000);        // ...for 1 sec
      noTone(buzzer);     // Stop sound...
      delay(1000);        // ...for 1sec
      digitalWrite(13, LOW);
  }
  else{
      digitalWrite(13, HIGH);
  }
  
  delay(1000);
}

//This is a function used to get the reading
int readSensor() {
  digitalWrite(sensorPower, HIGH);  // Turn the sensor ON
  delay(10);              // wait 10 milliseconds
  val = analogRead(sensorPin);    // Read the analog value form sensor
  digitalWrite(sensorPower, LOW);   // Turn the sensor OFF
  return val;             // send current reading
}
