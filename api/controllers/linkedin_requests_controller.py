from flask import Blueprint, request
from api.services.linkedin_requests_service import LinkedInRequestsService

linkedin_requests = Blueprint('linkedin_requests', __name__)
_linkedin_requests_service: LinkedInRequestsService = None

def init_linkedin_requests(linkedin_requests_service: LinkedInRequestsService):
    global _linkedin_requests_service
    _linkedin_requests_service = linkedin_requests_service

@linkedin_requests.route('/query', methods=['GET'])
def execute_query():
    return _linkedin_requests_service.handle_query(dict(request.args))

@linkedin_requests.route('/add', methods=['GET'])
def add_user():
    # Make sure a url was specified
    if request.args.get('url') is None:
        return "Please specify a url parameter"

    return _linkedin_requests_service.handle_add_user(request.args.get('url'))

@linkedin_requests.route('/add/params', methods=['GET'])
def add_user_by_params():
    return _linkedin_requests_service.handle_add_user_by_params(dict(request.args))

