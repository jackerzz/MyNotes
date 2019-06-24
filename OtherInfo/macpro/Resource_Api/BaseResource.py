from sileo.resource import Resource
from sile.registration import register

from models import Foo


class FooResource(Resource):

    query_set = Foo.objects.all()
    fields = ['bar']	#--->fields是序列化结果中包含的字段名称或属性的列表


    allowed_methods = ['get_pk', 'filter']
    	# allowed_methods是resource()支持的方法列表（get_pk，filter，form_dict，create，update，delete）
    filter_fields = ('bar__icontains',)
	# filter_fields是用户可以指定的可选过滤器参数列表。 例如，使用上面定义的resourse()
	# 当您访问过滤器时，生成的query_set可以是Foo.objects.all（）。filter（bar__icontains ='曾提供过的'）
    is_cached = True
	#	is_cached是一个布尔值，如果希望缓存resource()的输出/结果，则设置为True。 请注意，缓存是每个记录/实例而不是每个查询。
    cache_timeout = 120
    	# cache_timeout是一个整数，表示您希望
    cache_prefix = 'foo'
    	# cache_prefix指定所用缓存键的前缀。 在关于缓存键的示例中，自缓存键起可以是foo_1是cache_prefix和实例pk的组合


# if you want to make your resource accessible via HTTP request
#如果您想通过HTTP请求访问您的resource()
register(namespace='foo-space', name='foo', resource=FooResource)

