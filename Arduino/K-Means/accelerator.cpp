#include "accelerator.h"
#include <arduino.h>

Accelerator::Accelerator()
{
  
}


Accelerator::~Accelerator()
{
 
}

void Accelerator::makeMeasurement()
{
  m = {analogRead(xPin), analogRead(yPin), analogRead(zPin)};
}
void Accelerator::printMeasurement()
{
  Serial.print("X:");
  Serial.print(m.x);
  Serial.print(" Y:");
  Serial.print(m.y);
  Serial.print(" Z:");
  Serial.println(m.z);
}

Measurement Accelerator::getMeasurement()
{
  return m;
}
