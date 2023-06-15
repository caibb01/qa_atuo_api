# Generated by Django 4.1.7 on 2023-05-24 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('filecreate_at', models.DateField(default=None, verbose_name='文件生成时间')),
                ('file', models.FileField(max_length=1280, upload_to='export/', verbose_name='文件')),
            ],
        ),
        migrations.CreateModel(
            name='SqlList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bu', models.SmallIntegerField(choices=[(1, '天际'), (2, 'MTBG'), (3, '云ERP'), (4, '云采购'), (5, '产业BG'), (6, 'BG共享'), (7, '明源安全'), (8, '数字化中心')], default=2, verbose_name='业务线')),
                ('module', models.SmallIntegerField(choices=[(1, '客户专项'), (2, '线上反馈'), (3, '其它统计')], verbose_name='类型')),
                ('title', models.CharField(default='标题xxx', max_length=1280, verbose_name='标题')),
                ('describe', models.CharField(max_length=1280, verbose_name='SQL描述')),
                ('sqlquery', models.CharField(max_length=1280, verbose_name='SQL语句')),
                ('proposer', models.CharField(max_length=128, verbose_name='提出者')),
                ('query_start', models.DateField(verbose_name='SQL查询开始时间')),
                ('query_end', models.DateField(verbose_name='SQL查询结束时间')),
            ],
        ),
    ]