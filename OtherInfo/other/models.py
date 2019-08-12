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
