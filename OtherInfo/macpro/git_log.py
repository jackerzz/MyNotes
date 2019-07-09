(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git log
commit b193af3e21b836f4b0443640c120e5fffd3ef913 (HEAD -> 927-enhacement/influencer-page-display, origin/develop, origin/HEAD, develop)
Merge: 1743d28249 227dd564ac
Author: Chris Statzer <chris.statzer@gmail.com>
Date:   Wed Jul 3 08:03:35 2019 +0000

    Merge branch '906-bugfix/sms-btn-click-issue' into 'develop'
    
    Resolve "sms send btn can not clickable"
    
    Closes VIDS-906
    
    See merge request channelfix/channelfix!2824
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git diff
diff --git a/channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html b/channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
index d25ae3f8fc..9373f1f8a0 100644
--- a/channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
+++ b/channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
@@ -18,7 +18,7 @@
 
     {{ #tournament.user_is_influencer }}
     {{ #tournament.influencer_in_review }}
-    <button class="btn influence-btn in-review">
+    <button class="btn influence-btn in-review page-opener" data-page-opener="/{{ tournament.user_influencer_infos.vanity_url }}/">
         {{_i18n}}In Review{{/i18n}}
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git add .
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git log
commit b193af3e21b836f4b0443640c120e5fffd3ef913 (HEAD -> 927-enhacement/influencer-page-display, origin/develop, origin/HEAD, develop)
Merge: 1743d28249 227dd564ac
Author: Chris Statzer <chris.statzer@gmail.com>
Date:   Wed Jul 3 08:03:35 2019 +0000

    Merge branch '906-bugfix/sms-btn-click-issue' into 'develop'
    
    Resolve "sms send btn can not clickable"
    
    Closes VIDS-906
    
    See merge request channelfix/channelfix!2824
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git commit -m 'vids-927-repair‘
> ^C
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git commit -m 'vids-927-repair'
[927-enhacement/influencer-page-display a6779fdb2f] vids-927-repair
 2 files changed, 3 insertions(+), 1 deletion(-)
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git log
commit a6779fdb2fe26268cc331e6512da205d62d67141 (HEAD -> 927-enhacement/influencer-page-display)
Author: vsnew05 <1101694369@qq.com>
Date:   Mon Jul 8 17:50:18 2019 +0800

    vids-927-repair

commit b193af3e21b836f4b0443640c120e5fffd3ef913 (origin/develop, origin/HEAD, develop)
Merge: 1743d28249 227dd564ac
Author: Chris Statzer <chris.statzer@gmail.com>
Date:   Wed Jul 3 08:03:35 2019 +0000

    Merge branch '906-bugfix/sms-btn-click-issue' into 'develop'
    
    Resolve "sms send btn can not clickable"
    
    Closes VIDS-906
    
    See merge request channelfix/channelfix!2824

commit 1743d28249115fd798b4d1a263059868874474f8
Merge: fd800e4c53 0323ffc12a
Author: Chris Statzer <chris.statzer@gmail.com>
Date:   Wed Jul 3 08:03:15 2019 +0000

(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git log
commit a6779fdb2fe26268cc331e6512da205d62d67141 (HEAD -> 927-enhacement/influencer-page-display)
Author: vsnew05 <1101694369@qq.com>
Date:   Mon Jul 8 17:50:18 2019 +0800

    vids-927-repair

commit b193af3e21b836f4b0443640c120e5fffd3ef913 (origin/develop, origin/HEAD, develop)
Merge: 1743d28249 227dd564ac
Author: Chris Statzer <chris.statzer@gmail.com>
Date:   Wed Jul 3 08:03:35 2019 +0000

    Merge branch '906-bugfix/sms-btn-click-issue' into 'develop'
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git branch
* 927-enhacement/influencer-page-display
  develop
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git push origin/develop
fatal: 'origin/develop' does not appear to be a git repository
fatal: 无法读取远程仓库。

请确认您有正确的访问权限并且仓库存在。
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git push 
fatal: 当前分支 927-enhacement/influencer-page-display 没有对应的上游分支。
为推送当前分支并建立与远程上游的跟踪，使用

    git push --set-upstream origin 927-enhacement/influencer-page-display

(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git log
commit a6779fdb2fe26268cc331e6512da205d62d67141 (HEAD -> 927-enhacement/influencer-page-display)
Author: vsnew05 <1101694369@qq.com>
Date:   Mon Jul 8 17:50:18 2019 +0800

    vids-927-repair

commit b193af3e21b836f4b0443640c120e5fffd3ef913 (origin/develop, origin/HEAD, develop)
Merge: 1743d28249 227dd564ac
Author: Chris Statzer <chris.statzer@gmail.com>
Date:   Wed Jul 3 08:03:35 2019 +0000

    Merge branch '906-bugfix/sms-btn-click-issue' into 'develop'
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git status
位于分支 927-enhacement/influencer-page-display
无文件要提交，干净的工作区
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git commt --amend
git：'commt' 不是一个 git 命令。参见 'git --help'。

最相似的命令是
        commit
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git commt --mend
git：'commt' 不是一个 git 命令。参见 'git --help'。

最相似的命令是
        commit
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git commit --amend
[927-enhacement/influencer-page-display 6d669b39a0] Fix influencer page in review url
 Date: Mon Jul 8 17:50:18 2019 +0800
 2 files changed, 3 insertions(+), 1 deletion(-)
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git log
commit 6d669b39a00d3801ad11a82b4cf66526c6e762d5 (HEAD -> 927-enhacement/influencer-page-display)
Author: vsnew05 <1101694369@qq.com>
Date:   Mon Jul 8 17:50:18 2019 +0800

    Fix influencer page in review url

commit b193af3e21b836f4b0443640c120e5fffd3ef913 (origin/develop, origin/HEAD, develop)
Merge: 1743d28249 227dd564ac
Author: Chris Statzer <chris.statzer@gmail.com>
Date:   Wed Jul 3 08:03:35 2019 +0000

    Merge branch '906-bugfix/sms-btn-click-issue' into 'develop'
    
    Resolve "sms send btn can not clickable"
    
    Closes VIDS-906
    
    See merge request channelfix/channelfix!2824

commit 1743d28249115fd798b4d1a263059868874474f8
Merge: fd800e4c53 0323ffc12a
Author: Chris Statzer <chris.statzer@gmail.com>
Date:   Wed Jul 3 08:03:15 2019 +0000

    Merge branch 'VIDS-644-enhancement/enhance-swagger' into 'develop'
    
    enhance swagger
    
    Closes VIDS-644
    
    See merge request channelfix/channelfix!2821

commit fd800e4c537b3e375ac62663c6bd9f5349a8a0cb
Merge: 8fef2529f2 cc8507e03a
Author: Chris Statzer <chris.statzer@gmail.com>
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git status
位于分支 927-enhacement/influencer-page-display
无文件要提交，干净的工作区
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git push origin 927-enhacement/influencer-page-display
对象计数中: 58, 完成.
Delta compression using up to 6 threads.
压缩对象中: 100% (39/39), 完成.
写入对象中: 100% (58/58), 7.16 KiB | 7.16 MiB/s, 完成.
Total 58 (delta 45), reused 23 (delta 16)
remote: 
remote: To create a merge request for 927-enhacement/influencer-page-display, visit:
remote:   https://forge.channelfix.com/channelfix/channelfix/merge_requests/new?merge_request%5Bsource_branch%5D=927-enhacement%2Finfluencer-page-display
remote: 
To forge.channelfix.com:channelfix/channelfix.git
 * [new branch]            927-enhacement/influencer-page-display -> 927-enhacement/influencer-page-display
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git config
用法：git config [<选项>]

配置文件位置
    --global              使用全局配置文件
    --system              使用系统级配置文件
    --local               使用仓库级配置文件
    -f, --file <文件>     使用指定的配置文件
    --blob <数据对象 ID>  从给定的数据对象读取配置

操作
    --get                 获取值：name [value-regex]
    --get-all             获得所有的值：key [value-regex]
    --get-regexp          根据正则表达式获得值：name-regex [value-regex]
    --get-urlmatch        获得 URL 取值：section[.var] URL
    --replace-all         替换所有匹配的变量：name value [value_regex]
    --add                 添加一个新的变量：name value
    --unset               删除一个变量：name [value-regex]
    --unset-all           删除所有匹配项：name [value-regex]
    --rename-section      重命名小节：old-name new-name
    --remove-section      删除一个小节：name
    -l, --list            列出所有
    -e, --edit            打开一个编辑器
    --get-color           获得配置的颜色：配置 [默认]
    --get-colorbool       获得颜色设置：配置 [stdout-is-tty]

类型
    --bool                值是 "true" 或 "false"
    --int                 值是十进制数
    --bool-or-int         值是 --bool or --int
    --path                值是一个路径（文件或目录名）
    --expiry-date         值是一个到期日期

其它
    -z, --null            终止值是 NUL 字节
    --name-only           只显示变量名
    --includes            查询时参照 include 指令递归查找
    --show-origin         显示配置的来源（文件、标准输入、数据对象，或命令行）

(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git config --list
user.name=vsnew05
user.email=1101694369@qq.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
remote.origin.url=git@forge.channelfix.com:channelfix/channelfix.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.develop.remote=origin
branch.develop.merge=refs/heads/develop
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git config --global user.name "Zhou Zhikai"
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git config --global user.email "zhouzhikai@vidsai.com"
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git log
commit 6d669b39a00d3801ad11a82b4cf66526c6e762d5 (HEAD -> 927-enhacement/influencer-page-display, origin/927-enhacement/influencer-page-display)
Author: vsnew05 <1101694369@qq.com>
Date:   Mon Jul 8 17:50:18 2019 +0800

    Fix influencer page in review url

commit b193af3e21b836f4b0443640c120e5fffd3ef913 (origin/develop, origin/HEAD, develop)
Merge: 1743d28249 227dd564ac
Author: Chris Statzer <chris.statzer@gmail.com>
Date:   Wed Jul 3 08:03:35 2019 +0000

    Merge branch '906-bugfix/sms-btn-click-issue' into 'develop'
    
    Resolve "sms send btn can not clickable"
    
    Closes VIDS-906
    
    See merge request channelfix/channelfix!2824

commit 1743d28249115fd798b4d1a263059868874474f8
Merge: fd800e4c53 0323ffc12a
Author: Chris Statzer <chris.statzer@gmail.com>
Date:   Wed Jul 3 08:03:15 2019 +0000

    Merge branch 'VIDS-644-enhancement/enhance-swagger' into 'develop'
    
    enhance swagger
    
    Closes VIDS-644
    
    See merge request channelfix/channelfix!2821

commit fd800e4c537b3e375ac62663c6bd9f5349a8a0cb
Merge: 8fef2529f2 cc8507e03a
Author: Chris Statzer <chris.statzer@gmail.com>
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git reset b193af3e21b836f4b0443640c120e5fffd3ef913
重置后取消暂存的变更：
M       channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
M       channelfix/site/static/site/js/tournament/tournament_influencer_section.js
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git status
位于分支 927-enhacement/influencer-page-display
尚未暂存以备提交的变更：
  （使用 "git add <文件>..." 更新要提交的内容）
  （使用 "git checkout -- <文件>..." 丢弃工作区的改动）

        修改：     channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
        修改：     channelfix/site/static/site/js/tournament/tournament_influencer_section.js

修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git add .
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git stauts
git：'stauts' 不是一个 git 命令。参见 'git --help'。

最相似的命令是
        status
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git status
位于分支 927-enhacement/influencer-page-display
要提交的变更：
  （使用 "git reset HEAD <文件>..." 以取消暂存）

        修改：     channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
        修改：     channelfix/site/static/site/js/tournament/tournament_influencer_section.js

尚未暂存以备提交的变更：
  （使用 "git add <文件>..." 更新要提交的内容）
  （使用 "git checkout -- <文件>..." 丢弃工作区的改动）

        修改：     channelfix/site/static/site/js/tournament/tournament_influencer_section.js

(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git add .
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git commit -m 'Fix influencer page in review url
> 
> commit b193af3e21b836f4b0443640c120e5fffd3ef913 (origin/develop, origin/HEAD, develop)
> Merge: 1743d28249 227dd564ac
> Author: Chris Statzer <chris.statzer@gmail.com>
> Date:   Wed Jul 3 08:03:35 2019 +0000
> 
>     Merge branch '906-bugfix/sms-btn-click-issue' into 'develop'
>     
>     Resolve "sms send btn can not clickable"
>     
>     Closes VIDS-906
>     
>     See merge request channelfix/channelfix!2824
> 
> commit 1743d28249115fd798b4d1a263059868874474f8
> Merge: fd800e4c53 0323ffc12a
> Author: Chris Statzer <chris.statzer@gmail.com>
> Date:   Wed Jul 3 08:03:15 2019 +0000
> 
>     Merge branch 'VIDS-644-enhancement/enhance-swagger' into 'develop'
>     
>     enhance swagger
>     
>     Closes VIDS-644
>     
>     See merge request channelfix/channelfix!2821
> 
> commit fd800e4c537b3e375ac62663c6bd9f5349a8a0cb
> Merge: 8fef2529f2 cc8507e03a
> Author: Chris Statzer <chris.statzer@gmail.com>
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git reset b193af3e21b836f4b0443640c120e5fffd3ef913
> 重置后取消暂存的变更：
> M       channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
> M       channelfix/site/static/site/js/tournament/tournament_influencer_section.js
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git status
> 位于分支 927-enhacement/influencer-page-display
> 尚未暂存以备提交的变更：
>   （使用 "git add <文件>..." 更新要提交的内容）
>   （使用 "git checkout -- <文件>..." 丢弃工作区的改动）
> 
>         修改：     channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
>         修改：     channelfix/site/static/site/js/tournament/tournament_influencer_section.js
> 
> 修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git add .
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git stauts
> git：'stauts' 不是一个 git 命令。参见 'git --help'。
> 
> 最相Fix influencer page in review url
> 
> commit b193af3e21b836f4b0443640c120e5fffd3ef913 (origin/develop, origin/HEAD, develop)
> Merge: 1743d28249 227dd564ac
> Author: Chris Statzer <chris.statzer@gmail.com>
> Date:   Wed Jul 3 08:03:35 2019 +0000
> 
>     Merge branch '906-bugfix/sms-btn-click-issue' into 'develop'
>     
>     Resolve "sms send btn can not clickable"
>     
>     Closes VIDS-906
>     
>     See merge request channelfix/channelfix!2824
> 
s> commit 1743d28249115fd798b4d1a263059868874474f8
> Merge: fd800e4c53 0323ffc12a
> Author: Chris Statzer <chris.statzer@gmail.com>
> Date:   Wed Jul 3 08:03:15 2019 +0000
> 
>     Merge branch 'VIDS-644-enhancement/enhance-swagger' into 'develop'
>     
>     enhance swagger
>     
>     Closes VIDS-644
>     
>     See merge request channelfix/channelfix!2821
> 
> commit fd800e4c537b3e375ac62663c6bd9f5349a8a0cb
> Merge: 8fef2529f2 cc8507e03a
> Author: Chris Statzer <chris.statzer@gmail.com>
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git reset b193af3e21b836f4b0443640c120e5fffd3ef913
> 重置后取消暂存的变更：
> M       channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
> M       channelfix/site/static/site/js/tournament/tournament_influencer_section.js
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git status
> 位于分支 927-enhacement/influencer-page-display
> 尚未暂存以备提交的变更：
>   （使用 "git add <文件>..." 更新要提交的内容）
>   （使用 "git checkout -- <文件>..." 丢弃工作区的改动）
> 
>         修改：     channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
>         修改：     channelfix/site/static/site/js/tournament/tournament_influencer_section.js
> 
> 修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git add .
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git stauts
> git：'stauts' 不是一个 git 命令。参见 'git --help'。
> 
> 最相Fix influencer page in review url
> 
> commit b193af3e21b836f4b0443640c120e5fffd3ef913 (origin/develop, origin/HEAD, develop)
> Merge: 1743d28249 227dd564ac
> Author: Chris Statzer <chris.statzer@gmail.com>
> Date:   Wed Jul 3 08:03:35 2019 +0000
> 
>     Merge branch '906-bugfix/sms-btn-click-issue' into 'develop'
>     
>     Resolve "sms send btn can not clickable"
>     
>     Closes VIDS-906
>     
>     See merge request channelfix/channelfix!2824
> 
> commit 1743d28249115fd798b4d1a263059868874474f8
> Merge: fd800e4c53 0323ffc12a
> Author: Chris Statzer <chris.statzer@gmail.com>
> Date:   Wed Jul 3 08:03:15 2019 +0000
> 
>     Merge branch 'VIDS-644-enhancement/enhance-swagger' into 'develop'
>     
>     enhance swagger
>     
>     Closes VIDS-644
>     
>     See merge request channelfix/channelfix!2821
> 
> commit fd800e4c537b3e375ac62663c6bd9f5349a8a0cb
> Merge: 8fef2529f2 cc8507e03a
> Author: Chris Statzer <chris.statzer@gmail.com>
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git reset b193af3e21b836f4b0443640c120e5fffd3ef913
> 重置后取消暂存的变更：
> M       channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
> M       channelfix/site/static/site/js/tournament/tournament_influencer_section.js
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git status
> 位于分支 927-enhacement/influencer-page-display
> 尚未暂存以备提交的变更：
>   （使用 "git add <文件>..." 更新要提交的内容）
>   （使用 "git checkout -- <文件>..." 丢弃工作区的改动）
> 
>         修改：     channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
>         修改：     channelfix/site/static/site/js/tournament/tournament_influencer_section.js
> 
> 修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git add .
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git stauts
> git：'stauts' 不是一个 git 命令。参见 'git --help'。
> 
> 最相Fix influencer page in review url
> 
> commit b193af3e21b836f4b0443640c120e5fffd3ef913 (origin/develop, origin/HEAD, develop)
> Merge: 1743d28249 227dd564ac
> Author: Chris Statzer <chris.statzer@gmail.com>
> Date:   Wed Jul 3 08:03:35 2019 +0000
> 
>     Merge branch '906-bugfix/sms-btn-click-issue' into 'develop'
>     
>     Resolve "sms send btn can not clickable"
>     
>     Closes VIDS-906
>     
>     See merge request channelfix/channelfix!2824
> 
> commit 1743d28249115fd798b4d1a263059868874474f8
> Merge: fd800e4c53 0323ffc12a
> Author: Chris Statzer <chris.statzer@gmail.com>
> Date:   Wed Jul 3 08:03:15 2019 +0000
> 
>     Merge branch 'VIDS-644-enhancement/enhance-swagger' into 'develop'
>     
>     enhance swagger
>     
>     Closes VIDS-644
>     
>     See merge request channelfix/channelfix!2821
> 
> commit fd800e4c537b3e375ac62663c6bd9f5349a8a0cb
> Merge: 8fef2529f2 cc8507e03a
> Author: Chris Statzer <chris.statzer@gmail.com>
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git reset b193af3e21b836f4b0443640c120e5fffd3ef913
> 重置后取消暂存的变更：
> M       channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
> M       channelfix/site/static/site/js/tournament/tournament_influencer_section.js
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git status
> 位于分支 927-enhacement/influencer-page-display
> 尚未暂存以备提交的变更：
>   （使用 "git add <文件>..." 更新要提交的内容）
>   （使用 "git checkout -- <文件>..." 丢弃工作区的改动）
> 
>         修改：     channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
>         修改：     channelfix/site/static/site/js/tournament/tournament_influencer_section.js
> 
> 修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git add .
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git stauts
> git：'stauts' 不是一个 git 命令。参见 'git --help'。
> 
> 最相Fix influencer page in review url
> 
> commit b193af3e21b836f4b0443640c120e5fffd3ef913 (origin/develop, origin/HEAD, develop)
> Merge: 1743d28249 227dd564ac
> Author: Chris Statzer <chris.statzer@gmail.com>
> Date:   Wed Jul 3 08:03:35 2019 +0000
> 
>     Merge branch '906-bugfix/sms-btn-click-issue' into 'develop'
>     
>     Resolve "sms send btn can not clickable"
>     
>     Closes VIDS-906
>     
>     See merge request channelfix/channelfix!2824
> 
> commit 1743d28249115fd798b4d1a263059868874474f8
> Merge: fd800e4c53 0323ffc12a
> Author: Chris Statzer <chris.statzer@gmail.com>
> Date:   Wed Jul 3 08:03:15 2019 +0000
> 
>     Merge branch 'VIDS-644-enhancement/enhance-swagger' into 'develop'
>     
>     enhance swagger
>     
>     Closes VIDS-644
>     
>     See merge request channelfix/channelfix!2821
> 
> commit fd800e4c537b3e375ac62663c6bd9f5349a8a0cb
> Merge: 8fef2529f2 cc8507e03a
> Author: Chris Statzer <chris.statzer@gmail.com>
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git reset b193af3e21b836f4b0443640c120e5fffd3ef913
> 重置后取消暂存的变更：
> M       channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
> M       channelfix/site/static/site/js/tournament/tournament_influencer_section.js
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git status
> 位于分支 927-enhacement/influencer-page-display
> 尚未暂存以备提交的变更：
>   （使用 "git add <文件>..." 更新要提交的内容）
>   （使用 "git checkout -- <文件>..." 丢弃工作区的改动）
> 
>         修改：     channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html
>         修改：     channelfix/site/static/site/js/tournament/tournament_influencer_section.js
> 
> 修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git add .
> (venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git stauts
> git：'stauts' 不是一个 git 命令。参见 'git --help'。
> 
> :q
> ^C
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git status
位于分支 927-enhacement/influencer-page-display
要提交的变更：
  （使用 "git reset HEAD <文件>..." 以取消暂存）

        修改：     channelfix/site/mustachetemplates/site/mustachetemplates/tournament/partials/tournament_influencer_section.html

(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git add .
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git commit -m 'Fix influencer page in review url'
[927-enhacement/influencer-page-display d0cb513557] Fix influencer page in review url
 1 file changed, 1 insertion(+), 1 deletion(-)
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git log
commit d0cb5135577ec2b4c0b4fe8011336cd9f1d75e94 (HEAD -> 927-enhacement/influencer-page-display)
Author: Zhou Zhikai <zhouzhikai@vidsai.com>
Date:   Mon Jul 8 18:09:09 2019 +0800

    Fix influencer page in review url

commit b193af3e21b836f4b0443640c120e5fffd3ef913 (origin/develop, origin/HEAD, develop)
Merge: 1743d28249 227dd564ac
Author: Chris Statzer <chris.statzer@gmail.com>
Date:   Wed Jul 3 08:03:35 2019 +0000

    Merge branch '906-bugfix/sms-btn-click-issue' into 'develop'
    
    Resolve "sms send btn can not clickable"
    
    Closes VIDS-906
    
    See merge request channelfix/channelfix!2824

commit 1743d28249115fd798b4d1a263059868874474f8
Merge: fd800e4c53 0323ffc12a
Author: Chris Statzer <chris.statzer@gmail.com>
Date:   Wed Jul 3 08:03:15 2019 +0000

    Merge branch 'VIDS-644-enhancement/enhance-swagger' into 'develop'
    
    enhance swagger
    
    Closes VIDS-644
    
    See merge request channelfix/channelfix!2821

commit fd800e4c537b3e375ac62663c6bd9f5349a8a0cb
Merge: 8fef2529f2 cc8507e03a
Author: Chris Statzer <chris.statzer@gmail.com>
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git push -f origin 927-enhacement/influencer-page-display 
对象计数中: 10, 完成.
Delta compression using up to 6 threads.
压缩对象中: 100% (8/8), 完成.
写入对象中: 100% (10/10), 1.95 KiB | 1.95 MiB/s, 完成.
Total 10 (delta 6), reused 0 (delta 0)
remote: 
remote: To create a merge request for 927-enhacement/influencer-page-display, visit:
remote:   https://forge.channelfix.com/channelfix/channelfix/merge_requests/new?merge_request%5Bsource_branch%5D=927-enhacement%2Finfluencer-page-display
remote: 
To forge.channelfix.com:channelfix/channelfix.git
 + 6d669b39a0...d0cb513557 927-enhacement/influencer-page-display -> 927-enhacement/influencer-page-display (forced update)
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git pull origin develop
remote: Enumerating objects: 379, done.
remote: Counting objects: 100% (379/379), done.
remote: Compressing objects: 100% (162/162), done.
remote: Total 379 (delta 256), reused 289 (delta 197)
接收对象中: 100% (379/379), 275.41 KiB | 17.00 KiB/s, 完成.
处理 delta 中: 100% (256/256), 完成 55 个本地对象.
来自 forge.channelfix.com:channelfix/channelfix
 * branch                  develop    -> FETCH_HEAD
   b193af3e21..9613c8ccb9  develop    -> origin/develop
删除 channelfix/site/tests/test_forms/test_report_forms.py
删除 channelfix/site/forms/report_forms.py
Merge made by the 'recursive' strategy.
 channelfix/site/api_sileo/__init__.py                                                            |   1 -
 channelfix/site/api_sileo/report.py                                                              |  53 ++++++++++++--------
 channelfix/site/api_sileo/v2/challenge_friend.py                                                 |   2 +-
 channelfix/site/api_sileo/v2/exclusive.py                                                        |   1 +
 channelfix/site/api_sileo/v2/influencer.py                                                       |  54 +++++++++++++-------
 channelfix/site/api_sileo/v2/miniprogram_auth.py                                                 |   1 +
 channelfix/site/api_sileo/v2/report.py                                                           |  27 +++-------
 channelfix/site/api_sileo/v2/tournament_challenge.py                                             |   2 +-
 channelfix/site/forms/__init__.py                                                                |   2 +-
 channelfix/site/forms/report.py                                                                  |  84 +++++++++++++++++++++++++++++++
 channelfix/site/forms/report_forms.py                                                            |  87 --------------------------------
 channelfix/site/forms/v2/__init__.py                                                             |   2 +-
 channelfix/site/forms/v2/report.py                                                               | 131 ++++++++++++++++++------------------------------
 channelfix/site/models/votebox/validation_votebox.py                                             |   6 +--
 channelfix/site/mustachetemplates/site/mustachetemplates/dmca/report_entry_form.html             |   4 +-
 channelfix/site/mustachetemplates/site/mustachetemplates/tournament/battling/battling_panel.html |  39 +++++++--------
 channelfix/site/mustachetemplates/site/mustachetemplates/tournament/open/open_panel.html         |  40 +++++++--------
 channelfix/site/mustachetemplates/site/mustachetemplates/tournament/ranking/ranking_panel.html   |  13 ++++-
 channelfix/site/preprocessors/user_tasks.py                                                      |   6 +--
 channelfix/site/signals/dmca.py                                                                  |   4 +-
 channelfix/site/static/site/js/dmca/report_entry.js                                              |  55 ++++++++++++--------
 channelfix/site/static/site/js/internationalization/chinese.js                                   |   8 ++-
 channelfix/site/static/site/js/tournament/battling/match_details.js                              |   6 ++-
 channelfix/site/static/site/js/tournament/open/tournament_hud_section.js                         |   3 ++
 channelfix/site/static/site/js/tournament/sorting/entries_list.js                                |   2 +-
 channelfix/site/static/site/js/tournament/sorting/tournament_hud_section.js                      |   9 ++--
 channelfix/site/static/site/js/tournament/tournament_info_section.js                             |   1 +
 channelfix/site/static/site/js/tournament/tournament_video_metadata_overlay.js                   |  20 +++++++-
 channelfix/site/static/site/js/tournament/winners_page.js                                        |   2 +-
 channelfix/site/templates/site/dmca/form.html                                                    |  31 ++++++------
 channelfix/site/templates/site/mobile_error_codes/v2/cn/errors.json                              |   4 +-
 channelfix/site/templates/site/mobile_error_codes/v2/en-us/errors.json                           |   4 +-
 channelfix/site/tests/test_api_sileo/test_report.py                                              |   2 +-
 channelfix/site/tests/test_api_sileo/test_v2/test_influencer.py                                  |  12 ++++-
 channelfix/site/tests/test_api_sileo/test_v2/test_report.py                                      |   2 +-
 channelfix/site/tests/test_forms/test_report_forms.py                                            | 171 --------------------------------------------------------------
 channelfix/site/tests/test_forms/test_v2/test_report.py                                          | 172 +++++++++++++++++++++++++++++++++++++++++++--------------------
 channelfix/site/tests/test_preprocessors/test_user_tasks.py                                      |  12 ++---
 channelfix/site/tests/test_signals/test_dmca.py                                                  |   4 +-
 channelfix/site/tests/test_views/test_dmca_views.py                                              |  32 ++++++------
 channelfix/site/views/dmca.py                                                                    |  94 +++++++++++++++++++---------------
 channelfix/site/views/swagger.py                                                                 |   7 ++-
 ministry/forms/dmca_forms.py                                                                     |   4 +-
 ministry/forms/secondary_category_forms.py                                                       |   2 +-
 ministry/static/ministry/js/internationalization/chinese.js                                      |   1 +
 ministry/static/ministry/js/secondary_category/utils.js                                          |   1 +
 ministry/templates/ministry/secondary_category/detail.html                                       |   4 ++
 ministry/tests/factories/plex_factories.py                                                       |   4 +-
 ministry/tests/test_dmcas/test_report.py                                                         |  26 +++++-----
 ministry/views/dashboard.py                                                                      |   4 +-
 ministry/views/dmca.py                                                                           |  16 +++---
 plex/contrib/dmca/admin.py                                                                       |   4 +-
 plex/contrib/dmca/forms.py                                                                       |  34 ++++++++++---
 plex/contrib/dmca/migrations/0007_rename_dmca_model.py                                           |  27 ++++++++++
 plex/contrib/dmca/models.py                                                                      |  19 ++++---
 plex/contrib/dmca/test.py                                                                        |   6 +--
 plex/contrib/video/migrations/0030_secondarycategory_qq_group_key.py                             |  20 ++++++++
 plex/contrib/video/models.py                                                                     |   1 +
 sass/components/player.override.scss                                                             |   1 +
 sass/pages/tournament.new.scss                                                                   |  22 +++++++-
 tournament/base_tournament/models/rejection_reason.py                                            |   2 +
 61 files changed, 729 insertions(+), 681 deletions(-)
 create mode 100644 channelfix/site/forms/report.py
 delete mode 100644 channelfix/site/forms/report_forms.py
 delete mode 100644 channelfix/site/tests/test_forms/test_report_forms.py
 create mode 100644 plex/contrib/dmca/migrations/0007_rename_dmca_model.py
 create mode 100644 plex/contrib/video/migrations/0030_secondarycategory_qq_group_key.py
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git log
commit e5ed0c939b041677d0f993f3862087724f9af7b9 (HEAD -> 927-enhacement/influencer-page-display)
Merge: d0cb513557 9613c8ccb9
Author: Zhou Zhikai <zhouzhikai@vidsai.com>
Date:   Mon Jul 8 18:14:35 2019 +0800

    Merge branch 'develop' of forge.channelfix.com:channelfix/channelfix into 927-enhacement/influencer-page-display

commit d0cb5135577ec2b4c0b4fe8011336cd9f1d75e94 (origin/927-enhacement/influencer-page-display)
Author: Zhou Zhikai <zhouzhikai@vidsai.com>
Date:   Mon Jul 8 18:09:09 2019 +0800

    Fix influencer page in review url

commit 9613c8ccb94060c3296d7695da91a9886e44d0c9 (origin/develop, origin/HEAD)
Merge: bed000a8dd 02bfa0a68f
Author: Chris Statzer <chris.statzer@gmail.com>
Date:   Sun Jul 7 23:15:58 2019 +0000

    Merge branch '930-bugfix/CaptchaBox-limit-fix' into 'develop'
    
    remove check for tournament is challenge for CaptchaBox
    
    Closes VIDS-930
    
    See merge request channelfix/channelfix!2836

commit bed000a8dd630dda72b1c7f602f6b292ece85b24
Merge: 047d15dec2 b30b1e903f
Author: Chris Statzer <chris.statzer@gmail.com>
Date:   Sun Jul 7 23:15:50 2019 +0000

    Merge branch '898-task/report-tournament' into 'develop'
    
    rename model report to dmcareport and fix the old api
    
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ 
(venv) vsnew05@vsnew05:~/Desktop/buildout-next/src/channelfix$ git push origin 927-enhacement/influencer-page-display 
对象计数中: 8, 完成.
Delta compression using up to 6 threads.
压缩对象中: 100% (6/6), 完成.
写入对象中: 100% (8/8), 1.90 KiB | 1.90 MiB/s, 完成.
Total 8 (delta 4), reused 0 (delta 0)
remote: 
remote: View merge request for 927-enhacement/influencer-page-display:
remote:   https://forge.channelfix.com/channelfix/channelfix/merge_requests/2846
remote: 
To forge.channelfix.com:channelfix/channelfix.git
   d0cb513557..e5ed0c939b  927-enhacement/influencer-page-display -> 927-enhacement/influencer-page-display