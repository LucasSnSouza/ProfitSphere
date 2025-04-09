from flask import request

from services.responder_service import Responder
from controller.place_controller import PlaceController

class Routes():
    
    def __init__(self):
        self.place_controller = PlaceController()
    
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

        # - POSTs -
        
        @server.route("/create-place", methods=["POST"])
        def handle_create_place():
            return self.place_controller.create_place(request.get_json())

        # @server.route("/create-local-enterprise", methods=["POST"])
        # def handle_create_local_enterprise():
        #     try:
        #         data = self.create_local_enterprise(request.get_json())
        #         return Responder.success(data, message="Empresa criada com sucesso!")
        #     except Exception as e:
        #         return Responder.error("Não foi possível criar a empresa", 422)