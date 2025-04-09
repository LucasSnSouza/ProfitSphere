from services.responder_service import Responder
from services.place_service import PlaceService

class PlaceController():
    
    def __init__(self):
        self.place_service = PlaceService()
    
    def get_place_by_id(self, id):
        try:
            return Responder.success(self.place_service.get_by_id(id))
        except Exception:
            return Responder.error("O place não foi encontrado", 404)
        
    def get_all_places(self):
        try:
            return Responder.success(self.place_service.get_all())
        except Exception:
            return Responder.error("O place não foi teste", 404)
        
    def create_place(self, form):
        try:
            return Responder.success(self.place_service.create(form))
        except Exception:
            return Responder.error("O place não foi teste", 404)