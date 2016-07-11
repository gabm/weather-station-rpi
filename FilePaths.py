import os
import shutil
import sqlite3

def GetStationConfigFolder():
    return GetBaseFolder() + "config/"

def GetDataFolder():
    return GetBaseFolder() + "data/"

def GetBaseFolder():
    home = os.path.expanduser("~")
    return home + '/.weather-station-pi/'

def GetStationConfigFilename():
    return GetStationConfigFolder() + "station.yml"

def GetDatabaseFilename():
    return GetDataFolder() + "measuranddb"


def IsLayoutValid():
    isValid = os.path.isdir(GetBaseFolder())
    isValid = isValid & os.path.isdir(GetStationConfigFolder())
    isValid = isValid & os.path.isdir(GetDataFolder())

    isValid = isValid & os.path.exists(GetStationConfigFilename())
    isValid = isValid & os.path.exists(GetDatabaseFilename())

    return isValid


def InitDefaultFiles():
    CreateFolders()

    shutil.copy("config/station.yml.default", GetStationConfigFilename())

    ImportDefaultDatabase()

def ImportDefaultDatabase():

    con = sqlite3.connect(GetDatabaseFilename())
    f = open('database/config/sqlite/setupdatabase.sql', 'r')
    sql = f.read()
    try:
        con.executescript(sql)
    except sqlite3.OperationalError:
        None

def CreateFolders():
    try:
        os.mkdir(GetBaseFolder())
    except FileExistsError:
        None

    try:
        os.mkdir(GetStationConfigFolder())
    except FileExistsError:
        None

    try:
        os.mkdir(GetDataFolder())
    except FileExistsError:
        None