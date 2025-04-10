import json
import os

class JSONHelper:
    def __init__(self):
        self.local = ""
        self.json = {}
    
    def find(self, local: str):
        self.local = local
        with open(local, "r") as archive:
            self.json = json.load(archive)
        return self
    
    def add(self, add_data):
        self.json = {
            **self.json,
            **add_data
        }
        return self
    
    def push(self, key: str, append_data):
        if key in self.json:
            self.json[key].append(append_data)
        else:
            raise ValueError('Não existe existe essa chave no JSON')
        return self
    
    def apply(self):
        with open(self.local, "w", encoding="utf-8") as archive:
            json.dump(self.json, archive, indent=4)
        return self.json
        
    def get(self):
        return self.json
    