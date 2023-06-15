import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api-auto-test.settings")  # mysite表示项目名字
import django

django.setup()
from demoapp import models


class parameterizeUtils():


    def parameterizeUtils(self, ApiId) -> []:
        TestCaseInfoSet = models.TestCaseInfo.objects.filter(ApiId=ApiId)
        caseList = []
        # set 转换为 list，不用list（）强转，用for循环转，里面还是testCaseinfo 对象
        for i in TestCaseInfoSet:
            caseList.append(i)
        return caseList


if __name__ == '__main__':
    list = parameterizeUtils().parameterizeUtils("login")
    for i in list:
        print(i.caseRemark)
