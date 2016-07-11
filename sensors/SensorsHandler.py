

class SensorsHandler(object):
    def __init__(self, enabled_sensors):
        self._sensor_list = list()
        for sensor in enabled_sensors:
            self.create_sensors(sensor)
        
    def create_sensors(self, sensor):
        if (sensor.name() == 'HTU21D'):
            from sensors.drivers.HTU21D.Sensor import Sensor as HTU21DSensor

            device = HTU21DSensor(sensor.options())
            self._sensor_list.append(device)
            print("Created Sensor: " + sensor.name())

        if (sensor.name() == 'BMP085'):
            from sensors.drivers.BMP085.Sensor import Sensor as BMP085Sensor
            device = BMP085Sensor(sensor.options())
            self._sensor_list.append(device)
            print("Created Sensor: " + sensor.name())

        if (sensor.name() == 'MCP9808'):
            from sensors.drivers.MCP9808.Sensor import Sensor as MCP9808Sensor
            device = MCP9808Sensor(sensor.options())
            self._sensor_list.append(device)
            print("Created Sensor: " + sensor.name())

    def measure(self, unit):
        measurements = list()
        for sensor in self._sensor_list:
            meas = sensor.measure(unit)
            if meas is not None:
                measurements.append(meas)

        return measurements

