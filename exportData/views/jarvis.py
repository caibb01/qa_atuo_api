# import requests
# from django.shortcuts import render, HttpResponse
# import jsonpath
#
#
# def jarvisrenew(self=None):
#     """ 贾维斯续签 """
#     # 获取登陆的Token
#     get_tokendata = {
#         "url": "",
#         "headers": {
#             "content-type": "application/json;charset=UTF-8",
#             "origin": "https://..cn",
#             "referer": ""
#         },
#         "content": {
#             "username": "",
#             "password": "",
#             "type": "account"
#         }
#     }
#     result = requests.post(url=get_tokendata["url"], json=get_tokendata["content"],
#                            headers=get_tokendata["headers"])
#     token = jsonpath.jsonpath(result.json(), '$..token')
#     # token = result.json()["token"]
#     # token = "Token " + token
#     token = "Token " + token[0]
#     # 请求贾维斯续签功能
#     get_jsnewdata = {
#         "url": "",
#         "headers": {
#             "content-type": "application/json;charset=UTF-8",
#             "origin": "https://..cn",
#             "referer": "https://..cn/m/application/applyboard/service?node_id=2",
#             "Authorization": token
#         },
#     }
#     result_jarvis = requests.post(url=get_jsnewdata["url"],
#                                   headers=get_jsnewdata["headers"])
#     # 断言续签结果
#     try:
#         if result_jarvis.json()["status"].__contains__("Success"):
#             return HttpResponse("续签成功")
#
#     except:
#         return HttpResponse(result_jarvis.text)
#
#
# if __name__ == '__main__':
#     jarvisrenew()
