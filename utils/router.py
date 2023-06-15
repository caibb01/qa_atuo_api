class DemoRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == "exportdata":
            print(model._meta,type(model._meta),"read")
            return "default"

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "exportdata":
            return "cm-rep-test"
if __name__ == '__main__':
    db_for_read()
