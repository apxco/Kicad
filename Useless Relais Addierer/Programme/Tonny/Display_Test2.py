from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import framebuf,sys,time

pix_res_x  = 128 # SSD1306 horizontal resolution
pix_res_y = 64   # SSD1306 vertical resolution

i2c_dev = I2C(0,scl=Pin(21),sda=Pin(20),freq=1000000)  # start I2C on I2C1 (GPIO 26/27)
i2c_addr = 0x30 #  I2C address in hex format

oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev) # oled controller

print("oled1  ")



ByteA = b"101"
ByteB = b"11111111"
#ByteE = b"111111111"
ByteE = ByteA+ByteB
    
while True:


    pause = 1

    
    
    
    print("x", ByteA)  
    print("Y", ByteB)
    print("g", ByteE)
    
    print("A", int(ByteA, 2))  
    print("B", int(ByteB, 2))   
    print("E", int(ByteE, 2))
    
    hhh=int(ByteA,2)+int(ByteA,2)
    
    print("hhh", hhh)


    oled.fill(0) # clear the display
 
    print('Text zeilenweise darstellen')
    oled.text(f"Byte A        {int(ByteA, 2)}", 0, 0)
    oled.text(bytes.decode(ByteA), 0, 10) # Text, X, Y
    oled.text(f"Byte A    + {int(ByteB, 2)}", 0, 20)
    oled.text(bytes.decode(ByteB), 0, 30) # Text, X, Y
    oled.text(f"Ergebnis   {int(ByteE, 2)}", 0, 40)
    oled.text(bytes.decode(ByteE), 0, 50) # Text, X, Y

    oled.show()


    print('Linien zeichnen')
    oled.line(80, 33, 120, 33, 1) # Von x,y / Nach x,y / Farbe
    oled.show()
  #  oled.line(117, 53, 10, 10, 1) # Von x,y / Nach x,y / Farbe
  #  oled.show()


    time.sleep(pause)

   
    

#     print('Blinkender Pixel in der Mitte')
#     for _ in range (100):
#         oled.pixel(63, 32, 1) # X, Y, AN
#         oled.show()
#         time.sleep(0.5)
#         oled.pixel(63, 32, 0) # X, Y, AUS
#         oled.show()
#         time.sleep(0.5)
#         print("test")
# 
# 
# 
# 
#     time.sleep(pause)





