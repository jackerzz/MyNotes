from django.contrib.auth.models import User
from models import Foo
from sileo.resource import Resource
from sileo.fields import ResourceModel
		# fields模块包含几个可用于允许Resource序列化字段或属性的类通常不可序列化。也就是说他需要借助fields()序列化
class UserResource(Resource):
	query_set=User.objects.all()
	fields = ['pk','username']

class FooResource(Resource):
	query_set=Foo.objects.all()
	# ResourceModel()用于解析返回模型实例的字段/属性
	fields=['bar',ResourceModel('owner',resource=UserRsource)]


from sileo.fields import ResoerceTypeConvert
class Foo1Resource(Resource):
	query_set = Bar.objects.all()
		#foo1 = models.DecimalField(max_digits=12, decimal_places=5)
	fields=[ResourceTypeConvert('foo1',str)] #resource 类型 转换
class MethodField(Resource):
	query_set=User.objects.all()
	fields=(
			'first_name','last_name',
			ResourceMethodField(
				'full_name',method_name='get_full_name_field'
				)
			# ResourceMethodField:
					'''
						Resource通过方法在你的内容中创建自定义字段
					'''
		)
	def get_full_name_field(self,prop,obj,request):
		return '%s %s' % (obj.first_name, obj.last_name)

'''
	sileo.fields.ResourceCachedForeignKey
		ResourceCachedForeignKey	#resource 缓存 外键
			用于解析解析资源的外键实例缓存结果。 资源将尝试访问<foreignkey> _id属性
			首先，使用它来检查数据是否在缓存中，如果是，则立即返回。
			这将减少不必要的查询以获取实例本身。 一个常见的用例field是指具有在多个Resource中使用的缓存Resource，
			因此存在数据在缓存中的可能性很高（例如，用于解析用户的Resource）。
'''
class UserResource(Resource):
	query_set = User.objects.all()
	is_cached=True			
	chache_prefix="user"	#指定缓存前缀
	chache_timeout=200		#以秒为单位缓存多长时间
class PostResource(Resource):
	query_set = Post.objects.all()
	fields=('id','content','data',ResourceCachedForeignKey('user',resource=UserResource))
	allowed_methods=('filter',)
	filter_fields=('post_id',)
# Resource Methods
'''
	Resource() 
		method 允许您获取有关实例的数据
			get, filter, form_dict, create, update, and delete
			通过HTTP request.

'''
#eg:
class FooResource(Resource):
	query_set=Foo.objects.all()
	filter=(
		'title'
		)
	allowed_methods('get_pk')
	#git_pk methods 允许您获取有关其pk的实例的数据
	allowed_methods('filter')
	#filter methods 允许您获取包含与您的过滤器匹配的实例数据的列表
	filter_fields = ['title__icontains']#过滤器匹配的实例数据的列表
	allowed_methods('')
register(namespace='foo-space', name='foo', resource=FooResource)

#form_dict :
	# 通常用于使用javascript渲染表单
models:
from django.db import models
class Foo(models.Methods):
	title = models.CharField(max_length=50)
#ModelForm
from sileo.forms import ModelForm
from models import Foo
class FooForm(ModelForm):
	class Meta:
		models = Foo
		filter  =('title',)
#api
from forms import FooForm
class FooResource(Resource):
	query_set = Foo.objects.all()
	allowed_methods = ['form_dict']#指定 表单类(form_class) 属性
	form_class = FooForm
register(namespace='foo-space',name='foo',resource=FooResource)
#前端
var Foo = new sileo.Model('foo-space','foo');
Foo.objects.form_dict().then.(function(data){
	console.log(data):
	}).catch(function(xhr){
		console.log('something went wrong')
	})


# update_filter_fields
	'''
		一组过滤器以获取要填充表单的实例
	'''
#eg:
class FooResource(Resource):
	query_set = Foo.objects.all()
	fields= ['title']
	allowed_methods=['form_dict']
	form_class = FooForm
	update_filter_fields=('pk',)#指定用作过滤器的过滤器字段列表，以获取form_dict和update方法的实例
register(namespace='foo-space', name='foo', resource=FooResource)
#js
Foo.objects.form_dict({'pk':1}).then(function(data){
	console.log(data)
	})catch(function(xhr){
	console.log("something went wrong")
	})
#create
'''
	允许您使用指定的form_class创建新记录。 
	create方法的作用:
		将请求中的数据（POST和FILES）传递给表单实例并尝试保存表单。
'''
from CreateResource(Resource):
	query_set = Foo.objects.all()
	fields = ['title']
	allowed_methods = ['create']
	form_class = FooForm
register(namespace='foo-space',name='foo',resource=CreateResource)
#js
var Foo = new sileo.Model('foo-space','foo')
Foo.objects.create({'title':'heloowordl'}).then(function(data){
	console.log(data)
	}).catch(function(data){
		console.log("something went wrong");
	});
# update
class UpdateResource(Resource):
	query_set = Foo.objects.all()
	fields = ['title']
	allowed_methods=['update']
	form_class=FooForm
	update_filter_fields=("title",)
register(namespace='foo-space',name='foo',resource=UpdateResource)
#delete
class DeleteResource(Resource):
	query_set = Foo.objects.all()
	allowed_methods=('delete')
	delete_filter_fields=('pk',)
register(namespace='foo-space',name='foo',resource=DeleteResource)
#js
var Foo = new sileo.Model('foo-space', 'foo');

Foo.objects.delete({'pk': 1}).then(function(data) {
    console.log(data);
}).catch(function(xhr) {
    console.log('Something went wrong!');
});
#权限控制访问
'''
has_perm
自定制
	method_perms =(控制函数)# method_perms属性中添加权限函数。
has_object_perm
'''
# eg:
def login_required(resource, *args, **kwargs):
    request = resource.request
    return hasattr(request, 'user') and request.user.is_authenticated()

class FooResource(Resource):
    query_set = Foo.objects.all()
    allowed_methods = ['filter']
    method_perms = (login_required,)


--------------------------------------------
--------------------------------------------
def owner_required(resource, method, obj, *args, **kwargs):
	-->src/channelfix/sileo/permissions.py
	权限方法，如果对象属于当前登录的用户，则返回True。

    参数：
         resource  - 调用此方法的Resource实例
         obj  - 您要操作的对象
         method  - 表示正在尝试的操作的字符串执行。 选项包括filter，get_pk，create，update，并删除
eg:
	Api:
		object_perms=(owner_required,)

def login_age_required(resource, *args, **kwargs):
	-->src/channelfix/channelfix/site/api_sileo/permissions.py
	权限函数，如果用户的年龄大于或等于13岁则通过身份验证，则返回True
eg:
	method_perms = (login_age_required,)


-->src/channelfix/sileo/resource.py
def get_form(self, *args, **kwargs):
	使用的form_class属性
		return表单实例
         resource以及提供的参数和关键字参数
        参数
			form_class
			如果resource==None，则此方法将引发ValueError
         
def get_form_class(self, *args, **kwargs):
	
	return 用于create和update方法的表单类
def validate_form(self, form):
	return 如果给定的表单有效，则返回true，否则返回False。