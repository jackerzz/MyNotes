from celery import Celery

'''
    1、创建实例 Celery('demo')  
    2、通过config_from_object()加载配置文件
'''
app = Celery('demo')
app.config_from_object('celery_app.celeryconfig')
