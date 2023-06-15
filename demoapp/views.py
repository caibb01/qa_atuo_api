import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")  # mysite表示项目名字
import django
django.setup()
import demoapp.models as Model

if __name__ == '__main__':
    c = Model.Apiinfo.objects.all()
    for i in c:
        print(i.Url)