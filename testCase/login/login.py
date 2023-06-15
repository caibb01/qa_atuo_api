import json
import os
import unittest

import jsonpath
import requests
from parameterized import parameterized

from utils.assertUtils import assertUtils
from utils.jsonPathUtils import jsonPatjUtils
from utils.parameterizeUtils import parameterizeUtils
from utils.runner import runner

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")  # mysite表示项目名字
import django

django.setup()
from demoapp import models


class Login(runner):

    @classmethod
    def setUpClass(cls) -> None:
        super(Login, cls).setUpClass()

    @parameterized.expand(parameterizeUtils().parameterizeUtils("login"))
    def test_login(self, TestCaseInfo):
        """登录"""
        self.runner("login", TestCaseInfo)


if __name__ == '__main__':
    unittest.main()
