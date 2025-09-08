# Bibliotheken laden
from machine import Pin, I2C
import ssd1306
import time

# Wartezeit zwischen den Darstellungen
pause = 4 # Sekunden

# Pin-Konfiguration
i2c_scl_gpio = 21
i2c_sda_gpio = 20

print('I2C Initialisieren')
i2c = I2C(0, scl=Pin(i2c_scl_gpio), sda=Pin(i2c_sda_gpio),freq=100000)

print('OLED-Display initialisieren')
oled_width = 128 # Breite: Pixel
oled_height = 64 # Höhe: Pixel
#oled_width = 128 # Breite: Pixel
#oled_height = 32 # Höhe: Pixel
#display = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c,addr = 0x3c )
display = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c )
time.sleep(0.1)

#print('TCAs initialisieren')
# tca_addr_A = 0x20  # Adresse ByteA TCA modul Ausgang
# tca_addr_B = 0x21  # Adresse ByteB TCA modul Ausgang
# tca_addr_E = 0x22  # Adresse Ergebnis TCA modul Eingang
# 
# # Beispiel: Kanal 0 des ersten TCA-Moduls auswählen
# # Die genauen Werte hängen vom TCA-Chip ab (z.B. TCA9548A)
# # 0x01 bedeutet die Aktivierung von Kanal 0 auf dem TCA-Chip
# i2c.writeto(tca_addr_A, bytes([0x01]))
# print("Kanal 0 auf TCA a ausgewählt")
# 
# # Beispiel: Kanal 3 des zweiten TCA-Moduls auswählen
# i2c.writeto(tca_addr_B, bytes([0x08])) # 0x08 = 2^3, wählt Kanal 3
# print(f"Kanal 3 auf TCA b ausgewählt")


while(1):

    print('Display löschen')
    display.fill(0)
    display.show()

    ByteA = 1101006
    ByteB = 1002612
    ByteE = 7256249

    print('Text zeilenweise darstellen')
    display.text('Byte A', 0, 0)
    display.text(str(ByteA), 0, 10) # Text, X, Y
    display.text('Byte B' , 0, 20)
    display.text(str(ByteB), 0, 30) # Text, X, Y
    display.text('Ergebnis', 0, 40)
    display.text(str(ByteE), 0, 50) # Text, X, Y

    display.show()

    time.sleep(pause)

    print('Display löschen')
    display.fill(0)
    display.show()

    print('Überlangen Text darstellen')
    display.text("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0, 0) # Text, X, Y
    display.text('abcdefghijklmnopqrstuvmxyz', 0, 20)
    display.show()

    time.sleep(pause)

    print('Display löschen')
    display.fill(0)
    display.show()

    print('Pixel-Test')
    display.fill(1)
    display.show()

    time.sleep(pause)

    print('Display löschen')
    display.fill(0)
    display.show()

    print('Blinkender Pixel in der Mitte')
    for _ in range (10):
        display.pixel(63, 32, 1) # X, Y, AN
        display.show()
        time.sleep(0.5)
        display.pixel(63, 32, 0) # X, Y, AUS
        display.show()
        time.sleep(0.5)

    print('Display löschen')
    display.fill(0)
    display.show()

    print('Display-Funktionen')
    display.text('Display-', 28, 15)
    display.text('Funktionen', 20, 35)
    display.show()

    time.sleep(pause)

    print('Display ausschalten')
    display.poweroff()

    time.sleep(pause)

    print('Display einschalten')
    display.poweron()

    print('Darstellung invertiert')
    display.invert(True)
    display.show()
    time.sleep(pause)
    print('Darstellung normal')
    display.invert(False)
    display.show()

    time.sleep(pause)

    print('Helligkeit ändern')
    for brightness in range (0, 100, 10):
        display.contrast(brightness)
        time.sleep(0.5)

    time.sleep(pause)


    print('Display löschen')
    display.fill(0)
    display.show()

    print('Horizontale Linie (von links nach rechts) zeichnen')
    display.hline(0, 0, 128, 1) # Startpunkt: x,y, width (Länge auf X-Achse), colour (Farbe)
    display.show()

    time.sleep(pause)

    print('Vertikale Linie (von oben nach unten) zeichnen')
    display.vline(0, 0, 63, 1) # Startpunkt: x,y, height (Länge auf Y-Achse), colour (Farbe)
    display.show()

    time.sleep(pause)

    print('Linien zeichnen')
    display.line(10, 10, 117, 53, 1) # Von x,y / Nach x,y / Farbe
    display.show()
    time.sleep(pause)
    display.line(117, 53, 10, 10, 1) # Von x,y / Nach x,y / Farbe
    display.show()

    time.sleep(pause)

    print('Rechteck zeichnen')
    display.rect(10, 10, 108, 44, 1) # Von x,y / Pixel nach rechts,unten / Farbe
    display.show()

    time.sleep(pause)

    print('Gefülltes Rechteck zeichnen')
    display.fill_rect(20, 20, 88, 24, 1) # Von x,y / Pixel nach rechts,unten / Farbe
    display.show()

    print('Ende')
