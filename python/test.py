import FilePaths
from StationConfigReader import StationConfigReader
from sensors.SensorsHandler import SensorsHandler
from database.MeasurementDatabase import MeasurementDatabase

if not FilePaths.IsLayoutValid():
    FilePaths.InitDefaultFiles()
    print("Created default config in: " + FilePaths.GetBaseFolder())
    print("Please revise the settings and start again!")
    exit()

stationConfigReader = StationConfigReader(FilePaths.GetStationConfigFilename())

measurementDatabase = MeasurementDatabase(stationConfigReader.readWebserviceConfig())

sensorHandler = SensorsHandler(stationConfigReader.readSensorConfigs())
measurementDatabase.persistMeasurements(sensorHandler.measure('C'), stationConfigReader.readLocationID())
#measurementDatabase.syncQueue()
