import urllib

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


class MeasurementWebservice:
    def __init__(self, configuration):
        self._configuration = configuration

    def sync(self, data):
        try:
            passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
            passman.add_password(None, self._configuration["SyncURL"], self._configuration["Username"], self._configuration["Password"])
            authhandler = urllib2.HTTPBasicAuthHandler(passman)
            opener = urllib2.build_opener(authhandler)
            urllib2.install_opener(opener)

            params = {"version": "0.1",
                      "format": "json",
                      "measurands": data}

            jsonResults = urllib2.urlopen(self._configuration["SyncURL"], urllib.urlencode(params)).read()
            print(jsonResults)
        except Exception:
            print("Webservice error")
            return False
        return True
