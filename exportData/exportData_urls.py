from django.urls import path
from exportData.views import sqllist, query_load, jarvis, filelist,login


urlpatterns = [

    # 登陆
    path('login/', login.loginpy),
    path('logout/', login.logout),
    path('image/code/', login.image_code),

    # SQL清单
    path('sql/list/', sqllist.sql_list),
    path('sql/add/', sqllist.sql_add),
    path('sql/edit/', sqllist.sql_edit),
    path('sql/delete/', sqllist.sql_delete),

    # 文件列表
    path('file/list/', filelist.file_list),
    path('file/<int:file_id>/load/', filelist.file_download),
    path('file/<int:file_id>/preview/', filelist.preview_files),
    # path('file/preview/', filelist.preview_files),

    # SQL查询语句结果下载
    path('query_load/', query_load.query_sums),


    # 贾维斯续签
    path('jarvis/renew/', jarvis.jarvisrenew),
]
