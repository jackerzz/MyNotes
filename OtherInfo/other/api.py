resource.py
----------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------------------------
004:
	delete_object()        ---将对象标记为已删除。
							--参数：
                                * obj  - 需要删除的实例
	isinstance()		   ---isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
								--https://www.runoob.com/python/python-func-isinstance.html
	filter_query()		   ---返回 在filter方法中使用的查询集	 
								--参数：
						             * filters  - 包含过滤器查询参数的dict
						             * excludes - 包含排除部分参数的字典查询
	filter（）			    ---返回列表中的筛选查询对象。

						        --参数：
						             * filter_args  - 包含在中发送的过滤器数据的dict
						                              请求，这将在传递之前进行清理
						                              过滤查询
						             * top  - 启动请求的位置的上限索引。
	filter_fields()         ---   是用户可以指定的可选过滤器参数列表。

	ResourceQuerySet() 	    ---处理查询集属性解析的 ResourceField()
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
	resolve_fields()	   ---解析`fields`属性中指定的字段且建立一个字典，默认开启缓存

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
	get_form()             			--- 使用的form_class属性返回表单实例resource以及提供的参数和关键字参数参数。 如果resource没有，则此方法将引发ValueError指定form_class。
	resolve_filters()	   			--- 返回查询过滤器的键值对。
				---
				    参数：
			             * filter_args  - 应该是查询对象的过滤器的dict。
			             * required_fields  - 必填字段列表
			             * optional_fields  - 可选字段列表
				---			
	create_response_date().send()   ---发送消息（详：signal()）

	register() 			   			---register(namespace='foo-space', name='foo', resource=FooResource)
	signal()			   			---https://segmentfault.com/a/1190000008455657  #create_response_data() => models.py