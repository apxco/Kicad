from machine import Pin, I2C, ADC

#Homepage: https://github.com/TTitanUA/micropython_rotary_encoder
#PyPI-Seite: https://pypi.org/project/micropython-rotary-encoder/
import ssd1306
import framebuf,sys,time

#Homepage: https://github.com/TTitanUA/micropython_rotary_encoder
#PyPI-Seite: https://pypi.org/project/micropython-rotary-encoder/
from micropython_rotary_encoder import RotaryEncoderRP2, RotaryEncoderEvent
import utime
import random

#erstelle I2C Bus Objekt
i2c_dev = I2C(0,scl=Pin(21),sda=Pin(20),freq=1000000)  

#Adressen
Adr_TCAA = 0b111000 #0x38 Byte A Schreiben
Adr_TCAB = 0b111001 #0x39 Byte B Schreiben
Adr_TCAC = 0b111010 #0x3a Ergebnis Lesen

#Oled einrichten
Adr_TCAD = 0b111100 #0x3c Display
pix_res_x  = 128 # SSD1306 horizontal resolution
pix_res_y = 64   # SSD1306 vertical resolution

# erstelle Oled Objekt
oled = ssd1306.SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev, Adr_TCAD) 

#Setup Rotary Encoder
en_pin_clk_A = Pin(16, Pin.IN, Pin.PULL_UP)
en_pin_dt_A = Pin(17, Pin.IN, Pin.PULL_UP)
en_pin_sw_A = Pin(22, Pin.IN, Pin.PULL_UP)

en_pin_clk_B = Pin(18, Pin.IN, Pin.PULL_UP)
en_pin_dt_B = Pin(19, Pin.IN, Pin.PULL_UP)
en_pin_sw_B = Pin(26, Pin.IN, Pin.PULL_UP)

carry_pin = Pin(15, Pin.IN, None)

# erstelle encoder Objekt
encoderA = RotaryEncoderRP2(en_pin_clk_A, en_pin_dt_A )
encoderB = RotaryEncoderRP2(en_pin_clk_B, en_pin_dt_B )
 
#TCA Einrichten
TCA9534_REGISTER_INPUT_PORT = const(0x00)
TCA9534_REGISTER_OUTPUT_PORT = const(0x01)
TCA9534_REGISTER_CONFIGURATION = const(0x03)   
 
def reg_write(addr, reg, data): #Schreiben aud I2C
    msg = bytearray()
    msg.append(data)
    return i2c_dev.writeto_mem(addr, reg, msg)    
    
def read_port(addr):#Lesen von I2C
    port_in = i2c_dev.readfrom_mem(addr,TCA9534_REGISTER_INPUT_PORT,8)
    return int.from_bytes(port_in,8,'little')

#Setze Konfigurationsregister TCA9534
reg_write(Adr_TCAA, TCA9534_REGISTER_CONFIGURATION, 0x00) #Schreiben ByteA
reg_write(Adr_TCAB, TCA9534_REGISTER_CONFIGURATION, 0x00) #Schreiben Byte B
reg_write(Adr_TCAC, TCA9534_REGISTER_CONFIGURATION, 0xff) #Lesen Ergebnis

#Setze Startwerte
Eingabe = 0
ByteA=1
ByteB=1
ByteE=2
Modus=0
Timer=0
Timer_norm=0
Zufallszaeler=5000
Pixel_norm=pix_res_x/Zufallszaeler

def turn_left_A():
    global Eingabe
    if en_pin_sw_A.value() == 1:
        Eingabe = -1
    else:
        Eingabe = -10

def turn_right_A():
    global Eingabe
    if en_pin_sw_A.value() == 1:
        Eingabe = 1
    else:
        Eingabe = 10

def turn_left_B():
    global Eingabe
    if en_pin_sw_B.value() == 1:
        Eingabe = -2 #funktioniert nicht
    else:
        Eingabe = -10 #funktioniert nicht

def turn_right_B():
    global Eingabe
    if en_pin_sw_B.value() == 1:
        Eingabe = 2 #funktioniert nicht???
    else:
        Eingabe = 10 #funktioniert nicht???

def leseA(Ein1):
    global Eingabe
    Eingabe = 0
    encoderA.raw_tick()
    Ein1 += Eingabe
    if Ein1 < 0:
        Ein1 = 255
    elif Ein1 > 255:
        Ein1 = 0
    return Ein1

def leseB(Ein1):
    global Eingabe
    Eingabe = 0
    encoderB.raw_tick()  
    Ein1 += Eingabe
    if Ein1 < 0:
        Ein1 = 255
    elif Ein1 > 255:
        Ein1 = 0
    return Ein1
        
def zufall():
    x=random.randint(0, 255)
    y=random.randint(0, 255)
    reg_write(Adr_TCAA, TCA9534_REGISTER_OUTPUT_PORT, x) #Setze Relais A
    reg_write(Adr_TCAB, TCA9534_REGISTER_OUTPUT_PORT, y) #Setze Relais B 
    return x,y

def anzeige(ByteA, ByteB, ByteE, Timer_norm): 
    oled.fill(0) # clear the display    
    #anzeige ob Ergebnis aktuell Korrekt ist
    if ByteE == ByteA+ByteB:    
        oled.invert(0)
    else:
        oled.invert(1)
    
    oled.text(f"Byte A       {ByteA}", 0, 5)
    oled.text(f"Byte B    +  {ByteB}", 0, 25)
    oled.text(f"Ergebnis     {ByteE}", 0, 45)
    oled.line(0, 60, Timer_norm, 60, 1) # Ladebalken
    oled.line(80, 33, 120, 33, 1) # Von x,y / Nach x,y / Farbe
    oled.show()
    
def leseErgebnis(): #Lese Werte aus TCA
    ByteE=read_port(Adr_TCAC) # Sendet ganz viele Werte
    ByteE=bin(ByteE) # zu BIN Wandeln
    ByteE=ByteE[-8:] # nur letzte 8 Zeichen holen
    ByteE=int(ByteE,2) #zu int wandeln   
    if carry_pin.value() == 1: # prüfen ob Carry Bit gesetzt ist
        ByteE +=256
    return ByteE

#Display Angangswerte    
anzeige(ByteA,ByteB,ByteE, 0)
#Setze anfagswert Relais
reg_write(Adr_TCAA, TCA9534_REGISTER_OUTPUT_PORT, ByteA) #Schreibe A
reg_write(Adr_TCAB, TCA9534_REGISTER_OUTPUT_PORT, ByteB) #Schreibe B

# subscribe to events
encoderB.on(RotaryEncoderEvent.TURN_RIGHT, turn_right_B)
encoderB.on(RotaryEncoderEvent.TURN_LEFT, turn_left_B)
encoderA.on(RotaryEncoderEvent.TURN_LEFT, turn_left_A)
encoderA.on(RotaryEncoderEvent.TURN_RIGHT, turn_right_A)

while True:
        
    ByteB = leseB(ByteB)
    ByteA = leseA(ByteA)

    # Modus 0, Zufall
    if Modus == 0:
        Timer+=1
        Timer_norm = int(Timer*Pixel_norm) 
        if Timer > Zufallszaeler:
            Timer = 0
            ByteA,ByteB=zufall()  
            Modus=1
    
    # Modus 1 Tastendruck B startet Relais, einmal.
    if en_pin_sw_B.value() == 0:
        Modus = 1
        Timer = 0
        
    #Modus 2 Tastendruck A B startet Relais, jede Eingabe    
    if en_pin_sw_B.value() == 0 and en_pin_sw_A.value() == 0:
        Modus = 2
        Timer=0
  
    if Modus == 1:     
        counter = 10 #Schritte zum Ergebnis, muss ja nicht so schnell sein hier
        while counter >= 1:
            anzeige(ByteA, ByteB, ByteE, Timer_norm)
            reg_write(Adr_TCAA, TCA9534_REGISTER_OUTPUT_PORT, int(ByteA/counter)) #Schreibe A
            time.sleep(0.1)
            reg_write(Adr_TCAB, TCA9534_REGISTER_OUTPUT_PORT, int(ByteB/counter)) #Schreibe B
            counter -=1
        Modus=0
        
    if Modus == 2:
        reg_write(Adr_TCAA, TCA9534_REGISTER_OUTPUT_PORT, ByteA) #Schreibe A
        reg_write(Adr_TCAB, TCA9534_REGISTER_OUTPUT_PORT, ByteB) #Schreibe B
            
     #lesen des Ergebnisses
    ByteE=leseErgebnis()
    #Neu Anzeigen 
    anzeige(ByteA, ByteB, ByteE, Timer_norm)   


         