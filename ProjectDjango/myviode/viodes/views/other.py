import hashlib
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, render_to_response
from viodes import models
from viodes.froms import *

'''
    用户视频
'''


def video(request):
    return render(request, 'works/video.html')


def get_video(request):
    nid = request.GET.get('nid')
    video_list = list(models.Videos.objects.filter(id__gt=nid).values('id', 'src', 'title'))
    # 按照状态显示
    # flag = request.GET.get('flag')
    # img_list = list(models.Videos.objects.filter(flag=flag).values('id', 'src', 'title'))
    ret = {
        'status': True,
        'data': video_list
    }
    return JsonResponse(ret)


def video_upload2(request):
    if request.method == 'GET':
        videoform = UploadVideoForm()
        return render(request, '', locals())
    if request.method == 'POST':
        videoform = UploadVideoForm(request.POST, request.FILES)
        if videoform.is_valid():
            title = videoform.cleaned_data('title')
            summary = videoform.cleaned_data('summary')
            src = videoform.cleaned_data('src')
            if src and title and summary != '':
                models.Videos.objects.create(src=src, title=title, summary=summary).save()
                if models:
                    message = {'status': True, 'message': '成功'}
                    return JsonResponse(message)
            else:
                message = {'status': False, 'message': '失败'}
                return JsonResponse(message)


# 换成采用admin主件
# 单体上传
def video_upload(request):
    if request.method == 'GET':
        return render(request, 'works/video.html')
    else:
        img = request.FILES.get('img')
        f = open(img.name, 'wb')
        for line in img.chunks():
            f.write(line)
        f.close()
        return HttpResponse('上传成功')


def pdvideo(request):
    flag=0
    # flag = request.GET.get("flag")
    videoUpdate = list(models.Videos.objects.filter(flag=flag).values('id', 'src', 'title'))
    ret = {
        'status': True,
        'data': videoUpdate
    }
    return JsonResponse(ret)


'''
用户照片
'''


def imgs(request):
    return render(request, 'works/photo.html')


def get_img(request):
    # 全体显示
    nid = request.GET.get('nid')
    img_list = models.Img.objects.filter(id__gt=nid).values('id', 'src', 'title', 'create_time')
    # 按照状态显示
    # flag = request.GET.get('flag')
    # img_list = models.Img.objects.filter(flag=flag).values('id', 'src', 'title')

    img_list = list(img_list)
    ret = {
        'status': True,
        'data': img_list
    }
    return JsonResponse(ret)


def upload_photo2(request):
    if request.method == 'POST':
        title = request.GET.get('title')
        summary = request.GET.get('summayr')
        src = request.FILES.get('k3')
        if src and title and summary != '':
            models.Img.objects.create(src=src, title=title, summary=summary).save()
            if models:
                message = {'status': True, 'message': '成功'}
                return JsonResponse(message)
        else:
            message = {'status': False, 'message': '失败'}
            return JsonResponse(message)


# 换成采用admin主件
def upload_photo(request):
    import os
    message = {'status': True, 'data': None, 'message': None}
    obj = request.FILES.get('k3')
    file_path = os.path.join('static/photo', obj.name)
    f = open(file_path, 'wb')
    for li in obj.chunks():
        f.write(li)
    f.close()
    message['date'] = file_path
    return HttpResponse(json.dumps(message))


'''
    伪删除
'''


def pdimg(request):
    # 前的ajax 中设置flag=1
    flag = 0
    # flag = request.GET.get('flag')
    imgUpdate = list(models.Img.objects.filter(flag=flag).values('id', 'src', 'title'))
    ret = {
        'status': True,
        'data': imgUpdate
    }
    return JsonResponse(ret)


'''
    根据时间线输出
'''


def showtiems(request):
    timeline = list(models.Img.objects.dates('create_time', 'day', 'DESC').values('id', 'src', 'title', 'flag'))
    print(timeline)
    ret = {
        'status': True,
        'data': timeline
    }
    return JsonResponse(ret)


'''
    用户个人信息
'''


def User_info(request):
    id = 2
    obj = models.User.objects.get(id=id)
    if request.method == 'GET':
        form = UpdateForm(
            initial={
                'Username': obj.username,
                'Email': obj.email,
                'Sex': obj.sex,
            }
        )
        return render_to_response("account/userinfo.html", {'form': form})


'''
    修改个人信息
'''


def update_userinfo(request):
    id = 2
    obj = models.User.objects.get(id=id)
    print(obj)
    if request.method == 'GET':
        form = UpdateForm(
            initial={
                'Username': obj.username,
                'Email': obj.email,
                'Sex': obj.sex,
            }
        )
        return render_to_response("account/updateinfo.html", {'form': form})
    else:
        if request.method == 'POST':
            formdata = UpdateForm(request.POST)
            if formdata.is_valid():
                user = formdata.cleaned_data['Username']
                email = formdata.cleaned_data['Email']
                sex = formdata.cleaned_data['Sex']
                obj.username = user
                obj.email = email
                obj.sex = sex
                obj.save()
        return redirect('/viodes/userinfo/')
