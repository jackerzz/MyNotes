-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
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
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
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
        ResourceCachedForeignKey    #resource 缓存 外键
            用于解析解析资源的外键实例缓存结果。 资源将尝试访问<foreignkey> _id属性
            首先，使用它来检查数据是否在缓存中，如果是，则立即返回。
            这将减少不必要的查询以获取实例本身。 一个常见的用例field是指具有在多个Resource中使用的缓存Resource，
            因此存在数据在缓存中的可能性很高（例如，用于解析用户的Resource）。
'''
class UserResource(Resource):
    query_set = User.objects.all()
    is_cached=True          
    chache_prefix="user"    #指定缓存前缀
    chache_timeout=200      #以秒为单位缓存多长时间
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
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
from sileo.resource import Resource
from sile.registration import register

from models import Foo


class FooResource(Resource):

    query_set = Foo.objects.all()
    fields = ['bar']    #--->fields是序列化结果中包含的字段名称或属性的列表


    allowed_methods = ['get_pk', 'filter']
        # allowed_methods是resource()支持的方法列表（get_pk，filter，form_dict，create，update，delete）
    filter_fields = ('bar__icontains',)
    # filter_fields是用户可以指定的可选过滤器参数列表。 例如，使用上面定义的resourse()
    # 当您访问过滤器时，生成的query_set可以是Foo.objects.all（）。filter（bar__icontains ='曾提供过的'）
    is_cached = True
    #   is_cached是一个布尔值，如果希望缓存resource()的输出/结果，则设置为True。 请注意，缓存是每个记录/实例而不是每个查询。
    cache_timeout = 120
        # cache_timeout是一个整数，表示您希望
    cache_prefix = 'foo'
        # cache_prefix指定所用缓存键的前缀。 在关于缓存键的示例中，自缓存键起可以是foo_1是cache_prefix和实例pk的组合


# if you want to make your resource accessible via HTTP request
#如果您想通过HTTP请求访问您的resource()
register(namespace='foo-space', name='foo', resource=FooResource)


-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
BigBoos：
    https://legacy.gitbook.com/@wizardforcel
    https://www.cnblogs.com/ctztake/p/8428387.html


002：
    @cache_locking(lock_id,val)
         lock_id  - 要使用的缓存ID
         val  - 给定缓存的值
    
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
001
PanelPageMixin()  ---请求入口数据检测：仅ajax数据request可以通过
TemplateView()    ---基于类的通用模板视图的升级， 这个一个包括上面的JS变量和一个用于存储它的上下文。
                  ---我们的自定义模板视图不仅添加了传统上下文，还添加了一个JS变量暴露给渲染的附加上下文模板。
LoginRequiredMixin() 猜测：登录状态检测  &&  请求类型检测入口 get put post delete
mixins:           ---src/channelfix/channelfix/site/views/mixins.py   为对应views.py class 定义class
                  ---http://shouce.jb51.net/django-chinese-docs-18/3_4_4_Using%20mixins.html    

Rest              ---https://www.hairuinet.com/zb_users/upload/2017/06/201706161497601359210108.pdf


继承重写方法：
        https://segmentfault.com/a/1190000004400540
        generics.py
        mixins.py         (主要看这个)
        https://segmentfault.com/a/1190000004401112


-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
001
反射：
    https://www.cnblogs.com/haiyan123/p/7375772.html

反射：可以用字符串的方式去访问对象的属性，调用对象的方法（但是不能去访问方法），python中一切皆对象，都可以使用反射。

反射有四种方法:

    hasattr：hasattr（object,name）判断一个对象是否有name属性或者name方法。有就返回True，没有就返回False

    getattr：获取对象的属性或者方法，如果存在则打印出来。hasattr和getattr配套使用需要注意的是，如果返回的是对象的方法，返回出来的是对象的内存地址，如果需要运行这个方法，可以在后面添加一对（）

    setattr：给对象的属性赋值，若属性不存在，先创建后赋值

    delattr：删除该对象指定的一个属性

--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------
002
自动化测试（Testcase）
---->>>https://blog.csdn.net/u012291393/article/details/78768535    
    setup
      --user    --UserFactory()
      --data
      --url
    test_xxx_001:
        -->request
        -->response
        -->reverse() 刷新请求
        -->
注：工厂式生成测试用列，
003
require:
    https://www.cnblogs.com/xiaofenguo/p/6598373.html
    https://www.cnblogs.com/ngy0217/p/8780966.html
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
(function(root, declaration) {
    if (typeof define === 'function' && define.amd) {
        define(['stapes', 'promise'], declaration);
    } else {
        root.Sileo = declaration(root.Stapes, root.Promise);
    }
})(this, function(Stapes, Promise) {

    var ModelManager = Stapes.subclass({
        constructor: function(model) {
            this.model = model;
        },
        get: function(pk, extras) {
            var url = this.model.baseUrl + 'get/' + pk + '/';
            // extras are optional
            if (extras) {
                url += '?' + this._parseGetParams(extras);
            }
            return this._fetch('GET', url);
        },
        filter: function(filter, exclude) {
            var url = this.model.baseUrl + 'filter/';
            var filterArgs = this._parseGetParams(filter);
            if (filterArgs !== '') {
                url += '?' + filterArgs;
            }
            // exclude is optional
            if (exclude) {
                if (filterArgs === '') {
                    url += '?';
                }   else {
                    url += '&';
                }
                url += this._parseGetParams(exclude);
            }
            return this._fetch('GET', url);
        },
        form_dict: function(filter) {
            var url = this.model.baseUrl + 'form-info/';
            if (filter) {
                if (typeof filter !== 'object') {
                    filter = {'pk': filter};
                }
                var filterArgs = this._parseGetParams(filter);
                if (filterArgs !== '') {
                    url += '?' + filterArgs;
                }
            }
            return this._fetch('GET', url);
        },
        create: function(formdata, extras) {
            var url = this.model.baseUrl + 'create/';
            // extras are optional
            if (extras) {
                url += '?' + this._parseGetParams(extras);
            }
            return this._fetch('POST', url, formdata);
        },
        update: function(filter, formdata, extras) {
            if (typeof filter !== 'object') {
                filter = {'pk': filter};
            }
            var url = this.model.baseUrl + 'update/';
            var filterArgs = this._parseGetParams(filter);
            if (filterArgs !== '') {
                url += '?' + filterArgs;
            }
            // extras are optional
            if (extras) {
                if (filterArgs === '') {
                    url += '?';
                }   else {
                    url += '&';
                }
                url += this._parseGetParams(extras);
            }
            return this._fetch('POST', url, formdata);
        },
        delete: function(filter, extras) {
            if (typeof filter !== 'object') {
                filter = {'pk': filter};
            }
            var url = this.model.baseUrl + 'delete/';
            var filterArgs = this._parseGetParams(filter);
            if (filterArgs !== '') {
                url += '?' + filterArgs;
            }
            // extras are optional
            if (extras) {
                if (filterArgs === '') {
                    url += '?';
                }   else {
                    url += '&';
                }
                url += this._parseGetParams(extras);
            }
            return this._fetch('POST', url);
        },
        _fetch: function(method, url, data) {
            var _this = this;
            var xhr = null;
            var promise = new Promise(function(resolve, reject) {
                var req = new XMLHttpRequest();
                xhr = req;
                // somehow upload events dont fire unless
                // `req.upload` is accessed before connection is open
                req.upload.onprogress = function(){};
                req.open(method, url, true);
                req.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
                if (method === 'POST') {
                    req.setRequestHeader('X-CSRFToken', _this._getCSRFToken());
                }
                req.onreadystatechange = function() {
                    if (req.readyState === 4) {
                        if ((req.status === 200 || req.status === 201) &&
                        typeof resolve === 'function') {
                            _this.model.callback(resolve)(JSON.parse(req.responseText).data);
                        }   else if (req.status !== 200 &&
                        typeof reject === 'function') {
                            reject(req);
                        }
                    }
                };
                req.send(data ? getData(data) : null);
            });
            promise.xhr = xhr;
            return promise;
        },
        _parseGetParams: function(extras) {
            var exs = [];
            for (var key in extras) {
                if(extras.hasOwnProperty(key)) {
                    exs.push(key + '=' + extras[key]);
                }
            }
            return exs.join('&');
        },
        _getCSRFToken: function() {
            var pattern = new RegExp('(?:(?:^|.*;)\\s*'
                + encodeURIComponent('csrftoken').replace(/[\-\.\+\*]/g, '\\$&')
                + '\\s*\\=\\s*([^;]*).*$)|^.*$');
            var value = decodeURIComponent(
                document.cookie.replace(pattern, '$1'));
            return value || null;
        }
    });



    var utils = {
        extend: function(base) {
            Array.prototype.slice.call(arguments, 1).forEach(function(ext) {
                for (var key in ext) {
                    if (ext.hasOwnProperty(key)) {
                        base[key] = ext[key];
                    }
                }
            });
            return base;
        },

        flow: function(data, callbacks) {
            return callbacks.reduce(function(data, callback) {
                if (data instanceof Array) {
                    return data.map(callback);
                }
                return callback(data);
            }, data);
        }
    };

    var defaultOptions = { applyGlobalMiddlewares: true };
    var globalMiddlewares = [];

    var Model = Stapes.subclass({
        constructor: function(namespace, resource, middlewares, options) {
            this.baseUrl = '/api-sileo/' + namespace + '/' + resource + '/';
            this.middlewares = middlewares || [];
            this.options = utils.extend({}, defaultOptions, options);
            this.objects = new ModelManager(this);
        },

        callback: function(callback) {
            var model = this;
            return function(response) {
                if (model.options.applyGlobalMiddlewares) {
                    response = utils.flow(response, globalMiddlewares);
                }
                response = utils.flow(response, model.middlewares);
                window.wrapErrors(callback)(response);
            };
        }
    });

    Model.addGlobalMiddleware = function() {
        Array.prototype.forEach.call(arguments, function(middleware) {
            if (typeof middleware === 'function') {
                globalMiddlewares.push(middleware);
            }
        });
    };

    // wrapper function to log errors in async functions
    function wrapErrors(fn) {
        // don't wrap function more than once
        if (!fn.__wrapped__) {
            fn.__wrapped__ = function () {
                try {
                    return fn.apply(this, arguments);
                } catch (e) {
                    window.onerror(e);
                    throw e; // re-throw the error
                }
            };
        }
        return fn.__wrapped__;
    }

    function getData(data) {
        if (!data) {
            return null
        }
        if (data.constructor.name === 'Object') {
            var param = data;
            data = new FormData();
            for (var key in param) {
                data.append(key, param[key]);
            }
        }
        return data
    }

    window.wrapErrors = window.wrapErrors || wrapErrors;

    return {
        Model: Model,
        ModelManager: ModelManager
    };
});
restmodel.js
nodejs集群查询优化:
    https://segmentfault.com/a/1190000015841624
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------- 

 models Field Types总结# https://blog.csdn.net/devil_2009/article/details/41735611    
    #-------》PositiveSmallIntegerField
 on_delete #级联删除
    on_delete=None,               # 删除关联表中的数据时,当前表与其关联的field的行为
    on_delete=models.CASCADE,     # 删除关联数据,与之关联也删除
    on_delete=models.DO_NOTHING,  # 删除关联数据,什么也不做
    on_delete=models.PROTECT,     # 删除关联数据,引发错误ProtectedError
    # models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
    on_delete=models.SET_NULL,    # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
    # models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
    on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
    on_delete=models.SET,         # 删除关联数据,
     a. 与之关联的值设置为指定值,设置：models.SET(值)
     b. 与之关联的值设置为可执行对象的返回值,设置：models.SET(可执行对象)

@property #fields 属性修改 eg:常用在图片url生成，。。
owner #所有者
when #时间
m-to-m
    子表在主表中对应的外键属性：related_name='buyer_fruit'

pk代表主键(primary key)，pk更加独立于实际的主键字段，即您不必关心主键字段是否被称为id或object_id或任何。

staticmethod:https://www.runoob.com/python/python-func-staticmethod.html

 signals (触发时启动)
        对于Django内置的信号,仅需注册指定信号,当程序执行相应操作时,系统会自动触发注册函数
            https://www.cnblogs.com/haiyan123/p/8259647.html

-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------


resource.py

----------------------------------------------------------------------------------------------------------------------
004:
    delete_object()        ---将对象标记为已删除。
                            --参数：
                                * obj  - 需要删除的实例
    isinstance()           ---isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
                                --https://www.runoob.com/python/python-func-isinstance.html
    filter_query()         ---返回 在filter方法中使用的查询集    
                                --参数：
                                     * filters  - 包含过滤器查询参数的dict
                                     * excludes - 包含排除部分参数的字典查询
    filter（）                ---返回列表中的筛选查询对象。

                                --参数：
                                     * filter_args  - 包含在中发送的过滤器数据的dict
                                                      请求，这将在传递之前进行清理
                                                      过滤查询
                                     * top  - 启动请求的位置的上限索引。
    filter_fields()         ---   是用户可以指定的可选过滤器参数列表。

    ResourceQuerySet()      ---处理查询集属性解析的 ResourceField()
    ResourceField().resolve(self, obj, request, **kwargs) 
                            ---此方法需要在子类中实现
                                 参数：
                                     * obj  - 包含我们要解析的属性的实例
                                     * request  - 请求对象

----------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------------------------
003：
    get_form_class()       ---返回用于create和update方法的表单类


002:
    resolve_fields()       ---解析`fields`属性中指定的字段且建立一个字典，默认开启缓存

    ResourceMethodField()  ---Resource通过方法在你的内容中创建自定义字段
    ResourceModel()        ---用于解析返回模型实例的字段/属性                       
    ResourceFiel(): 
                    ---
                        属性设置
                        参数：
                         * prop  - resource解析的模型属性的名称
                         * namespace  - 解析程序类的已注册命名空间
                         * resource_name  - 解析程序类的注册名称
                         * version  - resource所属的版本
                         *资源 - 解析器类
                         注意：
                             如果提供命名空间和resource_name，则不提供resource将自动确定resource
                             命名空间和resource_name。 此外，如果您提供resource
                             不传递命名空间和resource_name，因为那些不会
                             用过的。

                         用法：
                             ResourceField（'my_field'，'namespance'，'name'）
                                 or
                             ResourceField（'my_field'，resource = ResourceClass）
                    ---
----------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------------------------

001:
    get_form()                      --- 使用的form_class属性返回表单实例resource以及提供的参数和关键字参数参数。 如果resource没有，则此方法将引发ValueError指定form_class。
    resolve_filters()               --- 返回查询过滤器的键值对。
                ---
                    参数：
                         * filter_args  - 应该是查询对象的过滤器的dict。
                         * required_fields  - 必填字段列表
                         * optional_fields  - 可选字段列表
                ---         
    create_response_date().send()   ---发送消息（详：signal()）

    register()                      ---register(namespace='foo-space', name='foo', resource=FooResource)
    signal()                        ---https://segmentfault.com/a/1190000008455657  #create_response_data() => models.py
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
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