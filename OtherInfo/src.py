src/channelfix
	 pyyaml/
	 	--yml解析器第三方库：https://github.com/yaml/pyyaml
	 static-media/
	 	--静态的外部文件
	 tasker/
	 	--定时任务 or 异步任务 初始化、log输出。。。。
     
     channelfix/
		 docs/
		 ministry/			--服务
		 patron/			--资助者（第三方接入）
		 plex/				--定制的api
		 sass/				--https://www.sass.hk/
		 setup.py
		 sileo/
		 tournament/ 					比赛
		 	 base_tournament/			基础
			 challenge_tournament/		挑战
			 generic_tournament/		通用			
			 social_tournament/			社交
			 	from __future__ import absolute_import, unicode_literals  # 目的是拒绝隐士引入防止冲突产生。


	     channelfix/
	     	-site
	     		 admin.py
				 api/
				 api_sileo/
				 apps.py
				 auth/
				 finders/
				 fixtures/
				 forms/
				 management/
				 middleware/
				 migrations/
				 models/
				 mustachetemplates/
				 preprocessors/
				 signals/
				 		--https://www.cnblogs.com/haiyan123/p/8259647.html
				 		--providing_args
             					此信号可以在send（）调用中传递的参数列表。
				 static/
				 tasks/
				 templates/
				 templatetags/
				 tests/
				 urls.py
				 utils/
				 views/
				 	default_pagination_size=20 #默认分页大小
				 	reverse() :反向list中的元素
