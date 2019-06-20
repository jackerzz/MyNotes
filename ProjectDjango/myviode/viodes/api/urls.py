from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from . import views


router = routers.DefaultRouter()
router.register(r'ImgView2', views.ImgView2)
router.register(r'user', views.UserDatiView)
router.register(r'VideoView2', views.VideoView)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'Userget', views.UserListView.as_view()),
    url(r'^login', views.UserLogingApiView.as_view()),

    # url(r'^logout', LogoutAPIView.as_view()),
    # url(r'^register', UserRegisterAPIView.as_view()),
]