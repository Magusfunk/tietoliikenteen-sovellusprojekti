#include "accelerator.h"
#include "keskipiste.h"

/*
   0 z +
   1 z -
   2 x +
   3 x -
   4 y +
   5 y -

*/

// Määritellään kytkentänavat kiihtyvyysanturille ja muuttujat:
const int VccPin2 = A0;  // Käyttöjännite
const int GNDPin2 = A4;  // laitteen maa-napa

void setup() {
  Serial.begin(9600);


  //Kiihtvyys - anturin napojen määrittely:
  pinMode(VccPin2, OUTPUT);  // Kiihtyvyysanturin käyttöjännite Vcc
  pinMode(GNDPin2, OUTPUT);  // Kiihtyvyysanturin GND

  // Asetetaan syöttöjännite (5V UNO-BOARDILLA, 3.3V Genuino 101:llä) ja maa-arvot (0V):
  digitalWrite(VccPin2, HIGH);
  delayMicroseconds(2);
  digitalWrite(GNDPin2, LOW);
  delayMicroseconds(2);
}

void loop() {
  float distance = 0;
  int winner[6];
  int tulos = 0;
  Accelerator Aobject;
  Aobject.makeMeasurement();
  Measurement m = Aobject.getMeasurement();  
  for (int piste = 0; piste < 6; piste++) {    
    distance = abs(sqrt(pow(keskipisteet[piste][0] - m.x, 2) + pow(keskipisteet[piste][1] - m.y, 2) + pow(keskipisteet[piste][2] - m.z, 2)));
    winner[piste] = distance;    
  }
  Serial.println();
  Serial.print("Winner: ");
  for (int index = 0; index < 6; index++) {
    Serial.print("<");
    Serial.print(winner[index]);
    Serial.print(">");
  }
  tulos = laskeVoittaja(winner);
  Serial.println();
  Serial.print("Voittaja:");
  Serial.println(tulos);  
  delay(1000);
}

int laskeVoittaja(int input[5]) {
  int minVal = 200;
  int minPlace = 7;

  // for (int index = 0; index < 6; index++) {
  //   Serial.print("<");
  //   Serial.print(input[index]);
  //   Serial.print(">");
  // }

  for (int index = 0; index < 6; index++) {
    if (input[index] < minVal) {
      minVal = input[index];
      // Serial.print("index:");
      // Serial.println(index);
      minPlace = index;
    }
  }


  // Serial.print("minPlace:");
  // Serial.println(minPlace);
  return keskipisteet[minPlace][3];
}
