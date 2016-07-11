from sensors import SensorBase
from Measurements import Measurement
from sensors.drivers.BMP085.BMP085Driver import BMP085Driver


class Sensor(SensorBase.SensorBase):
    def __init__(self, options_list):
        self._config = options_list
        self._driver = BMP085Driver()
        self._sensors = dict()

        if options_list['SealevelPressure']['Enabled'] == True:
            self._sensors['Pa'] = options_list['SealevelPressure']['sensorid']

        if options_list['Temperature']['Enabled'] == True:
            self._sensors['C'] = options_list['Temperature']['sensorid']
        
    def measure(self, unit):
        if unit in self._sensors:
            if unit == 'C':
                return Measurement(self._driver.read_temperature(), unit, self._sensors[unit])

            if unit == 'Pa':
                return Measurement(self._driver.read_sealevel_pressure(self._config["altitude"]), unit, self._sensors[unit])

        return None

