from database.MeasurementWebservice import MeasurementWebservice
from database.MeasurementDAO import MeasurementDAO
from database.QueueSyncer import QueueSyncer


class MeasurementDatabase(object):
    def __init__(self, configuration):
        self._configuration = configuration

    def persistMeasurements(self, measurements, locationid):
        daoMeasurement = MeasurementDAO()
        for measurement in measurements:
            daoMeasurement.persistMeasurement(measurement.value(), measurement.unit(), locationid, measurement.sensorid())
            daoMeasurement.insertIntoSyncQueue()

        daoMeasurement.closeHandle()

    def syncQueue(self):
        webservice = MeasurementWebservice(self._configuration)
        queueSyncer = QueueSyncer()

        queueSyncer.sync(webservice)
        queueSyncer.closeHandle()