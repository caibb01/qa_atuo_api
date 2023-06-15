import json
import os

import jsonpath

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api-auto-test.settings")  # mysite表示项目名字
import django

django.setup()

from demoapp import models


class jsonPatjUtils():

    def __init__(self):
        self.extractDict = {}

    def extract(self, TestCaseInfo, rsp):

        if TestCaseInfo.extractRespData is None:
            pass
        else:
            key_value = TestCaseInfo.extractRespData
            key_value_list = json.loads(key_value)
            for ibjects in key_value_list:
                jsonRoute = ibjects['jsonpath']
                paramName = ibjects['paramName']
                d = jsonpath.jsonpath(json.loads(rsp.text), jsonRoute)
                if paramName in ("token","Beartoken","Token","Jwttoken"):
                    self.extractDict[paramName] = "Bearer "+d[0]
                else:
                    self.extractDict[paramName] = d[0]
        return self.extractDict


    #废弃，用assertUtils里面的方法
    def assertRsp(self, ApiId, rsp):
        TestCaseInfoSet = models.TestCaseInfo.objects.filter(ApiId=ApiId)
        for TestCaseInfo in TestCaseInfoSet:
            key_value = json.loads(TestCaseInfo.expectedRespKeyInfo)
            checkType = TestCaseInfo.checkType
            if checkType == 1:
                for osjd in key_value:
                    jsonRoute = osjd['jsonpath']
                    exp = osjd['exp']
                    d = jsonpath.jsonpath(rsp, jsonRoute)
                    if exp == d[0]:
                        print("结果正确")
                    else:
                        print("对比错误")
            else:
                print(TestCaseInfo.expectedRespKeyInfo, "\n", json.dumps(rsp))
                p = json.dumps(rsp)
                q = json.loads(TestCaseInfo.expectedRespKeyInfo)
                s = json.dumps(q)
                if p == s:
                    print("结果正确")
                else:
                    print("对比错误")

    def replaceBody(self, targetDict, replaceDict):
        """
        :param targetDict: 字典类型，原始字典
        :param replaceDict: 字典类型，有替换字段的字典
        :return: 目标替换后的字典
        """
        for s in targetDict.values():
            try:
                replaceDict[s]
            except KeyError as e:
                print("")
            else:  # 只有try里面没报错的走这里
                #找到原始字典中key==替换字典中的value，然后替换掉
                for target in targetDict:
                    if targetDict[target] == s:
                        targetDict[target] = replaceDict[s]
        return targetDict


if __name__ == '__main__':
    a = {"code1": "$code", "expire": "$expire",
         "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdmF0YXIiOiJodHRwczovL3dld29yay5xcGljLmNuL3d3cGljLzc0NTc2OF9ySzlDdUItc1J0T2FTX3dfMTY3NzA1NjM2OC8wIiwiZG9tYWluX2FjY291bnQiOiJsaXlsNzIiLCJleHAiOjE2ODQ3NDAwMzksImlkIjo4ODIsIm9yaWdfaWF0IjoxNjg0MTM1MjM5LCJ6aF9uYW1lIjoi5p2O5bqU6b6ZIn0.VFJHur41ioElwC7nIkihps0MFWyvags3Aho-GQjzZ4M"}
    b = {"code": "$code", "expire": "shhada"}
    # c = json.loads(a)
    c = jsonPatjUtils().replaceBody(a, b)
    print(c)
