import json


JSON_DATA_PATH = './sample.json'

class LoadJsonData(object):

    def __init__(self, json_file=None):
        if not json_file:
            json_file = self.get_json_file_path()
        self.json_file = json_file


    def get_json_file_path(self):
        json_file_path = None

        if not json_file_path:
            json_file_path = JSON_DATA_PATH
        return json_file_path


    def load_json_data(self):
        with open(self.json_file, 'r') as json_file:
            self.data = json.load(json_file)
        return self.data