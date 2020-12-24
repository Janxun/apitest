import requests

class BaseApi(object):

    url = ""
    params = {}
    method = "GET"
    headers = {}
    proxies = {}
    data = {}
    json = {}


    def set_params(self,**params):
        self.params = params
        return self

    def set_data(self,data):
        self.data = data
        return self
    
    def set_json(self,json_data):
        self.json = json_data
        return self

    def run(self):
        self.response = requests.request(
            self.method,
            self.url,
            params=self.params,
            headers=self.headers,
            data=self.data,
            json=self.json,
            proxies=self.proxies,
            verify=False
        )
        return self

    def validate(self,key,expected_value):
        value =self.response
        for _key in key.split("."):
            if isinstance(value,requests.Response):
                value = getattr(value,_key)
            elif isinstance(value,requests.structures.CaseInsensitiveDict):
                value = value[_key]
        assert value == expected_value
        return self
