from abc import ABC, abstractmethod

from models.user import User

class BaseParser(ABC):

    @abstractmethod
    def get_user(self, url: str) -> User:
        pass