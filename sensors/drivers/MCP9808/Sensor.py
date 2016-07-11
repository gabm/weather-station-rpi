from sensors import SensorBase
from Measurements import Measurement
from sensors.drivers.MCP9808.MCP9808Driver import MCP9808Driver


class Sensor(SensorBase.SensorBase):
    def __init__(self, options_list):
        self._config = options_list
        self._driver = MCP9808Driver()
        self._sensors = dict()

        if options_list['Temperature']['Enabled'] == True:
            self._sensors['C'] = options_list['Temperature']['sensorid']
        
    def measure(self, unit):
        if unit in self._sensors:
            if unit == 'C':
                return Measurement(self._driver.readTempC(), unit, self._sensors[unit])

        return None

