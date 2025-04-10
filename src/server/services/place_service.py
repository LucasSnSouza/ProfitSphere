import json, os, uuid

from datetime import datetime
from helpers.paths_helper import PathsHelper
from helpers.json_helper import JSONHelper

class PlaceService(PathsHelper):
    
    def __init__(self):
        self.paths_helper = PathsHelper()
    
    def get_by_id(self, place_id: str) -> dict:
        place_data = None
        with open(f"{self.paths_helper.get_places_path()}/{place_id}/manifest.json", 'r') as archive:
            place_data = json.load(archive)
        return place_data
    
    def get_all(self) -> list:
        places_folders_list = os.listdir(self.paths_helper.get_places_path())
        places_list = []
        for folder in places_folders_list:
            with open(f"{self.paths_helper.get_places_path()}/{folder}/manifest.json", 'r') as archive:
                places_list.append(json.load(archive))
        return places_list
    
    def get_all_by_enterprise_id(self, id) -> list:
        places_folders_list = os.listdir(self.paths_helper.get_places_path())
        places_list = []
        for place in places_folders_list:
            manifest_data = JSONHelper().find(f"{self.paths_helper.get_places_path()}/{place}/manifest.json").get()
            if manifest_data.get('enterprise').get('id') == id:
                places_list.append(manifest_data)
        return places_list
    
    def create(self, form) -> dict:
        place_uuid = uuid.uuid1()
        world_uuid = uuid.uuid1()
        place_data = {
                        **form,
                        "id": str(place_uuid),
                        "enterprise": {
                          "id": form.get('enterprise').get('id')
                        },
                        "local": f"{self.paths_helper.get_places_path()}/{place_uuid}/manifest.json",
                        "createdAt": str(datetime.now()),
                        "updatedAt": str(datetime.now())
                    } 
        os.makedirs(f"{self.paths_helper.get_places_path()}/{place_uuid}/", exist_ok=True)
        with open(f"{self.paths_helper.get_places_path()}/{place_uuid}/manifest.json", "w", encoding="utf-8") as archive:
            json.dump(
                place_data,
                archive,
                indent=4
            )
        world_data = {
            "id": str(world_uuid),
            "local": f"{self.paths_helper.get_places_path()}/{place_uuid}/world.json",
            "valuation": 0,
            "createdAt": str(datetime.now()),
            "updatedAt": str(datetime.now()),
            "entities": []
        }
        with open(f"{self.paths_helper.get_places_path()}/{place_uuid}/world.json", "w", encoding="utf-8") as archive:
            json.dump(
                world_data,
                archive,
                indent=4
            )
        with open(f"{self.paths_helper.get_places_path()}/{place_uuid}/employees.json", "w", encoding="utf-8") as archive:
            json.dump(
                [],
                archive,
                indent=4
            )
            
        if 'enterprise' in form and 'id' in form['enterprise']:
            
            JSONHelper().find(f"{self.paths_helper.get_enterprise_path()}/{form.get('enterprise').get('id')}/manifest.json").push("places", str(place_uuid)).apply()
            
            return {
                "id": place_uuid,
                "trace": f"{self.paths_helper.get_places_path()}/{place_uuid}/",
                "place": place_data,
                "world": world_data,
                "employess": []
            }
        else:
            raise ValueError('Id de empresa responsavel não enviado corretamente')
            
        