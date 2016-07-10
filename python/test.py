import weather_config_reader as cfg
from  sensors import SensorsHandler as sensors_handler

cfg_reader = cfg.ConfigReader('../config/station.cfg')
handler = sensors_handler.SensorsHandler(cfg_reader.parse_sensor_list())
