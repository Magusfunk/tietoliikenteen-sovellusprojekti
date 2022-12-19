#include "accelerator.h"
#include "weightsBiases.h"

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
  int x = 0;
  int y = 1;
  int z = 2;
  float neuralResult[6];
  Accelerator Aobject;
  Aobject.makeMeasurement();
  Measurement m = Aobject.getMeasurement();

  Serial.print("Neuroverkon tulos ennen aktivointia: ");
  for (int outputNode = 0; outputNode < 6; outputNode++) {
    neuralResult[outputNode] = m.x * weights[x][outputNode] + 
                               m.y * weights[y][outputNode] + 
                               m.z * weights[z][outputNode] + 
                               biases[outputNode];
    Serial.print("<");
    Serial.print(neuralResult[outputNode], 9);
    Serial.print(">");
  }
  float testi[6] = { 1, 2, 3, 4, 5, 6 };
  activation(neuralResult);
  for (int e = 0; e < 6; e++) {
  }
  Serial.println("");
}

void activation(float* x) {
  float exponented[6];
  float euler = 2.718281828;
  float sum = 0;
  //Eksponenttiin korotus ja summaus
  for (int s = 0; s < 6; s++) {
    sum = sum + pow(euler, x[s]);
  }

  for (int i = 0; i < 6; i++) {
    x[i] = pow(euler, x[i]) / sum;
  }
}

int calculateWinner(int input[5]) {
  int minVal = 200;
  int minPlace = 7;
  float output;

  for (int index = 0; index < 6; index++) {
    if (input[index] < minVal) {
      minVal = input[index];
      minPlace = index;
    }
  }
  return output;
}
