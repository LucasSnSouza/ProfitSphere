from services.responder_service import Responder
from services.enterprise_service import EnterpriseService

class EnterpriseController():
    
    def __init__(self):
        self.enterprise_service = EnterpriseService()
        
    def get_enterprise_by_access_key(self, access):
        try:
            result = self.enterprise_service.get_by_access(access)
            if not result:
                return Responder.error("Essa empresa não foi encontrada.", 404)
            return Responder.success(self.enterprise_service.get_by_access(access))
        except Exception:
            return Responder.error(str(Exception), 404)
        
    def create_enterprise(self, form):
        try:
            return Responder.success(self.enterprise_service.create(form))
        except Exception:
            return Responder.error(str(Exception), 404)