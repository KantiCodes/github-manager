import os

import requests
from dotenv import load_dotenv
import json
load_dotenv() # Load env variables
CORE_API = 'https://api.github.com/'
ORG = os.getenv('GITHUB_ORGANISATION')
USERNAME = os.getenv('GITHUB_USERNAME')
PASSWORD = os.getenv('GITHUB_PASSWORD')


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

def get_team_id(team_name):
    """
    Function returns time id based on the team name

    Function uses GitHub API and returns the ID for requested team

    :param team_name: the name of team
    :return: id of the team
    """

    url = CORE_API + f"orgs/{ORG}/teams/{team_name}"
    response = requests.get(url,auth=(USERNAME, PASSWORD))

    if response:
        return response.json()['id']
    else:
        return f"team {team_name} not found"


def invite_user(user_id, team_ids):
    """
    Function invites user to the specific teams

    Function uses GitHub API to invite user with id specified in the function parameters to specific teams

    :param team_ids: list of ids to which the user is supposed to get invited
    :param user_id: the id of the user being invite
    :return: status of the invitation
    """
    url = CORE_API + f"orgs/{ORG}/invitations"
    body = {'invitee_id':user_id,'team_ids':team_ids}

    response = requests.post(url, data=json.dumps(body), auth=(USERNAME,PASSWORD))
    if response.status_code == 201:
        return response
    else:
        return False
