import json
import os

class Saver:
    def __init__(self, file):
        self.file = file

    def save(self, data):
        with open(self.file, "w") as file:
            json.dump(data, dile, indent = 4)

    def read(self):
        with open(self.file, "r") as file:
            data = file.read()

            if os.stat(slef.file).st_size == 0:
                return []

            return json.loads(data)
