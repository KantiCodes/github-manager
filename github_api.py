import os

import requests
from dotenv import load_dotenv
import json

load_dotenv() # Load env variables
CORE_API = 'https://api.github.com/'
ORG = os.getenv('GITHUB_ORGANISATION')
USERNAME = os.getenv('GITHUB_USERNAME')
PASSWORD = os.getenv('GITHUB_PASSWORD')
print(USERNAME,PASSWORD)
print (f"this is the org {ORG}")

def get_user_id(github_username):
    """
    Returns a github user id

    :param github_username: username of the github account
    :return: status of the request
    """
    url = CORE_API+ f"users/{github_username}"
    response = requests.get(url,auth=(USERNAME, PASSWORD))

    print(response)
    if response.status_code == 200:

        return response.json()['id']

    return None

def get_team_id(team):
    """
    Returns a github team id

    :param team:
    :return:
    """

    url = CORE_API + f"orgs/{ORG}/teams/{team}"
    response = requests.get(url,auth=(USERNAME, PASSWORD))

    if response:
        return response.json()['id']
    else:
        return False
    print(url)

def invite_user(user_id, team_ids):
    """

    :param team_ids:
    :param user_id:
    :return:
    """
    url = CORE_API + f"orgs/{ORG}/invitations"
    body = {'invitee_id':user_id,'team_ids':team_ids}

    response = requests.post(url, data=json.dumps(body), auth=(USERNAME,PASSWORD))
    if response.status_code == 201:
        return response
    else:
        return None

