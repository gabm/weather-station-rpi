import yaml


class DatabaseConfigReader(object):
    def __init__(self, filename):
        with open(filename, 'r') as ymlfile:
            self._cfg = yaml.load(ymlfile)

    def getConfiguration(self):
        return self._cfg