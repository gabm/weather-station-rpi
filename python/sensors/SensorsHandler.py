

class SensorsHandler(object):
    def __init__(self, enabled_sensors):
        self._enabled_sensors = enabled_sensors
        for sensor in self._enabled_sensors:
            self.import_sensor_module(sensor)
        
    def import_sensor_module(self, sensor):
        if (sensor.name() == 'HTU21D'):
            import drivers
            import drivers.HTU21D
            import drivers.HTU21D.Sensor
            print('imported')
            sensor = drivers.HTU21D.Sensor.Sensor(sensor.options())
