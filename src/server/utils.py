import os, json

class Preferences:
    
    def __init__(self, root: str = None) -> str:
        self.root = root or os.getcwd()
    
    def apply(self) -> object:
        if not hasattr(self, "preferences"):
            raise RuntimeError("Preferences not loaded. Call load() first.")
        self.create_folder(self.root, self.preferences)
        return self

    def load(self, relative_location: str = None) -> object:
        with open(f"{self.root}/{relative_location}", "r", encoding="utf-8") as file:
            json_preferences_data = json.load(file)
            self.preferences = json_preferences_data
        return self
    
    def create_folder(self, path: str, data: dict):
        for key, value in data.items():
            folder_path = os.path.join(path, key)
            os.makedirs(folder_path, exist_ok=True)  
            
            if isinstance(value, dict):
                self.create_folder(folder_path, value)