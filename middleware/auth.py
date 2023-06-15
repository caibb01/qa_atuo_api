from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, render, redirect


class AuthMiddlware(MiddlewareMixin):
    def process_request(self, request):
        # 判断不需要鉴权就能访问的url
        if request.path_info in ["/export/login/", "/export/image/code/"]:
            return
        # 判断用户是否登陆过，登陆过就会存在一个session
        info_dict = request.session.get("info")
        # session有值，那就通过这个中间件
        if info_dict:
            return
        # session没有值，无法通过这个中间件，下面这个是一个重定向操作
        return redirect("/export/login/")
        # return HttpResponse("未登录，请{}进入我们的系统吧！".format('<a href="/export/login">点击登录</a>'))

