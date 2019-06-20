002
    class UserTaskResource(Resource):
        query_set = UserTask.objects.all()
        fields = ('slug', 'streak_counter')


    class UserTaskActionResource(Resource):
        query_set = UserTaskAction.objects.all()
        allowed_methods = ('get_pk',)
        method_perms = (login_required,)
        fields = (
            ResourceMethodField('claimable', method_name='get_claimable'),#Resource通过方法在你的内容中创建自定义字段
            ResourceModel('task', resource=UserTaskResource),
            'status', 'claim_value')

        def get_pk(self, pk):
            # make sure we only allow getting rewards that the user own
            obj = self.get_instance(pk=pk, owner=self.request.user)
            return {
                'status_code': 200,
                'data': self.resolve_fields(obj=obj)
            }

        def get_claimable(self, prop, obj, request):
            return obj.task.get_handler().can_claim_reward(task_action=obj)




001：
    class VideoWatchResource(Resource):
        """
        Resource for creating a VideoWatch record.
        Upon create, this will emit the `videowatch_created` signal.
        """
        query_set = VideoWatch.objects.all()
        fields = (
            'id', ResourceTypeConvert('play_time', float),
            ResourceTypeConvert('video_duration', float),
            ResourceTypeConvert('when', convert_isoformat),)
        update_filter_fields = ('watch_data',)
        allowed_methods = ('create', 'update',)
        form_class = VideoWatchForm

        def get_form(self, *args, **kwargs):
            form_class = self.get_form_class(*args, **kwargs)
            if form_class is None:
                raise ValueError('{} did not specify a form_class'.format(
                    self.__class__.__name__))
            return form_class(self.request.user, *args, **kwargs)

        def resolve_filters(self, *args, **kwargs):
            filters = super(VideoWatchResource, self).\
                resolve_filters(*args, **kwargs)
            if 'watch_data' in filters:
                filters['id'] = signing.loads(
                    filters.pop('watch_data')).get('watch_id')
            return filters

        def create_response_data(self, obj):
            videowatch_created.send(
                sender=VideoWatch, instance=obj, target=obj.video, created=True)
            return {'watch_data': signing.dumps({'watch_id': obj.id})}