

# Create your models here.
from django.db import models


class BaseModel(models.Model):
    """
        数据库表公共字段
        """
    objects = models.Manager()
    createTime = models.DateTimeField(blank=True, auto_now=True)
    updateTime = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        # abstract = True：为抽象模型类，用于其他模型类继承，数据库迁移时不会创建ModelBase表
        abstract = True
        verbose_name = '公共字段表'
        db_table = 'BaseModel'



class Apiinfo(BaseModel):
    id = models.AutoField(primary_key=True)
    ApiId = models.CharField(max_length=255, verbose_name="接口英文名", blank=False)
    ApiName = models.CharField(max_length=255, verbose_name="接口中文名", blank=False)
    Url = models.URLField(blank=False)
    Type = models.CharField(max_length=255, verbose_name="接口类型，GET，POST，UPDATE等", blank=False)
    Headers = models.TextField(blank=False, verbose_name="'请求头，里面放json串")
    Auth = models.TextField(blank=True, verbose_name="'是否鉴权，只做标识作用")

    class Meta:
        db_table = 'apiInfo'
        verbose_name = '接口详情'
        verbose_name_plural = verbose_name



class TestCaseInfo(BaseModel):
    id = models.AutoField(primary_key=True)
    caseId = models.CharField(max_length=255, unique=True, db_index=True)
    caseRemark = models.CharField(max_length=255, unique=True, db_index=True)
    ApiId = models.CharField(max_length=255, unique=True, db_index=True)
    requestData = models.TextField()
    expectedStatusCode = models.TextField(verbose_name="期望的状态码")
    extractRespData = models.TextField()
    expectedRespKeyInfo = models.CharField(max_length=255, null=True, blank=True)
    checkType = models.CharField(max_length=255, default=None, choices=[('0', '校验成功'), ('1', '校验失败')])
    class Meta:
        db_table = 'testCaseInfo'
        verbose_name = '接口case详情'
        verbose_name_plural = verbose_name

class SqlCheck(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255, default=None, choices=[('0', '后置校验'), ('1', '后置校验')])
    sql_id = models.IntegerField(default=None, null=True)
    case_id = models.IntegerField(default=None, null=True)
    sql = models.CharField(max_length=255, default=None, null=True)
    expected = models.CharField(max_length=255, default=None, null=True)
    actual = models.CharField(max_length=255, default=None, null=True)
    check_result = models.CharField(max_length=255, default=None, choices=[('1', '校验失败'), ('0', '校验通过')], null=True)

    class Meta:
        db_table = 'sqlCheck'
        verbose_name = 'sql校验'
        verbose_name_plural = verbose_name
