# BME280 Micropython driver for the BME280 sensor

This is a driver for the Bosch BME280 temperature/pressure/humidity sensor,
for use with MicroPython on Pycom of ESP8266 boards. It is also compatible with
the BMP280 which provides the same interface but temperature + pressure only.

Two different variants of the library are supplied. bme20_int.py uses integer
arithmetic. bme280_float.py uses float arithmetic for the compensation  of the
raw values. The results are (almost) the identical, but the format of the
returned values differs.

## About the BME280

The Bosch BME280 Environmental Sensor is a combined temperature, pressure and
humidity sensor. It can communicate via I2C or SPI; this driver uses I2C.

See the datasheet at https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BME280_DS002.pdf
for details.

## Class

bme= BME280(i2c=i2c, mode=BME280_OSAMPLE_8, address=BME280_I2CADDR)

mode is the setting for oversampling of the humidity value, address the i2c
address used.

## Property

### values = BME280.value

The `values` property is a convenience function that provides a tuple of
human-readable string values to quickly check that the sensor is working.
In practice, the method to use is `read_compensated_data()` which returns
a `(temperature, pressure, humidity)`-tuple

## Methods

### values = read_compensated_data(result = None)

Values is an array of either integers of floats, holding the values of temperature,
pressure and humidity. The format differs for integers and floats:

#### Integer formats:
* `temperature`:  the temperature in hundredths of a degree Celsius. For example,
the value 2534  indicates a temperature of 25.34 degrees.
* `pressure`: the atmospheric pressure. This 32-bit value consists of 24 bits
indicating the integer value, and 8 bits indicating the fractional value. To get
a value in Pascals, divide the return value by 256. For example, a value of
24674867 indicates 96386.2Pa, or 963.862hPa.
* `humidity`: the relative humidity. This 32-bit value consists of 22 bits
indicating the integer value, and 10 bits indicating the fractional value.
To get a value in %RH, divide the return value by 1024. For example, a value of
47445 indicates 46.333%RH.

#### Float formats
* `temperature`:  the temperature in degree Celsius.
* `pressure`: the atmospheric pressure in Pascal.
* `humidity`: the relative humidity in percent.

If the parameter result is supplied as an array of the appropriate type, The
return values will in addition be stored in that array, and the array will be
returned.

### read_raw_data(result)
Store the raw sensor data into the array result, which must provide space for three
32 bit integers, as provided for instance by `array("i", [0, 0, 0])`. This
method is used internally.

### Example

Copy `bme280.py` onto the board. Then:

``` python
#
# this script assumes the default connection of the I2C bus
# On pycom devuces that is P9 = SDA, P10 = scl
#
import machine
import bme280

i2c = machine.I2C()
bme = bme280.BME280(i2c=i2c)

print(bme.values)
```
