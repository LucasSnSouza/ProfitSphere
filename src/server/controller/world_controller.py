from services.responder_service import Responder
from services.world_service import WorldService

class WorldController():
    
    def __init__(self):
        self.world_service = WorldService()