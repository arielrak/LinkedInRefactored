from abc import ABC, abstractmethod

from models.user import User


class BaseDAL(ABC):
    @abstractmethod
    def add_user(self, user: User) -> User:
        pass

    @abstractmethod
    def query(self, query_terms_as_user_object: User) -> [User]:
        pass