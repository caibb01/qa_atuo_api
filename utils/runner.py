import json
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api-auto-test.settings")  # mysite表示项目名字
import django

django.setup()
import unittest
import requests
from demoapp import models
from utils.assertUtils import assertUtils
from utils.jsonPathUtils import jsonPatjUtils


class runner(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.jsonUtils = jsonPatjUtils()

    def runner(self,ApiId,TestCaseInfo):
        ApiInfoObj = models.Apiinfo.objects.filter(ApiId=ApiId).first()
        # 替换请求体变量
        requestBody = self.jsonUtils.replaceBody(json.loads(TestCaseInfo.requestData), jsonPatjUtils().extractDict)
        headers = self.jsonUtils.replaceBody(json.loads(ApiInfoObj.Headers), self.jsonUtils.extractDict)
        rsp = requests.post(url=ApiInfoObj.Url, json=requestBody, headers=headers)
        # 提取response 关键信息
        self.jsonUtils.extract(TestCaseInfo, rsp)
        # 断言
        assertUtils(TestCaseInfo, rsp).assertEntirety()
