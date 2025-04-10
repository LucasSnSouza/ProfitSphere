import os

class PathsHelper:
    
    def __init__(self):
        self.root = os.getcwd()
    
    def get_enterprise_path(self):
        return os.path.join(self.root, "storage", "storage_enterprises")
    
    def get_places_path(self):
        return os.path.join(self.root, "storage", "storage_places")