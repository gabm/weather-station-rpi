from DatabaseConfigReader import DatabaseConfigReader
from StationConfigReader import StationConfigReader
from sensors.SensorsHandler import SensorsHandler
from database.MeasurementDatabase import MeasurementDatabase

stationConfigReader = StationConfigReader('../config/station.yml')
databaseConfigReader = DatabaseConfigReader('../config/database.yml')

measurementDatabase = MeasurementDatabase(databaseConfigReader.getConfiguration())

sensorHandler = SensorsHandler(stationConfigReader.readSensorConfigs())
measurementDatabase.persistMeasurements(sensorHandler.measure('C'), stationConfigReader.readLocationID())
#measurementDatabase.syncQueue()
