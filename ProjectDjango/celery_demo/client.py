from celery_app import task1
from celery_app import task2

''' 
    异步任务执行调度client端
    执行任务模块 
    将视频转成480 360 720 格式
    144p    (192×144，20帧/秒)，4：3，录制一分钟大约1MB；         ffmpeg -i input_file -s 192x144 output_file
    240p    (320×240，20帧/秒)，4：3，录制一分钟大约3MB；         ffmpeg -i input_file -s 320x240 output_file
    360p    (480×360，20帧/秒) ，4：3，录制一分钟大约7MB；        ffmpeg -i input_file -s 480×360 output_file
    480p    (640×480，20帧/秒)，4：3，录制一分钟大约12MB；        ffmpeg -i input_file -s 640×480 output_file
    720p    (1280×720，30帧/秒)  ， 16:9，录制一分钟大约35MB；    ffmpeg -i input_file -s 1280×720 output_file
    1080p  (1920×1080，30帧/秒) ，16:9 ， 录制一分钟大约80MB。    ffmpeg -i input_file -s 1920×1080 output_file
'''


def run():
    task1.add.apply_async(args=[2, 5])
    task2.multiply.apply_async(args=[2, 5])
    print("------------hello world0---------------------")


if __name__ == '__main__':
    run()