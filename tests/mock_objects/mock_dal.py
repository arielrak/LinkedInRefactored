from abstracts.base_dal import BaseDAL
from models.user import User


class MockDAL(BaseDAL):
    """
        MockDAL that returns exactly the information given to it
    """


    def add_user(self, user: User) -> User:
        return user


    def query(self, query_terms_as_user_object: User) -> [User]:
        yield query_terms_as_user_object