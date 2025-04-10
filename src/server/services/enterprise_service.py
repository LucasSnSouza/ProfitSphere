import json, os, uuid

from datetime import datetime
from helpers.paths_helper import PathsHelper
from helpers.json_helper import JSONHelper

class EnterpriseService:
    
    def __init__(self):
        self.paths_helper = PathsHelper()
        
    def get_by_access(self, access):
        list_enterprises = os.listdir(self.paths_helper.get_enterprise_path())
        for enterprise in list_enterprises:
            manifest_data = JSONHelper().find(f"{self.paths_helper.get_enterprise_path()}/{enterprise}/manifest.json").get()
            if 'access' in manifest_data:
                if manifest_data['access'] == access:
                    return manifest_data
            else:
                raise ValueError('O arquivo não possui uma chave de acesso')
    
    def create(self, form):
        enterprise_uuid = uuid.uuid1()
        enterprise_folder = f"{self.paths_helper.get_enterprise_path()}/{enterprise_uuid}"
        enterprise_data = {
                        **form,
                        "id": str(enterprise_uuid), 
                        "local": enterprise_folder,
                        "places": [],
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
        return enterprise_data