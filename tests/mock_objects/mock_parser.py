from abstracts.base_parser import BaseParser
from models.user import User


class MockParser(BaseParser):
    """
        Return a user with all blank fields except name, which is the url provided
    """

    def get_user(self, url: str):
        return User(name=url)