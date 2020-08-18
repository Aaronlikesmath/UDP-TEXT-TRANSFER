import json

class JsonWrap(object):
    # def __init__(self, filename):
    #     self.filename = filename
    def __init__(self, filename):
        self.filename = filename

    def openjs(self):
        with open(self.filename) as f:
            data = json.load(f)
        return data
    
    def openjsvar(self, var):
        with open(self.filename) as f:
            datadict = json.load(f)
        
        data = datadict.get(var, "Error var not found in json")
        return data