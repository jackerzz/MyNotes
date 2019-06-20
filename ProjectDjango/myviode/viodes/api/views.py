from rest_framework import generics, viewsets, mixins
from viodes.models import *
from viodes.api.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import  HTTP_400_BAD_REQUEST

'''
generics.ListAPIView
    --GET:表中的数据
viewsets.ModelViewSet
    --GET,POST,详细的表结构信息
'''


class UserDatiView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class ImgView2(viewsets.ModelViewSet):
    queryset = Img.objects.all()
    serializer_class = ImgSerializers


class VideoView(viewsets.ModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializers


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserLogingApiView(APIView):
    queryset = User.objects.all()
    serializers_class = UserSerializers
    permission_classes = [AllowAny]

    def post(self, request, formata=None):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = User.objcts.get(username__exact=username)
        if user.password == password:
            serializers = UserSerializers(user)
            new_data = serializers.data
            self.request.session['user_id'] = user.id
            return Response(new_data, status=200)
        return Response('password error', HTTP_400_BAD_REQUEST)
