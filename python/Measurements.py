

class Measurement(object):
    def __init__(self, value, unit, sensorid):
        self._value = value
        self._unit = unit
        self._sensorid = sensorid
        
    def value(self):
        return self._value
    
    def unit(self):
        return self._unit
    
    def sensorid(self):
        return self._sensorid
        
