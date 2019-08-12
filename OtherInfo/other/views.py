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

Rest 			  ---https://www.hairuinet.com/zb_users/upload/2017/06/201706161497601359210108.pdf


继承重写方法：
		https://segmentfault.com/a/1190000004400540
		generics.py
		mixins.py         (主要看这个)
		https://segmentfault.com/a/1190000004401112

