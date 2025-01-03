from machine import Pin, SoftI2C
import ssd1306_I2C

i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306_I2C.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello, World !', 0, 0)
oled.show()
