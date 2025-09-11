
//The timer can either run from 0 to 255, or from 0 to a fixed value. (The 16-bit Timer 1 has additional modes to supports timer values up to 16 bits.)
//In the following "x" is "0", "1" or "2" for timer 0, 1 or 2.
//
//Setting the timer prescaller:
//  Setting                          Prescale_factor
//  TCCRxB = _BV(CS01);              1
//  TCCRxB = _BV(CS11);              8
//  TCCRxB = _BV(CS10) | _BV(CS11);  64
//  TCCRxB = _BV(CS12);              256
//  TCCRxB = _BV(CS10) | _BV(CS12);  1024
//
//WGM bits:
//  Control the overall mode of the timer (These bits are split between TCCRnA and TCCRnB registers)
//
//CS bits
//  Clock Select bits, these control the clock prescaler
//
//COMnA bits
//  Compare Match Output A Mode bits.  These enable/disable/invert output A
//
//COMnB bits
//  Compare Match Output B Mode bits.  These enable/disable/invert output B
//
//OCRnA and OCRnB registers
//  Output Compare Registers, set the levels at which outputs A and B will be affected. When the timer value matches the register value, the corresponding output will be modified as specified by the mode.

/*
Timer output  Arduino output  Chip pin  Pin name
OC0A      6       12      PD6
OC0B      5       11      PD5
OC1A      9       15      PB1
OC1B      10        16      PB2
OC2A      11        17      PB3
OC2B      3       5     PD3

*/






#define potiPinIntense PC0
#define potiPinDauer PC1
#define ledPin 11

int16_t  potiValueIntense;
int16_t  potiValueDauer;
int16_t  dauer;
char up;
     
void setup() {
  Serial.begin(115200);
  
  noInterrupts();   
  // Timer0
  // reset Timer0
  TCCR0A = 0; // set TCCR0A register to 0
  TCCR0B = 0; // set TCCR0B register to 0
  TCNT0  = 0; // reset counter value
  //Timer aktivieren
  TCCR0A |= (1 << WGM01); // enable timer0 CTC mode
  TIMSK0 |= (1 << OCIE0A); // enable timer0 compare interrupt
  OCR0A = 124; // set compare match register of timer 0 (max. value: 255 = 2^8 - 1)
  // 64 prescaling for timer0
  TCCR0B |= (1 << CS02) | (1 << CS00) |(0 << CS01);  
    
   
  // Timer 1 
  TCCR1A = 0;  
  TCCR1B = 0;
  TCCR1A |= (1 << WGM10) | (1 << WGM11) | (1 << WGM12) | (1 << WGM13); /*  Fast PWM 10Bit */
  TCCR1B  |= (0 << CS12) | (1 << CS11) | (0 << CS10);   //* Set Preescaler 8 */           
  TCCR1A |= (1 << COM1A1) | (1<<COM1B1);/* No invertir la Senal PWM */
  DDRB |= (1 << DDB1)| (1 << DDB2); //PWM-Pin 9 and 10 als Output

  interrupts();

//pinMode(8, OUTPUT);
pinMode(ledPin, OUTPUT);
up=1;

}
   

ISR(TIMER0_COMPA_vect) {
   noInterrupts();  
  // timer0 interrupt to-do code here
  
  
  potiValueDauer = analogRead(potiPinDauer);
 //Serial.println(potiValueDauer);
  potiValueDauer = map(potiValueDauer, 0, 1023, 1, 512);

  // Dreieck aus(maximum)  
  if (potiValueDauer <= 500)
  { 
    digitalWrite(ledPin, LOW);
    dauer = 0;
    interrupts();
    return;
  }
  digitalWrite(ledPin, HIGH);
  // Burstdauer
  
  if (up == 1)
  {
  dauer = dauer + (potiValueDauer) ;
  }
  else 
  {
  dauer = dauer - (potiValueDauer);  
  }

  
  if (dauer <= 1)
  {
    up = 1;
  }
  if (dauer >= 512)
  {
    up = 0;
  } 
  
 
  interrupts();
//Serial.println(potiValueDauer);
//Serial.println(dauer);
//Serial.println(dauer);
}

void setIntense() 
  {
  potiValueIntense = analogRead(potiPinIntense);   // Resolucion 10Bit
  potiValueIntense = map(potiValueIntense, 0, 1023, 512, 0);

  potiValueIntense = potiValueIntense-dauer;
  if (potiValueIntense <=0)
  {
  potiValueIntense = 0;
  }
    
  //Serial.println(potiValueIntense);
  OCR1A = potiValueIntense;
  OCR1B = (potiValueIntense-1023)*-1;
  };

void setDauer()
  {

  
  };

void loop() {

 
setIntense();

  







 
}
