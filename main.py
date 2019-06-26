from config import config
from api.api_server import APIServer
from api.services.linkedin_requests_service import LinkedInRequestsService
from database.sql_alchemy_dal import SQLAlchemyDAL
from parser.scrapedin_parser import LinkedInParser

def main():
    dal = SQLAlchemyDAL("sqlite:////"+config["db_path"])
    parser = LinkedInParser()

    # Initial dependency injection
    linkedin_requests_service = LinkedInRequestsService(dal, parser)
    api_server = APIServer(linkedin_requests_service)

    api_server.run()

if __name__ == '__main__':
    main()