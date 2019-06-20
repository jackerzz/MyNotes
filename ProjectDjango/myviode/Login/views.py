import time
import uuid

from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import login as auth_login
from django.urls import reverse

from Login.froms import BindEmail
from Login.utils.OAuth_Base import OAuth_GitHub, OAuth_WEIBO, OAuth_QQ
from Login import models

# Create your views here.
# github
from myviode import settings


def git_login(request):
    oauth_git = OAuth_GitHub(settings.GITHUB_APP_ID, settings.GITHUB_CALLBACK_URL)
    url = oauth_git.get_auth_url()
    return HttpResponseRedirect(url)


def git_check(request):
    type = '1'
    request_code = request.GET.get('code')
    oauth_git = OAuth_GitHub(settings.GITHUB_APP_ID, settings.GITHUB_CALLBACK_URL)
    try:
        access_token = oauth_git.get_access_token(request_code)
        time.sleep(0.1)
    except:
        data = {}
        data['goto_url'] = '/'
        data['goto_time'] = 100000
        data['goto_page'] = True
        data['message_title'] = '登录失败'
        data['message'] = '获取授权失败，请确认是否允许授权，并重试。若问题无法解决，请联系网站管理人员'
        return render_to_response('', data)
    infos = oauth_git.get_user_info()  # 获取用户信息

    nickname = infos.get('login', '')
    image_url = infos.get('avatar_url')
    open_id = str(oauth_git.openid)
    signature = infos.get('bio', '')
    if not signature:
        signature = '无标个性签名'
    sex = '1'
    githubs = models.OAuth_ex.objects.filter(openid=open_id, type=type)
    if githubs:
        auth_login(request, githubs[0].user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect('/')
    else:
        try:
            email = oauth_git.get_email()
        except:
            url = ''
            return HttpResponseRedirect(url)
    users = models.User.objects.filter(email=email)
    if users:
        users = users[0]
    else:
        while models.User.objects.filter(username=nickname):  # 防止用户名重复
            nickname = nickname + '*'
            users = models.User(username=nickname, sex=sex, signature=signature)
            pwd = str(uuid.uuid1())  # 随机设置用户密码
            users.password(pwd)
            users.is_active = True
            users.download_image(image_url, nickname)  # 下载用户头像图片
            users.save()
    oauth_ex = models.OAuth_ex(user=users, openid=open_id, type=type)
    oauth_ex.save()  # 保存后登录
    auth_login(request, users, backend='django.contrib.auth.backends.ModelBackend')
    data = {}  # 登录反馈
    data['goto_url'] = '/'
    data['goto_time'] = 10000
    data['goto_page'] = True
    data['message_title'] = '绑定成功'
    data['message'] = u'绑定成功,你的用户名：<b>%s</b>,你可以通过第三方账户的登录本站拉' % nickname
    return render_to_response('Login/success.html', data)


# QQ
def qq_login(requset):
    oauth_qq = OAuth_QQ(settings.QQ_APP_ID, settings.QQ_KEY, settings.QQ_CALLBACK_URL)
    url = oauth_qq.get_auth_url()
    return HttpResponseRedirect(url)


def qq_check(request):
    type = 3
    code = request.GET.get('code', '')
    oauth_qq = OAuth_QQ(settings.QQ_APP_ID, settings.QQ_KEY, settings.QQ_CALLBACK_URL)
    try:
        access_token = oauth_qq.get_access_token(code)
        time.sleep(0.1)
    except:
        data = {}
        data['goto_url'] = '/'
        data['goto_time'] = 100000
        data['goto_page'] = True
        data['message_title'] = '登录失败'
        data['message'] = '获取授权失败，请确认是否允许授权，并重试。若问题无法解决，请联系网站管理人员'
        return render_to_response('Login/success.html', data)
    openid = oauth_qq.get_open_id()
    qquser = models.OAuth_ex.objects.filter(openid=openid, type=type)
    if qquser:
        auth_login(request, qquser[0].user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect('/')
    else:
        infos = oauth_qq.get_user_info()
        nickname = infos.get('nickname', '')
        image_url = infos.get('figureurl_qq_1')
        sex = '1' if infos.get('gender', '') == '男' else '2'
        signature = '无个性签名'
        url = "%s?nickname=%s&openid=%s&type=%s&signature=%s&image_url=%s&sex=%s" % (
            reverse('oauth:bind_email'), nickname, openid, type, signature, image_url, sex)
        return HttpResponseRedirect(url)  # 提示用户绑定emial


# 微博
def weibo_login(request):
    oauth_weibo = OAuth_WEIBO(settings.WEIBO_APP_ID, settings.WEIBO_KEY, settings.WEIBO_CALLBACK_URL)
    url = oauth_weibo.get_auth_url()
    return HttpResponseRedirect(url)


def weibo_check(request):
    type = 3
    code = request.GET.get('code','')
    oauth_weibo = OAuth_WEIBO(settings.WEIBO_APP_ID, settings.WEIBO_KEY, settings.WEIBO_CALLBACK_URL)
    try:
        oauth_weibo.get_access_token(code)
        time.sleep(0.1)
    except:
        data={}
        data['goto_url']='/'
        data['goto_time']=10000
        data['goto_page'] = True
        data['message_title'] = '登录失败'
        data['message'] = '获取授权失败，请确认是否允许授权，并重试。若问题无法解决，请联系网站管理人员'
        return render_to_response('oauth/response.html', data)
    openid = oauth_weibo.get_open_id()  #获取用户信息
    weibos = models.OAuth_ex.objects.filter(openid=openid, type=type)
    infos = oauth_weibo.get_user_info()
    nickname = infos.get('screen_name', '')
    image_url = infos.get('profile_image_url', )
    signature = infos.get('description', '')
    sex = 'm' if infos.get('gender', '') == '男' else 'f'
    if not signature:
        signature = '你有点懒'
    if weibos:
        auth_login(request,weibos[0].user,backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect('/')
    else:
        try:
            email = oauth_weibo.get_email()
        except:
            url=''
            return HttpResponseRedirect(url)
    user = models.User.objects.filter(email=email)
    if user:
        user = user[0]
    else:
        while models.User.objects.filter(username = nickname):
            nickname = nickname +'*'
            users = models.User(username =nickname,sex =sex,signature=signature)
            pwd = str(uuid.uuid1())
            users.password(pwd)
            users.is_active = True
            users.download_image(image_url,nickname)
            users.save()
    oauth_ex = models.OAuth_ex(user=users,openid=openid,type=type)
    oauth_ex.save()
    data = {}  # 登录反馈
    data['goto_url'] = '/'
    data['goto_time'] = 10000
    data['goto_page'] = True
    data['message_title'] = '绑定成功'
    data['message'] = u'绑定成功,你的用户名：<b>%s</b>,你可以通过第三方账户的登录本站拉' % nickname
    return render_to_response('Login/success.html', data)


# 邮箱绑定
def bind_email(request):
    sex = request.GET.get('sex', request.POST.get('sex', ''))
    openid = request.GET.get('openid', request.POST.get('openid', ''))
    nickname = request.GET.get('nickname', request.POST.get('nickname', ''))
    type = request.GET.get('type', request.POST.get('type', ''))
    signature = request.GET.get('signature', request.POST.get('signature', ''))
    image_url = request.GET.get('image_url', request.POST.get('image_url', ''))

    if request.method == 'POST':
        froms = BindEmail(request.POST)
        if froms.is_valid():
            openid = froms.cleaned_data['openid']
            nickname = froms.cleaned_data['nickname']
            type = froms.cleaned_data['type']
            signature = froms.cleaned_data['signature']
            image_url = froms.cleaned_data['image_url']
            sex = froms.cleaned_data['sex']
            email = froms.cleaned_data['email']
            password = froms.cleaned_data['password']
            users = models.User.objects.filter(email=email)
            if users:
                user = users[0]
            else:
                while models.User.objects.filter(username=nickname):
                    nickname = nickname + '*'
                user = models.User(username=nickname, email=email, sex=sex, signature=signature)
                user.password(password)
                user.is_active = True
                user.download_image(image_url, nickname)
                user.save()
            oauth_ex = models.OAuth_ex(user=user, openid=openid, type=type)
            oauth_ex.save()
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            data = {}
            data['goto_page'] = True
            data['goto_url'] = '/'
            data['goto_time'] = 10000
            data['message_title'] = '绑定成功'
            data['message'] = '绑定成功您的用户名为：<b>%s</b>。您现在可以同时使用本站账号和此第三方账号登录本站了！' % nickname
            return render_to_response('Login/success.html', data)
        else:
            form = BindEmail(
                initial={
                    'openid': openid,
                    'nickname': nickname,
                    'type': type,
                    'signature': signature,
                    'image_url': image_url,
                    'sex': sex
                })
        return render(request, 'Login/bind_email.html', context={'form': form, 'nickname': nickname, 'type': type})
