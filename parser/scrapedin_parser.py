from Naked.toolshed.shell import muterun_js
import yaml

from abstracts.base_parser import BaseParser
from models.user import User


class LinkedInParser(BaseParser):

    # Accepts URL of a public LinkedIn page
    def get_user(self, url):
        print("Fetching data. Please wait...")

        raw_data = muterun_js('/users/ariel/programming/LinkedInRefactored/parser/scraper.js', url)

        print("Done fetching data.")

        # Handle error executing script
        if raw_data.exitcode != 0:
            print(raw_data.exitcode)
            print(raw_data.stderr)
            raise RuntimeError("Error executing node script: ", raw_data.exitcode)
            return

        raw_data = raw_data.stdout
        data = self._clean_data(raw_data)
        self._find_useful_fields(data)

        return User(name=self._name,
                    title=self._title,
                    position=self._current_position,
                    summary=self._summary,
                    skills=self._skills,
                    experience=self._experience,
                    education=self._education)


    def _clean_data(self, raw_data):
        raw_data = raw_data.decode('utf-8')
        raw_data = raw_data.replace("\'", "\"")
        raw_data = raw_data.replace("\n", "")
        raw_data = raw_data.replace("\'", "\"")
        raw_data = raw_data.replace("\xe2\x80\x93", "-")
        raw_data = yaml.load(raw_data, Loader=yaml.FullLoader)
        return raw_data

    def _find_useful_fields(self, data):
        self._name = str(self._find('name', data))
        self._title = str(self._find('positions', data)[0]["title"])
        self._current_position = str(self._find('positions', data)[0])
        self._summary = str(self._find('summary', data))
        self._skills = str(self._find('skills', data))
        self._experience = str(self._find('positions', data))
        self._education = str(self._find('educations', data))

    # Recursive method for finding the first instance of a key in a nested dict
    # Adapted from Stack Overflow:s https://tinyurl.com/y4qmzdj3
    def _find(self, target_key, dictionary):
        if target_key in dictionary: return dictionary[target_key]
        for _, value in dictionary.items():
            if isinstance(value, dict):
                return self._find(target_key, value)