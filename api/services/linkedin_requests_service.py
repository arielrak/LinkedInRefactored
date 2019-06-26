from dataclasses import asdict

from abstracts.abstract_dal import BaseDAL
from abstracts.abstract_parser import BaseParser
from models.user import User
import json


class LinkedInRequestsService:
    def __init__(self, dal: BaseDAL, parser: BaseParser):
        self._dal = dal
        self._parser = parser
        pass

    def handle_query(self, args: dict):
        args = self._remove_invalid_args(args)

        query_terms_as_user = User(**args)
        list_of_users = []
        # Put all query results in list
        for result in self._dal.query(query_terms_as_user):
            list_of_users.append(asdict(result))

        return json.dumps(list_of_users)

    def handle_add_user(self, url: str):
        print(url)
        try:
            user = self._parser.get_user(url)
            self._dal.add_user(user)
            return json.dumps(asdict(user))
        except Exception as e:
            e = str(e)
            return json.dumps("An error occurred: " + e)

    def handle_add_user_by_params(self, args: dict):
        args = self._remove_invalid_args(args)

        params_as_user = User(**args)
        return json.dumps(asdict(self._dal.add_user(params_as_user)))

    def _remove_invalid_args(self, args: dict):
        valid_args = ["name", "title", "position", "summary", "skills", "experience", "education"]

        for key in args.copy().keys():
            if key not in valid_args:
                args.pop(key, None)

        return args