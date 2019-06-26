import unittest

from parser.scrapedin_parser import LinkedInParser


class TestBaseParser(unittest.TestCase):

    def test_sample_url(self):
        url = "https://www.linkedin.com/in/hwicheong/"
        parser = LinkedInParser()
        user = parser.get_user(url)

        assert user.name == "Cookie M."
        assert user.summary == "I eat cookies"

if __name__ == '__main__':
    unittest.main()