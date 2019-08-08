vscode:
	拉取主分支：git pull origin develop  		注:提交后注意看是否与主库冲突
	切换分支：git checkout 分支name
	删除本地分支：git branch -d 分支name
	创建分支src/channelfix: git  branch 927-enhacement/influencer-page-display  注： 需要基于最新的分支进行开发后在提交
	编码
	提交：git add .
		 git commit -m 'Fix infuluencer page in review url'
		 git push origin 927-enhacement/influencer-page-display
		 	error：
		 		git log 	注：查看日志
		 		git branch 	注：查看分支
		 		git status	注：查看状态
		 		git --amend  注：修改commit 的内容
		 		git config --list   注： 查看git配置
					git config --global user.name ""
			 		git config --global user.email ""

			 	git log 
			 		-->	commit "提交id串"
			 	git reset commit "提交id串"
		 		git push -f origin 927-enhacement/influencer-page-display   注：覆盖远程上一次提交的内容
Chrome: 
	合并代码：
		https://forge.channelfix.com/channelfix/channelfix/merge_requests/2846#
		备注为wip状态
		修改wip 状态
		p+1人 可以提交
		其他需要3个人
	修改任务status:
		https://bposeats.atlassian.net/browse/
		并指定开发人员
	申请审查:
		https://mm.channelfix.com/tchannelfix/channels/code-review
			格式：
				@here if you have time, please review my changes for influencer page in review VIDEO_LIVE=undefined,thanks 
				[channelfixmr](https://forge.channelfix.com/channelfix/channelfix/merge_requests/2891/diffs),
				[jiraissue](https://bposeats.atlassian.net/browse/VIDS-927)
git--help:
	https://www.cnblogs.com/haiyan123/p/7994318.html
	https://github.com/dunwu/blog/blob/master/source/_posts/tools/git.md
	https://github.com/dunwu/blog
# 放弃工作目录下的所有修改
$ git reset --hard HEAD