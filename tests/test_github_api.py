from app.github_api import get_user_id
import os
from dotenv import load_dotenv
from pytest_mock import mock
import requests

load_dotenv() # Load env variables
CORE_API = 'https://api.github.com/'
ORG = os.getenv('GITHUB_ORGANISATION')
USERNAME = os.getenv('GITHUB_USERNAME')
PASSWORD = os.getenv('GITHUB_PASSWORD')


class TestsOffline:
    """
    Class for testing
    """
    def test_get_user_id(self):
        mock.patch('requests.get', return_value='123')
        result = get_user_id('kanticodes')
        print(result)
        assert False


class TestsOnline:
    """

    """
    def test_get_user_id_valid(self):
        result = get_user_id('kanticodes')
        print(result)
        assert result == 24612001
