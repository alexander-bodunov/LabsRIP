__author__ = 'Work'
import BaseClient
import requests
import json

class GetFriends(BaseClient.BaseClient):
    def __init__(self,method):
        self.BASE_URL="http://api.vk.com/method/"
        self.method=method#в переменной method хранится запрос к серверу(у нас то что нужно получить - пользователя или список друзей пользователя)
        self.http_method = 'get'

    def get_dict_data(self):#получаем словарь в результате запросов к серверу
        dict_data = json.loads(self.execute())#метод execute() объявлен в родительском классе BaseClient.Он вызывает метод _get_data()
        #метод _get_data() возвращает файл в формате json, а нам нужен словарь
        return dict_data

    def _get_data(self, method, http_method):
        response=requests.get(self.generate_url(method))#посылаем запрос на сервер
        return self.response_handler(response)#возвращаем только текстовую часть ответа

    def response_handler(self, response):#обработчик ответа
        text_part=response.text
        dict_data=json.loads(text_part)#в переменной dict_data содержится словарь, она нужна для проверки наличия ошибок в пределах данной функции
        if "error" in dict_data.keys():
            raise Exception
        return text_part
