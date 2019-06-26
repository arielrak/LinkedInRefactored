from flask import Flask
from waitress import serve

from config import config
from api.controllers.linkedin_requests_controller import linkedin_requests, init_linkedin_requests
from api.services.linkedin_requests_service import LinkedInRequestsService

class APIServer:
    def __init__(self, linkedin_requests_service: LinkedInRequestsService):
        self._linkedin_requests_service: LinkedInRequestsService = linkedin_requests_service
        self._app: Flask = Flask(__name__)

        self._init()

    def _init(self):
        self._app.register_blueprint(linkedin_requests, url_prefix='/api')
        init_linkedin_requests(self._linkedin_requests_service)

    @property
    def app(self) -> Flask:
        return self._app

    def run(self):
        host = config["api_host"]
        port = config["api_port"]
        serve(self._app, host=host, port=port)



