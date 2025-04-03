from flask import Flask
from flask_cors import CORS
from routes import routes
import services as Controller
import threading

WebServer = Flask(__name__)
CORS(WebServer)
ControllerThread = threading.Thread(target=Controller.State.run)
ControllerThread.start()

routes(Controller.State, WebServer)

if __name__ == "__main__":
    WebServer.run(debug=True)
