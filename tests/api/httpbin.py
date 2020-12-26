from one_apitest.api import BaseApi

class ApiHttpbinGet(BaseApi):
    url = "https://httpbin.org/get"
    params = {}
    method = "GET"
    headers = {"accept":"application/json"}
    proxies = {"https":"http://127.0.0.1:8888","http":"http//127.0.0.1:8888"}


class ApiHttpbinPost(BaseApi):
    url = "https://httpbin.org/post"
    method = "POST"
    proxies = {"https":"http://127.0.0.1:8888","http":"http//127.0.0.1:8888"}
    headers = {"accept":"application/json"} 
