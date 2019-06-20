import os

from ffmpy import FFmpeg

from myviode import celery_app, settings
from viodes.models import Videos, AutoVideoFile


@celery_app.task
def handle_video_edit(video_id):
    video_file = Videos.objects.get(title=video_id)  # 数据库中获取视频object
    print(video_file)
    video_file_path = video_file.src.path  # 获取视频路径
    video_file_name = os.path.basename(video_file_path)  # 获取视频名称

    # 组装文件路径
    P_360_path = os.path.join(settings.MEDIA_ROOT, 'Videos/TranscodingVideo/P360')
    P_480_path = os.path.join(settings.MEDIA_ROOT, 'Videos/TranscodingVideo/P480')
    P_720_path = os.path.join(settings.MEDIA_ROOT, 'Videos/TranscodingVideo/P720')
    if not os.path.exists(P_360_path):
        os.makedirs(P_360_path)
    if not os.path.exists(P_480_path):
        os.makedirs(P_480_path)
    if not os.path.exists(P_720_path):
        os.makedirs(P_720_path)
    print(P_360_path, P_480_path, P_720_path)
    # 组装文件名
    out_path_720 = os.path.join(P_720_path, video_file_name + '{}_720.mp4'.format(
        str(video_id)))  # root路经+原视频名称+视频id+_720/480/360.ogg
    out_path_480 = os.path.join(P_480_path, video_file_name + '{}_480.mp4'.format(str(video_id)))
    out_path_360 = os.path.join(P_360_path, video_file_name + '{}_360.webm'.format(str(video_id)))

    try:
        out_path_360, out_path_480, out_path_720 = Edit_change(video_file_path, out_path_720, out_path_480,
                                                               out_path_360)

        auto = AutoVideoFile.objects.create(wav_360_file=out_path_360, ogg_480_file=out_path_480,
                                            mkv_720_file=out_path_720)
        auto.save()
    except:
        pass
    return None


# 对视频进行编码
def Edit_change(video_path, out_path_720, out_path_480, out_path_360):
    ff = FFmpeg(
        inputs={video_path: None},
        outputs={
            out_path_360: '-vf scale=480:360',
            out_path_480: '-vf scale=640:480',
            out_path_720: '-vf scale=1280:720'
        })
    print(ff.cmd)
    ff.run()
    return out_path_360, out_path_480, out_path_720
