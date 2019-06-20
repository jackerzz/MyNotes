import hashlib
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from viodes import models
from viodes.froms import *

'''
    用户登录
'''
from django.shortcuts import render

from viodes.froms import UserForm


def Urser_login(request):
    if request.method == "GET":
        login_form = UserForm()
        return render(request, 'account/login.html', {"login_form": login_form})
    else:
        if request.method == "POST":
            login_form = UserForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                print('username：%s,password:%s', username, password)
                user = models.User.objects.filter(username=username, password=password)
                if user:
                    message = "欢迎登录"
                    print('欢迎登录')
                    # request.session["Username"] = username
                    # request.session.set_expiry(60000)
                    return redirect('/myproject.html', locals())
                else:
                    message = "用户名不存在或者密码不对"
                    return render(request, 'account/login.html', locals())

        return render(request, 'account/login.html', locals())


'''
    用户注册
'''


# 升级版
def User_signup(request):
    if request.method == 'GET':
        signup_form = RegisterForm()
        return render(request, "account/signup.html", {'signup_form': signup_form})
    else:
        if request.method == 'POST':
            signup_form = RegisterForm(request.POST)
            if signup_form.is_valid():
                username = signup_form.cleaned_data['Username']
                password1 = signup_form.cleaned_data['Password']
                password2 = signup_form.cleaned_data['password2']
                email = signup_form.cleaned_data['email']
                sex = signup_form.cleaned_data['sex']
                if username and password1 and password2 and email:
                    if password1 == password2:
                        user_obj = models.User.objects.filter(username=username).first()
                        email_obj = models.User.objects.filter(email=email).first()
                        if user_obj or email_obj:
                            message = '该邮箱已经被注册或在用名已存在'
                            return HttpResponse(message)
                        else:
                            models.User.objects.create(username=username, password=password1, email=email,
                                                       sex=sex).save()
                            return redirect('/viodes/login/')
                    else:
                        return HttpResponse('两次密码不一致')
        else:
            return HttpResponse('不能为空')


# 低配版
def register(request):
    if request.method == 'GET':
        return render(request, 'Rest/register.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        re_pwd = request.POST.get('re_pwd')
        email = request.POST.get('email')
        if name and pwd and re_pwd and email:
            if pwd == re_pwd:
                user_obj = models.User.objects.filter(username=name).first()
                email_obj = models.User.objects.filter(email=email).first()
                if user_obj and email_obj:
                    return HttpResponse('用户或在邮相地址已存在')
                else:
                    models.User.objects.create(username=name, password=pwd, email=email).save()
                    return redirect('/login/')
            else:
                return HttpResponse('两次密码不一致')

        else:
            return HttpResponse('不能有空！')


# password 加盐
def Hash_code(s, salt='psdd'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


'''
    用户找回密码
'''


# 输入邮箱
def User_Email(request):
    if request.method == 'GET':
        emailforms = EmailForm()
        return render(request, 'Retrieve/cs_email.html', locals())
    else:
        if request.method == 'POST':
            email_form = EmailForm(request.POST)
            if email_form.is_valid():
                email = email_form.cleaned_data['email']
                print(email)
                if email != '':
                    same_email_user = models.User.objects.filter(email=email)
                    #same_email_user = models.User.objects.filter(email_date__isnull=True)
                    if same_email_user:
                        return redirect('/viodes/cs_retrievepw/')
                    else:
                        message = '请检测你输入邮箱是否有误'
                        return render(request, 'Retrieve/cs_email.html', locals())
                else:
                    message = "请检查你填写的内容！"
                    return render(request,'Retrieve/cs_email.html',locals())
            else:
                message = '请检查你填写的内容'
                return HttpResponse(locals())


# 更改密码
def User_Retrieve(request):
    if request.method == 'GET':
        Retrieve = RetrieveForm()
        return render(request, 'Retrieve/cs_retrievepw.html', locals())
    else:
        if request.method == 'POST':
            retrieve_form = RetrieveForm(request.POST)
            print(retrieve_form,retrieve_form.changed_data)
            password = retrieve_form.cleaned_data['password1']
            password2 = retrieve_form.cleaned_data['password2']
            email = retrieve_form.cleaned_data['email']
            print(email, password2)
            if retrieve_form.is_valid():
                if email and password and password2:
                    if password == password2:
                        Email = models.User.objects.filter(email=email)
                        print(email)
                        if Email:
                            models.User.objects.filter(email=email).update(password=password)
                            return redirect('/viodes/login/')
                        else:
                            message = '请检测你输入邮箱是否有误'
                            return render(request, 'Retrieve/cs_retrievepw.html', locals())
                    else:
                        message = '请检查你填写的内容'
                        return render(request, 'Retrieve/cs_retrievepw.html', locals())


def Sc_retieve(request):
    if request == "GET":
        message = "恭喜你已经成功重置密码"
        email = EmailForm()
        render(request, 'Retrieve/sc_retieve.html', locals())
