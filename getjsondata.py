class GetJsonData:
    import requests

    def __init__(self, http, json=[]):
        self.http = http
        self.json = json

    def download(self):
        import requests
        from time import perf_counter

        t1 = perf_counter()
        print("Downloading...")
        try:
            r = requests.get(self.http)
        except Exception as e:
            print(f"Error retrieving data: {e}")
            return False
        else:
            if r.status_code == 200:
                self.json = r.json()
                return True
            else:
                return False
        finally:
            t2 = perf_counter()
            print(f"Done in {t2 - t1}")

    def getJson(self):
        if not self.json is None:
            return self.json
        else:
            return None

    def printJson(self):
        print(self.json)

    def convertStringJson(self, data):
        from json import loads

        return loads(data)

    def getJsonString(self):
        from json import dumps

        return dumps(self.json, indent=2)

    def saveJsonToFile(self, filename):
        from json import dump

        with open(filename, "w") as file:
            dump(self.json, file)

    def loadJsonFromFile(self, filename):
        from json import load

        with open(filename) as file:
            self.json = load(file)

        return self.json
