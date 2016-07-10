

class Measurement(object):
    def __init__(self, value, unit):
        self._value = value
        self._unit = unit
        
    def value(self):
        return self._value
    
    def unit(self):
        return self._unit
        
