import json
from sqlite3 import connect, OperationalError

import FilePaths


class QueueSyncer:
    def __init__(self):
        # sqlite connecton
        try:
            self.conn = connect(FilePaths.GetDatabaseFilename())
            self.cursor = self.conn.cursor()

        except OperationalError:  # Can't locate database file
            print("cant locate database file")
            exit(1)

    def sync(self, webservice):
        data = self.getData()
        json_data = json.dumps(data)
        success = webservice.sync(json_data)

        if (success):
            # remove
            self.clearSyncQueue()

    def closeHandle(self):
        'Closes the connection to the database'
        self.conn.commit()  # Make sure all changes are saved
        self.conn.close()

    def getData(self):
        cmd = "SELECT M.CREATIONDATE, M.LOCATION_ID, M.SENSOR_ID, M.VALUE, M.UNIT FROM MEASURAND M INNER JOIN SYNC_QUEUE S ON M.ID = S.MEASURAND_ID"
        self.cursor.execute(cmd)
        return self.cursor.fetchall()

    def clearSyncQueue(self):
        cmd = "DELETE FROM SYNC_QUEUE"
        self.cursor.execute(cmd)
