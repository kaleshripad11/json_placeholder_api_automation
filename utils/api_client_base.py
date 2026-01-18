import requests
from utils.config_reader import get_configs

conf = get_configs()

class Api_Client_Base:
    def __init__(self, base_url=conf["base_url"], default_headers=conf["headers"]):
        self.base_url = base_url
        self.headers = default_headers
        self.api_reponse = None
        
    def post_api(self, api_url, api_headers, body_data=None):
        self.api_response = requests.request("POST", url=api_url, data=body_data, headers=api_headers, json=None)
        return self.api_response
    
    def get_api(self, api_url, api_header, body_params=None):
        self.api_reponse = requests.request("GET", url=api_url, headers=api_header, params=body_params)
        return self.api_reponse