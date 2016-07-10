

class SensorsHandler(object):
    def __init__(self, enabled_sensors):
        self._sensor_list = list()
        for sensor in self._enabled_sensors:
            self.create_sensors(sensor)
        
    def create_sensors(self, sensor):
        if (sensor.name() == 'HTU21D'):
            import drivers
            import drivers.HTU21D
            import drivers.HTU21D.Sensor
            print('imported')
            sensor = drivers.HTU21D.Sensor.Sensor(sensor.options())
            self._sensor_list.append(sensor)
            
    def measure():
        for sensor in self._sensor_list:
            print(sensor.measure())
