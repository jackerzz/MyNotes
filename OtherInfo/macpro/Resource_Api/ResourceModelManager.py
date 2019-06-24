from django.contrib.auth.models import User

from models import Bar

from sileo.resource import Resource
from sileo.fields import ResourceGenericModel
'''
	
sileo.fields.ResourceModelManager
	ResourceModelManager用于解析返回模型管理器的字段/属性
sileo.fields.ResourceQuerySet
		ResourceQuerySet用于解析返回查询集的属性
sileo.fields.ResourceGenericModel
		ResourceGenericModel用于解析返回不同类型实例的字段/属性，这对GenericForeignkeys特别有用
			----> from django.contrib.contenttypes.fields import GenericForeignKey
			----> target = GenericForeignKey('target_type', 'target_id')
'''
class  UserResource(Resource):
	query_set=User.objecets.all()
	fields=['pk','username']
class BarResource(Resource):
	query_set=Bar.objecets.all()
	fields=['foo',ResourceGenericModel('target',{"User":UserResource})]
		
'''
sileo.fields.ResourceTypeConvert
	ResourceTypeConvert允许您提供将字段/属性转换为可序列化的函数的函数
'''