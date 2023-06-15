import json

# 1、定义封装类
import jsonpath


class assertUtils:

    # 2、初始化数据，日志
    def __init__(self, TestCaseInfo, rsp):
        self.testCaseInfo = TestCaseInfo
        self.rsp = rsp

    # 3、code相等
    def assert_code(self, code, expected_code):
        """
    　　验证返回状态码
    　　:param code:rsp的code
    　　:param expected_code:期望的code，对应testCaseInfo的expectedStatusCode
    　　:return:
    　　"""
        try:
            assert int(code) == int(expected_code)
            print("HTTPcode断言正确，实际为： %s ，预期为：%s" %(code, expected_code))
        except Exception as e:
            print("code error,code is %s,expected_code is %s" % (code, expected_code))
            raise e

    # 4、body相等
    def assert_body(self, body, expectedBody):
        """
        验证返回结果内容相等
        :param body:
        :param expected_body:
        :return:
        """

        try:
            assert body == expectedBody
            print("断言正确" , (body, expectedBody))
        except Exception as e:
            print("body error,body is %s,expected_body is %s" % (body, expectedBody))
            raise e

    # 5、body包含
    def assert_in_body(self, body, expected_body):
        """
        验证返回结果是否包含期望的结果
        :param body:
        :param expected_body:
        :return:
        """

        try:
            assert expected_body == body
            print("断言正确", (body, expected_body))
        except Exception as e:
            print("不包含或者body是错误，body is %s,expected_body is %s" % (body, expected_body))
            raise e

    # 6、拼装给case使用
    def assertEntirety(self):
        self.assert_code(self.rsp.status_code, self.testCaseInfo.expectedStatusCode)
        # 全部断言
        if 0 == int(self.testCaseInfo.checkType):
            self.assert_body(self.rsp.text, self.testCaseInfo.expectedRespKeyInfo)
        # 只断言需要的值
        elif 1 == int(self.testCaseInfo.checkType):
            key_value = json.loads(self.testCaseInfo.expectedRespKeyInfo)
            for key_rsp in key_value:
                jsonRoute = key_rsp['jsonpath']
                exp = key_rsp['exp']
                jsonPathValue = jsonpath.jsonpath(json.loads(self.rsp.text), jsonRoute)[0]
                self.assert_in_body(exp, jsonPathValue)
        else:
            print("类型错误")


if __name__ == '__main__':
    exp = "TRUE"
    vody = {"result": "TRUE1"}
    expcode = 200
    rspcode = 200
    c = assertUtils().assert_in_body(vody, exp)
    d = assertUtils().assert_code(expcode, rspcode)
    print(c)
    print(d)
