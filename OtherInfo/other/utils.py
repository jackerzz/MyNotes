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
	  --user	--UserFactory()
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