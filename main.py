#!/usr/bin/env python
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

    if (len(argv) <= 1 or not (argv[0] == '-u' or argv[0] == "--units")):
        print("Please specify the units to measure using '-u <unit1> <unit2>' or '--unit <unit1> <unit2>'")
        exit()

    simOnly = False
    if (argv[len(argv)-1] == '-s'):
        print("Simulating only - no values to database or upload")
        simOnly = True
        del argv[-1]

    stationConfigReader = StationConfigReader(FilePaths.GetStationConfigFilename())
    measurementDatabase = MeasurementDatabase(stationConfigReader.readWebserviceConfig())
    sensorHandler = SensorsHandler(stationConfigReader.readSensorConfigs())

    measuredSomething = False
    for i in range(1, len(argv)):
        measurements = sensorHandler.measure(argv[i])
        
        if len(measurements) == 0:
            print("Specified to measure " + argv[i] + " but nothing has been measured")
            continue

        if (not simOnly):
            measurementDatabase.persistMeasurements(measurements, stationConfigReader.readLocationID())
            measuredSomething = True
        else:
          for meas in measurements:
            print("Meas: " + str(meas.value()) + meas.unit() + " from id: " + str(meas.sensorid()))

    if (measuredSomething and not simOnly):
        measurementDatabase.syncQueue()


if __name__ == "__main__":
    main(sys.argv[1:])
