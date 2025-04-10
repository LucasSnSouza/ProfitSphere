from flask import request

from services.responder_service import Responder
from controller.place_controller import PlaceController
from controller.enterprise_controller import EnterpriseController

class Routes():
    
    def __init__(self):
        self.place_controller = PlaceController()
        self.enterprise_controller = EnterpriseController()
    
    def bind(self, server):
        
        @server.route("/")
        def handle_main():
            return Responder.success(message="Servidor está funcionando!")

        # - GETs -
        
        @server.route("/place/<string:id>", methods=["GET"])
        def handle_place_by_id(id):
            return self.place_controller.get_place_by_id(id)

        @server.route("/places", methods=["GET"])
        def handle_all_places():
            return self.place_controller.get_all_places()
        
        @server.route("/places/enterprise/<string:id>", methods=["GET"])
        def handle_all_places_by_enterprise_id(id):
            return self.place_controller.get_all_places_by_enterprise_id(id)
        
        @server.route("/enterprise/access/<string:access>", methods=["GET"])
        def handle_enterprise_by_access(access):
            return self.enterprise_controller.get_enterprise_by_access_key(access)        
        
        @server.route("/enterprise/id/<string:id>", methods=["GET"])
        def handle_enterprise_by_id(id):
            return self.enterprise_controller.get_enterprise_by_access_key(id)  

        # - POSTs -
        
        @server.route("/create-place", methods=["POST"])
        def handle_create_place():
            return self.place_controller.create_place(request.get_json())

        @server.route("/create-local-enterprise", methods=["POST"])
        def handle_create_local_enterprise():
            return self.enterprise_controller.create_enterprise(request.get_json())