

class SensorsHandler(object):
    def __init__(self, enabled_sensors):
        self._sensor_list = list()
        for sensor in enabled_sensors:
            self.create_sensors(sensor)
        
    def create_sensors(self, sensor):
        if (sensor.name() == 'HTU21D'):
            import drivers
            import drivers.HTU21D
            import drivers.HTU21D.Sensor

            sensor = drivers.HTU21D.Sensor.Sensor(sensor.options())
            self._sensor_list.append(sensor)
            
    def measure(self):
        for sensor in self._sensor_list:
            measurements = sensor.measure()
	    for meas in measurements:
                print(meas.value())
