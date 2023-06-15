import json
import os
import unittest

from utils.assertUtils import assertUtils
from utils.runner import runner

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api-auto-test.settings")  # mysite表示项目名字
import django

django.setup()
import requests
from parameterized import parameterized

from utils.jsonPathUtils import jsonPatjUtils

from demoapp import models
from utils.parameterizeUtils import parameterizeUtils


class ekp(runner):

    @classmethod
    def setUpClass(cls) -> None:
        cls.jsonUtils = jsonPatjUtils()

    @parameterized.expand(parameterizeUtils().parameterizeUtils("Jwt"))
    def test_ekp_jwt(self, TestCaseInfo):
        self.runner("Jwt", TestCaseInfo)

    @parameterized.expand(parameterizeUtils().parameterizeUtils("GetAllValidUserList"))
    def test_getAllValidUserList(self, TestCaseInfo):
        self.runner("GetAllValidUserList", TestCaseInfo)

    @parameterized.expand(parameterizeUtils().parameterizeUtils("GetBusinessUnitAllCol"))
    def test_getBusinessUnitAllCol(self, TestCaseInfo):
        self.runner("GetBusinessUnitAllCol", TestCaseInfo)

    @parameterized.expand(parameterizeUtils().parameterizeUtils("GetMyUserAllCol"))
    def test_getMyUserAllCol(self, TestCaseInfo):
        self.runner("GetMyUserAllCol", TestCaseInfo)

    @parameterized.expand(parameterizeUtils().parameterizeUtils("UserLoginForDomain"))
    def test_userLoginForDomain(self, TestCaseInfo):
        self.runner("UserLoginForDomain", TestCaseInfo)


if __name__ == '__main__':
    unittest.main()
