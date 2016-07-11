from sensors.drivers.HTU21D.HTU21DDriver import *
from sensors import SensorBase
from Measurements import Measurement

class Sensor(SensorBase.SensorBase):
    def __init__(self, options_list):
        self._config = options_list
        self._driver = HTU21DDriver()
        self._sensors = dict()

        if options_list['Temperature']['Enabled'] == True:
            self._sensors['C'] = options_list['Temperature']['sensorid']

        if options_list['Humidity']['Enabled'] == True:
            self._sensors['Percent'] = options_list['Humidity']['sensorid']
        
    def measure(self, unit):
        if unit in self._sensors:
            if unit == 'C':
                return Measurement(self._driver.readTempC(), unit, self._sensors[unit])

            if unit == 'Percent':
                return Measurement(self._driver.readRelativHumidity(), unit, self._sensors[unit])

        return None

