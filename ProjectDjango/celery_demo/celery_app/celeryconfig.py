'''
定时任务&&异步任务
    server端启动命令(异步通用)
        celery -A celery_app worker --loglevel=info
    启动命令client端
        celery beat -A celery_app
'''

BROKER_URL = 'redis://127.0.0.1:6379'  # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'  # 指定 Backend
CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'
CELERY_IMPORTS = (  # 指定导入的任务模块
    'celery_app.task1',
    'celery_app.task2',
    'celery_app.handle_video_edit'

)

'''
#定时任务
# Broker and Backend
from datetime import timedelta
from celery.schedules import crontab
BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区

CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2'
)
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=30),  # 每隔30秒执行一次
        'args': (4, 5)  # 任务参数
    },
    'multiply-at-some-time': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=16, minute=31),  # 设置在下午16：20执行一次
        'args': (4, 5)  # 执行任务参数
    }
}
'''
