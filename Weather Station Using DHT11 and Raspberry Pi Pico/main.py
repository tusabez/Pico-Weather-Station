from machine import Pin, I2C
import utime as time
from pico_i2c_lcd import I2cLcd
from DHT22 import DHT22

i2c = I2C(id=1,scl=Pin(27),sda=Pin(26),freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
dht_data = Pin(15,Pin.IN,Pin.PULL_UP)
dht_sensor=DHT22(dht_data,Pin(14,Pin.OUT),dht11=False)

while True:
     T,H = dht_sensor.read()
    #Converted to Fahrenheit (FT) for LCD display
    FT = T*1.8+32
    if T is None:
        print(" sensor error")
    else:
        print("{:3.1f}'C  {:3.1f}%".format(T,H))
    #DHT22 not responsive if delay too short
    time.sleep_ms(500)
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr('Temp:')
    lcd.move_to(10,0)
    #If using Celsius, change (FT) to (T) and "F" to "C" on line below
    lcd.putstr(str(round(FT, 1))+"F")
    lcd.move_to(0,1)
    lcd.putstr('Humidity:')
    lcd.move_to(10,1)
    lcd.putstr(str(H)+"%")
