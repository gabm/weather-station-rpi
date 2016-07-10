import ConfigParser
from sensors import SensorConfig

class ConfigReader(object):
    def __init__(self, filename):
        self._configParser = ConfigParser.ConfigParser()
        self._configParser.optionxform=str
        self._configParser.readfp(open(filename))
        
    def parse_sensor_list(self):
        sensor_section = 'Sensors'
        sensors_list = list()
        sensor_entries = self._configParser.options(sensor_section)
        for sensor_entry in sensor_entries:
            if ( self._configParser.get(sensor_section, sensor_entry) == 'Enabled'):
                conf = SensorConfig.SensorConfig(sensor_entry, self._configParser.items(sensor_entry))
                sensors_list.append(conf)
        
        return sensors_list
