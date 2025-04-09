from flask import jsonify

class Responder:
    
    @staticmethod
    def success(data):
        return jsonify({
            "success": True,
            "data": data
        }), 200

    @staticmethod
    def error(message, code=400):
        return jsonify({
            "success": False,
            "error": message
        }), code