from django.http import HttpResponse


from viodes.tasks import handle_video_edit




def test(request):
    handle_video_edit.delay('s2')
    return HttpResponse('--------ok-------')