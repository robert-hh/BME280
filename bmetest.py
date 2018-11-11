#
# Example. Using I2C at P9, P10
#
from machine import I2C
from bme280 import *
i2c=I2C()
bme280 = BME280(i2c=i2c)
bme280.values

