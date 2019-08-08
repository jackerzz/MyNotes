import anyjson as json
import http.client as http
from mock import patch

from django.urls import reverse
from django.test import TestCase

from channelfix.site.tests.factories import UserFactory
from channelfix.site.tests.test_api_sileo.resource_resolver import(
    ResourceBaseTestCase
)
from plex.contrib.video.models import VideoPost
from plex.contrib.video.factories import VideoPostFactory
from plex.contrib.video.tasks import save_mention_context
from plex.contrib.zencoder.tests import DummyClient
from plex.contrib.storage.backend import StorageBackend

@patch('plex.contrib.zencoder.requests',DummyClient())
class VideoPostResourceTestCase(ResourceBaseTestCase,TestCase):
    fixtures = ['test_user','test_groups','test_actions']
    namespace = 'video-post'
    resource_name = 'video-post'
    version = 'v2'

    @classmethod
    def setUpTestData(self):
        super().setUpTestData()
        self.user = UserFactory()
        args = (self.version,self.namespace,self.resource_name)
        self.create_url = reverse('sileo:api-create-version',args=args)
        self.request_headers = {
            'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest',
        }

    def get_instance(self):
        return VideoPostFactory(owner=self.user,status=0)
    
    def test_get_pk(self):
        self.client.login(username=self.user.username,password='password')
        video_post = VideoPostFactory(owner=self.user)
        user = UserFactory()
        video_post.user_mentions.add(user)
        save_mention_context(video_post,[user])
        get_url = reverse(
            'sileo:api-detail-version',
            args=(self.version,self.namespace,self.resource_name,video_post.id
            ))
        response = self.client.get(get_url,**self.request_headers)
        self.assertEqual(http.OK,response.status_code)
        resp = json.loads(response.content.decode('utf-8')).get('data')
        self.assertTrue('video' in resp)
        self.assertEqual(list,type(resp['mention_context']))
        self.client.logout()
        response = self.client.get(get_url,**self.request_headers)
        self.assertEqual(http.FORBIDDEN,response.status_code)

    def test_create_method(self):
        self.client.login(username=self.user.username,password='password')
        response = self.client.post(
            self.create_url,{'raw_video_uuid': 'test-video-9.mp4'},
            **self.request_headers)
        self.assertEqual(http.BAD_REQUEST,response.status_code)

        StorageBackend.add_key_to_valid_keys(key='test-video-9')
        response = self.client.post(
            self.create_url,{'raw_video_uuid':'test-video-9.mp4'},
            **self.request_headers)
        self.assertEqual(http.CREATED,response.status_code)
        resp = json.loads(response.content.decode('utf-8')).get('data')
        print(resp)
        self.assertIsNotNone(resp)
        video_post = VideoPost.objects.filter(
            video__raw_video_uuid='test-video-9.mp4').first()
        self.assertIsNotNone(video_post)
        self.assertEqual(video_post.status,VideoPost.PENDING)