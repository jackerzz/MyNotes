from django.conf.urls import url
from viodes.views import  other, user,VideoProcessing

urlpatterns = [
    url(r'^login/', user.Urser_login),  # 用户登录
    url(r'^signup/', user.User_signup),  # 用户注册

    url(r'^register', user.register),
    url(r'^register.html', user.register),
    # 修改用户信息
    url(r'^updateinfo/', other.update_userinfo),

    url(r'^userinfo/', other.User_info),

    # 用户图片
    url(r'^imgs.html$', other.imgs),
    url(r'^get_imgs.html$', other.get_img),
    # url(r'^Timeline.html$', views.Timeline),
    # 用户视频
    url(r'^video.html$', other.video),
    url(r'^get_video.html$', other.get_video),

    # 找回密码
    url(r'^cs_retrievepw/', user.User_Retrieve),  # 更改密码
    url(r'^cs_email/', user.User_Email),  # 输入邮箱
    url(r'^sc_retieve/', user.Sc_retieve),
    # 草稿相功能
    url(r'^Pseudo_delete_img.html$', other.pdimg),
    url(r'^Pseudo_delete_video.html$', other.pdvideo),
    # 单体上传
    url(r'^uploadPhoto/', other.upload_photo),
    url(r'^upload.html/', other.video_upload),
    # 根据创建时间轴显示
    url(r'^showtimes.html$', other.showtiems),
    url(r'^test$', VideoProcessing.test),
]
