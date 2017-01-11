__author__ = 'Work'
import BaseClient
import requests
import json

class GetUser(BaseClient.BaseClient):
    def __init__(self,method):
        self.BASE_URL="http://api.vk.com/method/"
        self.method=method
        self.http_method = 'get'

    def get_dict_data(self):#получаем словарь в результате запросов к серверу
        dict_data = json.loads(self.execute())
        return dict_data

    def _get_data(self, method, http_method):
        response=requests.get(self.generate_url(method))
        return self.response_handler(response)

    def response_handler(self, response):
        dict_data=json.loads(response.text)
        if "error" in dict_data.keys():
            raise Exception
        return response.text
