"""myviode URL Configuration

The `urlpatterns` list routes URLs to viewss. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function viewss
    1. Add an import:  from my_app import viewss
    2. Add a URL to urlpatterns:  url(r'^$', viewss.home, name='home')
Class-based viewss
    1. Add an import:  from other_app.viewss import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls

from myviode import settings
from viodes.views import views
from django.contrib import admin
from rest_framework.authtoken import views as vi
from django.views.static import serve
urlpatterns = [
    url(r'^$', views.Home),
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    url(r'^myproject.html$', views.myproject),
    url(r'^api/',include('viodes.api.urls',namespace='api')),
    url(r'^viodes/',include('viodes.urls',namespace='viodes')),
    url(r'^login/',include('Login.urls',namespace='Login')),
    url('docs', include_docs_urls(title='paker')),
    # 验证码
    url(r'^captcha', include('captcha.urls')),
    # 退出
    url(r'^logout/', views.User_logut),
    url(r'api-token-auth/', vi.obtain_auth_token),



]
