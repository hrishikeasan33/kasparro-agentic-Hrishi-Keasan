
import json

class DataParserAgent:
    def __init__(self, path):
        self.path = path

    def load_product(self):
        return json.load(open(self.path))
