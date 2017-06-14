#include <SoftwareSerial.h>

SoftwareSerial mySerial(1, 0); // RX, TX
int incomingByte;
float tempC;
int tempPin = A0;
void setup()
{
  mySerial.begin(9600);
}
void loop() // run over and over
{
  if (mySerial.available())
  {
    incomingByte = mySerial.read();
    if (incomingByte == 'e') {
     tempC = analogRead(tempPin); 
     tempC = (5.0 * tempC * 100.0)/1024.0; 
     mySerial.println(tempC);
     delay(200);
    }
  }
}

