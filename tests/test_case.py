from tests.api.httpbin import *

def test_httpbin_get():
    ApiHttpbinGet().run()\
        .validate("status_code",200)\
        .validate("headers.server","gunicorn/19.9.0")\
        .validate("json().url","https://httpbin.org/get")\
        .validate("json().args",{})\
        .validate("json().headers.Accept",'application/json')

def test_httpbin_get_with_params():
    ApiHttpbinGet()\
        .set_params(abc=123,xyz=456)\
        .run()\
        .validate("status_code",200)\
        .validate("headers.server","gunicorn/19.9.0")\
        .validate("json().url","https://httpbin.org/get?abc=123&xyz=456")\
        .validate("json().headers.Accept",'application/json')

def test_httpbin_post():
    ApiHttpbinPost()\
        .set_json({"abc": 456})\
        .run()\
        .validate("status_code",200)\
        .validate("headers.server","gunicorn/19.9.0")\
        .validate("json().url","https://httpbin.org/post")\
        .validate("json().headers.Accept",'application/json')








# def test_version():
#     from one_apitest import __version__
#     assert isinstance(__version__,str)

# def test_httpbin_get():
    # resp = requests.get(
    #     https://httpbin.org/get",
    #     headers = {"accept":"application/json"}
    # )
    # assert resp.status_code == 200
    # assert resp.headers["server"] == "gunicorn/19.9.0"
    # assert resp.json()["url"] == "https://httpbin.org/get"


# def test_httpbin_get_with_params():
#     resp = requests.get(ApiHttpbinPost.url,
#         params={"abc":123},
#         headers={"accept":"application/json"}
#     )
#     assert resp.status_code == 200
#     assert resp.headers["server"] == "gunicorn/19.9.0"

# def test_httpbin_post():
#     resp = requests.post(
#         "https://httpbin.org/post",
#         headers={"accept":"application/json"},
#         json={"abc": 123}
#     )
#     assert resp.status_code == 200
#     assert resp.headers["server"] == "gunicorn/19.9.0"
#     assert resp.json()["url"] == "https://httpbin.org/post" 
#     assert resp.json()["json"]["abc"] == 123