from flask import request

def routes(Server, WebService):
    
    @WebService.route("/")
    def FlaskMain():
        pass
    
    @WebService.route("/envoriment/<string:id>", methods=["GET"])
    def FlaskEnvoriment(id):
        return Server.envoriment(id)
    
    @WebService.route("/place/<string:id>", methods=["GET"])
    def FlaskPlace(id):
        return Server.place(id)
    
    @WebService.route("/places", methods=["GET"])
    def FlaskPlaces():
        return Server.places()
    
    @WebService.route("/create-place", methods=["POST"])
    def FlaskCreatePlace():
        form = request.get_json()
        return Server.create_place(form)
    
    @WebService.route("/create-local-enterprise", methods=["POST"])
    def FlaskCreateLocalEnterprise():
        form = request.get_json()
        return Server.create_local_enterprise(form)