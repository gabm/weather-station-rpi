from ConfigReader import ConfigReader
from sensors.SensorsHandler import SensorsHandler

cfg_reader = ConfigReader('../config/station.yml')
handler = SensorsHandler(cfg_reader.readSensorConfigs())
handler.measure('C')
