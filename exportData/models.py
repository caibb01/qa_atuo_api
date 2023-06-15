from django.db import models
from django.db.models.query import QuerySet

# 自定义软删除查询基类
class SoftDeletableQuerySetMixin(object):
    """
    QuerySet for SoftDeletableModel. Instead of removing instance sets
    its ``is_deleted`` field to True.
    """
    def delete(self):
        """
        Soft delete objects from queryset (set their ``is_deleted``
        field to True)
        """
        self.update(is_deleted=True)


class SoftDeletableQuerySet(SoftDeletableQuerySetMixin, QuerySet):
    pass


class SoftDeletableManagerMixin(object):
    """
    Manager that limits the queryset by default to show only not deleted
    instances of model.
    """
    _queryset_class = SoftDeletableQuerySet

    def get_queryset(self):
        """
        Return queryset limited to not deleted entries.
        """
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints

        return self._queryset_class(**kwargs).filter(is_deleted=False)


class SoftDeletableManager(SoftDeletableManagerMixin, models.Manager):
    pass

# 自定义软删除抽象基类
class SoftDeletableModel(models.Model):

    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True  # 成功发送Signal信号需要将abstract设置为true
        auto_created = False

    objects = SoftDeletableManager()

    def delete(self, using=None, soft=True, *args, **kwargs):
        if soft:
            self.is_deleted = True
            self.save(using=using)
        else:
            return super(SoftDeletableModel, self).delete(using=using, *args, **kwargs)
# Create your models here


class SqlList(models.Model):
    bu_choices = (
        (1, "天际"),
        (2, "MTBG"),
        (3, "云ERP"),
        (4, "云采购"),
        (5, "产业BG"),
        (6, "BG共享"),
        (7, "明源安全"),
        (8, "数字化中心"),

    )
    bu = models.SmallIntegerField(verbose_name="业务线", choices=bu_choices, default=2)
    module_choices = (
        (1, "客户专项"),
        (2, "线上反馈"),
        (3, "其它统计")
    )
    module = models.SmallIntegerField(verbose_name="类型", choices=module_choices)
    title = models.CharField(verbose_name="标题", max_length=1280, default="标题xxx")
    describe = models.CharField(verbose_name="SQL描述", max_length=1280)
    sqlquery = models.TextField(verbose_name="SQL语句")
    proposer = models.CharField(verbose_name="提出者", max_length=128)
    query_start = models.DateField(verbose_name="SQL查询开始时间")
    query_end = models.DateField(verbose_name="SQL查询结束时间")



class DataFile(models.Model):
    """   文件  """
    name = models.CharField(verbose_name="名称", max_length=32)
    filecreate_at = models.DateTimeField(verbose_name="文件生成时间", default=None)
    file = models.FileField(verbose_name="文件", max_length=1280, upload_to="exportdata/")
