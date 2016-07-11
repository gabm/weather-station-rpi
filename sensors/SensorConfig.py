

class SensorConfig(object):
    def __init__(self, name, options):
        self._name = name
        self._options = options
        
    def name(self):
        return self._name
    
    def options(self):
        return self._options
