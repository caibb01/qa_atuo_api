from django.shortcuts import render, redirect, HttpResponse
from io import BytesIO
from django import forms

# from utils.encrypt import md5
from utils.bootstrap import BootStrapForm
from utils.code_img import check_code


#
#

class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="请输入用户名",
        widget=forms.TextInput,
        required=True

    )

    password = forms.CharField(
        label="请输入密码",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )

    code = forms.CharField(
        label="请输入验证码",
        widget=forms.TextInput(),
        required=True
    )
    # def clean_password(self):
    #     password = self.cleaned_data.get("password")
    #     return md5(password)


def login(request):
    form = LoginForm

    # 判断请求为查询，则直接返回列表信息即可
    if request.method == "GET":
        return render(request, "login.html", {"form": form})

    form = LoginForm(data=request.POST)

    # user_input_code = form.cleaned_data.pop("code")
    # print(user_input_code)
    # print(form.cleaned_data)
    api_username = form.username
    api_password = form.password

    # 验证成功，获取到的用户名和密码

    if form.is_valid():
        userinput_code = form.cleaned_data.pop("code")
        # 验证码的校验
        code = request.session.get("image_code", '')
        if userinput_code.upper() != code.upper():
            form.add_error("code", "验证码错误")
            return render(request, "login.html", {"form": form})

        # 去数据库验证用户名和密码是否正确，获取用户对象、None
        admin_object = Admin.objects.filter(**form.cleaned_data).first()  # 判断用户在数据库是否存在
        # 验证用户是否存在，不存在则报错
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, "login.html", {"form": form})

        # 用户名和密码与数据库匹配上的话
        # 网站生成随机字符串；写到用户浏览器的cookie中，在写入到session中
        request.session["info"] = {'id': admin_object.id, 'username': admin_object.username, }
        request.session.set_expiry(60 * 60 * 24 * 7)  # 设置登陆成功后的免登录时间，7天

        return redirect("/export/sql/list/")

    return render(request, "login.html", {"form": form})


def image_code(request):
    img,code_string = check_code()  # 使用生成图片验证码的图片和code
    print(img,code_string)
    # 写入到自己的session中以便后续获取验证码再进行校验
    request.session['image_code'] = code_string
    # 給验证码的session设置60s超时，注意这里设置了，等一下整一个session都是60秒
    request.session.set_expiry(60)

    stream = BytesIO()  # 需要借用到一个内存动态展示到页面上
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())  # 使用到页面上


def logout(request):
    request.session.clear()
    return redirect('/export/login/')


import requests


def loginpy(request):
    if request.method == 'GET':
        return render(request, "login.html")


    # 获取用户输入账号密码进行校验
    info_name = request.POST.get("name")
    info_password = request.POST.get("password")
    print(info_password)

    def ekp_result():
        """获取EKP结果，Ture有权限进入系统，无则代表无权限 """
        # 获取EKP_token
        if info_password =='':
            return "False"
        token_data = {
            "url": 'https://mdcmip.mingyuanyun.com/MIPApiAuth/Jwt',
            "json": {"AppKey": "8e98868bf67845cba9044d8616eb8a89",
                     "AppSecret": "5c58ff9c694f4b6f82ca4d66007ece76"
                     },
            "header": {'Content-Type': 'application/json'
                       }
        }
        token_rusult = requests.post(url=token_data["url"], json=token_data["json"],
                                     headers=token_data["header"]).json()
        user_token = token_rusult["access_token"]

        # 获取Ekp返回：Ture or Flase
        ekp_data = {
            "url": "https://mdcmip.mingyuanyun.com/apigate/UserLoginForDomain",
            "json": {"sUserName": "{}".format(info_name),
                     "sPassWord": "{}".format(info_password)},
            "header": {
                "Authorization": "Bearer {}".format(user_token)
            }
        }

        ekp_result = requests.post(url=ekp_data["url"], json=ekp_data["json"], headers=ekp_data["header"]).text
        return ekp_result
    ekpresult = ekp_result()
    print(ekpresult)
    if ekpresult == 'True':
        request.session["info"] = {'username': info_name}
        request.session.set_expiry(60 * 60 * 24 * 7)  # 设置登陆成功后的免登录时间，7天

        # 验证码的校验
        userinput_code = request.POST.get("code")
        code = request.session.get("image_code", '')
        if userinput_code.upper() != code.upper():
            err_code_msg = "验证码错误"
            return render(request, "login.html", {"err_msg": err_code_msg})
        return redirect("/export/sql/list/")
    err_msg = "用户名或密码错误"
    return render(request, "login.html", {"err_msg": err_msg})


def logout(request):
    """  退出登陆  """
    request.session.clear()
    return redirect('/export/login/')
