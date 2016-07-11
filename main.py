import getopt
import sys

import FilePaths
from StationConfigReader import StationConfigReader
from sensors.SensorsHandler import SensorsHandler
from database.MeasurementDatabase import MeasurementDatabase


def main(argv):
    if not FilePaths.IsLayoutValid():
        FilePaths.InitDefaultFiles()
        print("Created default config in: " + FilePaths.GetBaseFolder())
        print("Please revise the settings and start again!")
        exit()

    opts, args = getopt.getopt(argv, "u:", ["unit="])

    stationConfigReader = StationConfigReader(FilePaths.GetStationConfigFilename())
    measurementDatabase = MeasurementDatabase(stationConfigReader.readWebserviceConfig())
    sensorHandler = SensorsHandler(stationConfigReader.readSensorConfigs())

    for opt, args in opts:
        if opt in ("-u", "--unit"):
            for arg in args:
                measurementDatabase.persistMeasurements(sensorHandler.measure(arg), stationConfigReader.readLocationID())
            measurementDatabase.syncQueue()


if __name__ == "__main__":
    main(sys.argv[1:])