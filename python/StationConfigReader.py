import yaml
from sensors import SensorConfig

class StationConfigReader(object):
    def __init__(self, filename):
        with open(filename, 'r') as ymlfile:
            self._cfg = yaml.load(ymlfile)

    def readSensorConfigs(self):
        configList = list()
        for sensor in self._cfg['Sensors']:
            conf = SensorConfig.SensorConfig(sensor, self._cfg[sensor])
            configList.append(conf)
        
        return configList


    def readLocationID(self):
        return self._cfg['General']['locationid']
