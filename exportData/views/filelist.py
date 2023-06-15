# Django包
from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
# 实现下载包
from django.http import HttpResponse, Http404, FileResponse

# 导入models模型包
from exportData.models import SqlList, DataFile
import os


def file_list(request):
    queryset = DataFile.objects.all().order_by("-id")
    return render(request, "file.html", {"queryset": queryset})


def file_download(request, file_id):
    # 根据文件的标识符或其他参数获取文件对象
    file_object = get_object_or_404(DataFile, id=file_id)

    # 获取文件的路径或文件对象
    file_path = file_object.file

    # 打开文件并创建 FileResponse 对象
    # file = open(file_path, 'rb')
    response = FileResponse(file_path)

    # 设置响应头，指定文件的 MIME 类型
    response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    # 设置响应头，指定文件的名称
    import urllib.parse
    filename = urllib.parse.quote(file_object.name + '.xlsx')
    response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    return response


# def preview_files(request):
#     file_path = os.path.join('media', 'exportdata')
#     file_list = os.listdir(file_path)  # 获取文件夹中的文件列表
#     # 将文件列表传递给模板
#     return render(request, 'preview_files.html', {'file_list': file_list})

import pandas as pd
def preview_files(request, file_id):
    # 获取用户要预览的ID、标题及文件存放地址
    row_object = DataFile.objects.filter(id=file_id).first()
    files_path = row_object.file
    # 使用pandas读取Excel文件
    df = pd.read_excel(files_path)

    # 在视图函数中进行数据处理,以便在JavaScript中使用
    table_data = df.fillna('-').astype(str).values.tolist()  # 将数据转换为字符串列表

    column_headers = df.columns.tolist()  # 获取列标题列表
    content = {
        'table_data': table_data,
        'column_headers': column_headers,
        'files_name': row_object.name
    }
    # 渲染模板并将数据传递给模板
    return render(request, 'preview_files.html', content)
