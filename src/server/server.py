"""
Outpost Studio: Servidor de Gerenciamento de Dados

Camada de inicialização do servidor.

Autor: Lucas dos Santos Souza
Criado em: 04/04/2025
"""

import utils, router

from flask import Flask
from flask_cors import CORS # type: ignore


service_web_server = Flask(__name__)
CORS(service_web_server)


if __name__ == "__main__":
    
    utils.Preferences().load('preferences.json').apply()
    router.Routes().bind(service_web_server)
    
    service_web_server.run(debug=True)
