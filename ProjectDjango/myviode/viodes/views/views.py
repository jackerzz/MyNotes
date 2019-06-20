from django.shortcuts import render, redirect

'''
    主页
'''


def Home(request):
    return render(request, 'account/home.html')


'''
    退出
'''


def User_logut(request):
    if not request.session.get('is_login', None):
        return redirect('login')
    request.session.flush()
    return redirect('login')


'''
    我的作品主页
'''


def myproject(request):
    return render(request, 'works/myproject.html')
