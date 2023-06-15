from django.shortcuts import HttpResponse, render, redirect

from exportData.models import SqlList

from utils.bootstrap import BootStrap, BootStrapModelForm, BootStrapForm
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import random
import json


def sql_list(requests):
    """ SQL查询列表 """

    # 获取SQL查询列表数据，进行渲染
    # queryset = SqlList.objects.not_deleted.all().order_by("-id")
    queryset = SqlList.objects.all().order_by("-id")

    return render(requests, "sql_list.html", {"queryset": queryset})


class ModelFormSqlList(BootStrapModelForm):
    """ ModelFormSql表单 """

    class Meta:
        model = SqlList
        fields = "__all__"


@csrf_exempt
def sql_add(request):
    """ 新增 """
    if request.method == "POST":
        form = ModelFormSqlList(data=request.POST)
        if form.is_valid():
            form.save()
            Responses = {
                "code": 200,
                "status": True
            }
            return HttpResponse(json.dumps(Responses))
        Responses = {"errors": form.errors}
        return HttpResponse(json.dumps(Responses, ensure_ascii=False))
    form = ModelFormSqlList()
    return render(request, "sql_add.html", {"form": form})


@csrf_exempt
def sql_edit(request):
    """ 编辑 """
    sqlid = request.GET.get("sqlid")
    row_objecty = SqlList.objects.filter(id=sqlid).first()
    if not row_objecty:
        return HttpResponse("数据不存在,请刷新重试一下")

    if request.method == "GET":
        form=ModelFormSqlList(instance=row_objecty)
        return render(request, "sql_edit.html", {"form": form})

    form = ModelFormSqlList(data=request.POST, instance=row_objecty)
    if form.is_valid():
        form.save()
        return redirect('/export/sql/list')
    return render(request, "sql_edit.html", {"form": form})

def sql_delete(request):
    """ 删除  """
    sqlid = request.GET.get("sqlid")
    SqlList.objects.filter(id=sqlid).delete()
    return redirect('/export/sql/list')
