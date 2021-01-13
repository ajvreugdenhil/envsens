#include <SparkFunHTU21D.h>
#include <Wire.h>
HTU21D myHumidity;

float last_humidity = 0;
float last_temperature = 0;
bool values_read = false;

void setup() {
  Serial.begin(9600);
  myHumidity.begin();
}

void loop()
{
  if(Serial.available())
  {
    Serial.read();
    Serial.print("{\"Humidity\":");
    Serial.print(last_humidity);
    Serial.print(",\"Temperature\":");
    Serial.print(last_temperature);
    Serial.println("}");
    values_read = true;
  }
  
  // Update values every second or after they've been read.
  if (((millis() % 1000) == 0) || values_read) 
  {
    last_humidity = myHumidity.readHumidity();
    last_temperature = myHumidity.readTemperature();
    values_read = false;
  }
}