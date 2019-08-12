#from : https://www.cnblogs.com/ctztake/p/9932002.html
$ ps -ef|grep nginx 
	# nginx会自动根据当前主机的CPU的内核数目创建对应的进程数量(当前ubuntu主机是2核4线程配置)
$ nginx
	#启动
$ nginx -s stop 
or
$ nginx -s quit


nginx 配置：

		ain                                # 全局配置

		events {                            # nginx工作模式配置

		}

		http {                                # http设置
		    ....

		    server {                        # 服务器主机配置
		        ....
		        location {                    # 路由配置
		            ....
		        }

		        location path {
		            ....
		        }

		        location otherpath {
		            ....
		        }
		    }

		    server {
		        ....

		        location {
		            ....
		        }
		    }

		    upstream name {                    # 负载均衡配置
		        ....
		    }
		}


基础配置

日志配置

ssl证书加密

压缩配置

文件缓存配置


nginx 配置文件组成：
	main：用于进行nginx全局信息的配置
	events：用于nginx工作模式的配置
	http：用于进行http协议信息的一些配置
	server：用于进行服务器访问信息的配置
	location：用于进行访问路由的配置
	upstream：用于进行负载均衡的配置





