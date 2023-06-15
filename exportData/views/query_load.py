# Django基本包
from django.shortcuts import HttpResponse, render, redirect
from django.db import connections
from string import Template
import MySQLdb
# python内置包
import time
import openpyxl
import os
# 数据库模型包
from exportData.models import SqlList, DataFile

from django.db import connection, ProgrammingError


# 返回数据是元组的
def django_sql(sql, database_name=None, data=None):
    if database_name:
        connection = connections[database_name]
    else:
        connection = connections['default']
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(sql, data)
        else:
            cursor.execute(sql)
        raws = cursor.fetchall()
        raws_list = []
        fieldlist = []
        if cursor.rowcount > 0:  # TODO：异步处理，成功后会有消息通知最好
            for i in list(raws):
                raws_list.append(list(i))
            col = cursor.description
            for i in col:
                fieldlist.append(i[0])
    except:
        connection.rollback()
        raws = None
    connection.commit()
    cursor.close()
    if raws is None:
        raws_list = "False"
        fieldlist = "False"
        return raws_list, fieldlist
    return raws_list, fieldlist


now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())


def query_sums(request):
    """ 查询结果下载 """
    # 获取用户传入的ID
    uid = request.GET.get("id")
    # 获取数据库的SQL查询语句,不存在直接退出提示用户该查询语句不存在，劝你返回。
    exists = SqlList.objects.filter(id=uid).exists()
    if exists:
        file_object = SqlList.objects.filter(id=uid).first()
        query_sql = file_object.sqlquery
        # 时间字段参数化
        get_query_time = {
            "END_TIME": "'" + file_object.query_end.strftime('%Y-%m-%d') + "'",
            "START_TIME": "'" + file_object.query_start.strftime('%Y-%m-%d') + "'",
        }
        query_sql = Template(query_sql).substitute(get_query_time)
        # 获取SQL查询结果和对应返回的字段
        raws_list, fieldlist = django_sql(sql=query_sql, database_name='cm_rep_test')
        if raws_list != "False":
            # 如果是查询语句，即fieldlist有值则创建工作簿写入文件，否则进行别的操作，目前先重定向至列表页。
            if raws_list:
                # 读取到内容，写入到文件中并获取文件的路径写入数据库 希望写到这个位置，但是数据库不需要存media

                file_path = os.path.join("media", "exportdata", now_time + file_object.title + ".xlsx")
                db_file_path = os.path.join("exportdata", now_time + file_object.title + ".xlsx")
                DataFile.objects.create(name=file_object.title,
                                        filecreate_at=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
                                        file=db_file_path)
                # 打开一个新的工作簿
                workbook = openpyxl.Workbook()
                # 创建一个新的工作表
                worksheet = workbook.active
                # 写入文件内容
                worksheet.append(fieldlist)
                for row in raws_list:
                    worksheet.append(row)
                    # 保存写入的内容至指定的地址
                    workbook.save(file_path)
                    # result_content = {
                    #     "file_path": file_path,
                    #     'get_host': request.get_host()
                    # }
                # return redirect((get_host+"/"+ file_path))
                # return HttpResponse("""<a href="{}/{}"></a>""".format(result_content["get_host"],result_content["file_path"]))
                return redirect('/export/file/list')
            return HttpResponse("该查询不符合规范，请返回页面重试")
        return HttpResponse("该查询不符合规范，请返回页面-操作-编辑-SQL语句页面检查后重试")
    return HttpResponse("该查询已不存在，请返回页面重试")
