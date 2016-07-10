import HTU21DDriver
from sensors import SensorBase
from sensors import Measurements

class Sensor(SensorBase.SensorBase):
    def __init__(self, options_list):
        self._config = options_list
        self._driver = HTU21DDriver.HTU21DDriver()
        
    def measure(self):
        measurements = list()
        for entry in self._config:
            if (entry[1] == 'Enabled'):
                if (entry[0] == 'Temperature'):
                    meas = Measurements.Measurements(self._driver.readTempC(), 'C')
                    measurements.append(meas)
                if (entry[0] == 'Humidity'):
                    meas = Measurements.Measurements(self._driver.readRelativHumidity(), '%')
                    measurements.append(meas)
        return measurements

