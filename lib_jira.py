import requests
import json

from requests.auth import HTTPBasicAuth

class Jira:
    def __init__(self,host,user,pw,api_version='3'):
        self.user = 'paulo.souza@sensedata.com.br'
        self.pw = 'xAgPeVji4UURafRlU1fb97B0'
        self.api_version = api_version
    
    def get_data_from_jira(params):
        url = 'https://sensedata.atlassian.net/rest/api/2/search?jql=project="Squad Axé"&status!="Go production"&startAt=0'

        response = requests.get(
            url, auth=HTTPBasicAuth(self._user, self._pw)
        )
