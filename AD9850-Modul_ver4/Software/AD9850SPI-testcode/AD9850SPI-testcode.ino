//Testcode funktioniert!

#include <AD9850SPI.h>
#include <SPI.h>

const int W_CLK_PIN = 13;
const int FQ_UD_PIN = 8;
const int RESET_PIN = 9;
//Data = 11.



double freq = 900000;
double trimFreq = 124999500;

int phase = 0;

void setup(){
  DDS.begin(W_CLK_PIN, FQ_UD_PIN, RESET_PIN);
  DDS.calibrate(trimFreq);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop(){
  DDS.up();
  digitalWrite(3, HIGH);
  DDS.setfreq(freq, phase);
  delay(200);
  digitalWrite(3, LOW);
  //DDS.down();
  //delay(2000);
  freq = freq + 10000;
  //DDS.powerOff();
//  DDS.up();
//  delay(3000);
//  DDS.down();
//  
//  DDS.powerOff();
//  delay(5000);
  
  
  
}
