import json
import unittest

from api.services.linkedin_requests_service import LinkedInRequestsService
from models.user import User
from tests.mock_objects.mock_dal import MockDAL
from tests.mock_objects.mock_parser import MockParser


class TestLinkedInRequestsService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        mock_dal = MockDAL()
        mock_parser = MockParser()
        cls._linkedin_requests_service = LinkedInRequestsService(mock_dal, mock_parser)

    def test_wellformed_query(self):

        args = {
            "name" : "Ariel",
            "skills" : "testing"
        }

        response = self._linkedin_requests_service.handle_query(args)
        response = json.loads(response)[0]

        assert response["name"] == "Ariel"
        assert response["skills"] == "testing"

    def test_malformed_query(self):

        args = {
            "name" : "Ariel",
            "junk" : "junk"
        }

        response = self._linkedin_requests_service.handle_query(args)
        response = json.loads(response)[0]

        assert(response["name"] == "Ariel")
        assert("junk" not in response)

    def test_add_user(self):

        response = self._linkedin_requests_service.handle_add_user("test url")
        response = json.loads(response)

        assert(response["name"] == "test url")

    def test_wellformed_add_by_params(self):

        args = {
            "name": "Ariel",
            "skills": "testing"
        }

        response = self._linkedin_requests_service.handle_add_user_by_params(args)
        response = json.loads(response)

        assert response["name"] == "Ariel"
        assert response["skills"] == "testing"

    def test_malformed_add_by_params(self):

        args = {
            "name": "Ariel",
            "junk": "junk"
        }

        response = self._linkedin_requests_service.handle_add_user_by_params(args)
        response = json.loads(response)

        assert (response["name"] == "Ariel")
        assert ("junk" not in response)


if __name__ == '__main__':
    unittest.main()