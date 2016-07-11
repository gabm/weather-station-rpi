

class SensorsHandler(object):
    def __init__(self, enabled_sensors):
        self._sensor_list = list()
        for sensor in enabled_sensors:
            self.create_sensors(sensor)
        
    def create_sensors(self, sensor):
        if (sensor.name() == 'HTU21D'):
            from sensors.drivers.HTU21D.Sensor import Sensor as HTU21DSensor

            sensor = HTU21DSensor(sensor.options())
            self._sensor_list.append(sensor)
            
    def measure(self, unit):
        measurements = list()
        for sensor in self._sensor_list:
            meas = sensor.measure(unit)
            if meas is not None:
                measurements.append(meas)

        return measurements
