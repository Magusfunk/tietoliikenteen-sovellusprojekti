#ifndef ACCELERATOR_H
#define ACCELERATOR_H

#include "messaging.h"

const int xPin   = A1;   // x-kanavan
const int yPin   = A2;   // y-kanava
const int zPin   = A3;   // z-kanava

struct Measurement
{
  int x;
  int y;
  int z;
};

class Accelerator
{
  public:
    Accelerator();
    ~Accelerator();
    void makeMeasurement();
    void printMeasurement();
    Measurement getMeasurement();

  private:
    Measurement m;
};

#endif // ACCELERATOR_H
