import json, os, uuid

from datetime import datetime

class PlaceService:
    
    def __init__(self):
        self.folder = f"{os.getcwd()}/storage/storage_places/"
    
    def get_by_id(self, place_id: str) -> dict:
        place_data = None
        with open(f"{self.folder}/{place_id}/manifest.json", 'r') as archive:
            place_data = json.load(archive)
        return place_data
    
    def get_all(self) -> list:
        places_folders_list = os.listdir(self.folder)
        places_list = []
        for folder in places_folders_list:
            with open(f"{self.folder}/{folder}/manifest.json", 'r') as archive:
                places_list.append(json.load(archive))
        return places_list
    
    def create(self, form) -> dict:
        place_uuid = uuid.uuid1()
        place_data = {
                        **form,
                        "id": str(place_uuid), 
                        "local": f"{self.folder}/{place_uuid}/",
                        "createdAt": str(datetime.now()),
                        "updatedAt": str(datetime.now())
                    } 
        os.makedirs(f"{self.folder}/{place_uuid}/", exist_ok=True)
        with open(f"{self.folder}/{place_uuid}/manifest.json", "w", encoding="utf-8") as archive:
            json.dump(
                place_data,
                archive,
                indent=4
            )
        with open(f"{self.folder}/{place_uuid}/world.json", "w", encoding="utf-8") as archive:
            json.dump(
                [],
                archive,
                indent=4
            )
        return {
                    "id": place_uuid,
                    "trace": f"{self.folder}/{place_uuid}/",
                    "place": place_data
                }