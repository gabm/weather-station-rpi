from abc import ABCMeta, abstractmethod

class SensorBase(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def measure(self, unit): pass