import uuid, json, os
from datetime import datetime

class State:
    
    def __init__(self):
        pass
    
    def run(self):
        pass
    
    
    def environment(self, place_id: str):
        try:
            place_folder = f"{os.getcwd()}/storage/storage_places/{place_id}/"
            environment_data = None
            with open(f"{place_folder}/environment.json", 'r') as archive:
                environment_data = json.load(archive)
            return self.response(200, "local criado com sucesso", environment_data)
        except Exception as e:
            return self.response(422, "Não foi possivel criar uma região", e)
    
    def place(self, place_id: str):
        try:
            place_folder = f"{os.getcwd()}/storage/storage_places//{place_id}/"
            place_data = None
            with open(f"{place_folder}/manifest.json", 'r') as archive:
                place_data = json.load(archive)
            return self.response(200, "local criado com sucesso", place_data)
        except Exception as e:
            return self.response(422, "Não foi possivel criar uma região", e)
    
    def places(self):
        try:
            places_folder = f"{os.getcwd()}/storage/storage_places/"
            places_folders_list = os.listdir(places_folder)
            places_list = []
            for folder in places_folders_list:
                with open(f"{places_folder}/{folder}/manifest.json", 'r') as archive:
                    places_list.append(json.load(archive))
            return self.response(200, "local criado com sucesso", places_list)
        except Exception as e:
            return self.response(422, "Não foi possivel criar uma região", e)
    
    def create_place(self, place_form: dict ) -> dict:
        try:
            place_uuid = uuid.uuid1()
            place_folder = f"{os.getcwd()}/storage/storage_places/{place_uuid}"
            place_data = {
                            **place_form,
                            "id": str(place_uuid), 
                            "local": place_folder,
                            "createdAt": str(datetime.now()),
                            "updatedAt": str(datetime.now())
                        } 
            os.makedirs(place_folder, exist_ok=True)
            with open(f"{place_folder}/manifest.json", "w", encoding="utf-8") as archive:
                json.dump(
                    place_data,
                    archive,
                    indent=4
                )
            with open(f"{place_folder}/world.json", "w", encoding="utf-8") as archive:
                json.dump(
                    [],
                    archive,
                    indent=4
                )
            return self.response(200, "local criado com sucesso",
                {
                    "id": place_uuid,
                    "trace": place_folder,
                    "place": place_data
                })
        except Exception as e:
            return self.response(422, "Não foi possivel criar uma região", e)
        
    def create_local_enterprise(self, place_form: dict ) -> dict:
        try:
            enterprise_uuid = uuid.uuid1()
            enterprise_folder = f"{os.getcwd()}/data/storage_enterprises/{enterprise_uuid}"
            enterprise_data = {
                            **place_form,
                            "id": str(enterprise_uuid), 
                            "local": enterprise_folder,
                            "createdAt": str(datetime.now()),
                            "updatedAt": str(datetime.now())
                        }
            os.makedirs(enterprise_folder, exist_ok=True)
            with open(f"{enterprise_folder}/manifest.json", "w", encoding="utf-8") as archive:
                json.dump(
                    enterprise_data,
                    archive,
                    indent=4
                )
            return self.response(200, "local criado com sucesso", enterprise_data)
        except Exception as e:
            return self.response(422, "Não foi possivel criar uma região", e)
    