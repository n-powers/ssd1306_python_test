from machine import Pin,I2C
import ssd1306_scroll as ssd1306

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

lcd = ssd1306.SSD1306_I2C(128,64,i2c)
lcd.text("Micropython",0,0)
lcd.text("are",24,16)
lcd.text("Awesome",64,24)
lcd.show()