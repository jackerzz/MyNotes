003:
	将项目源码托管到oschina中

	1. 点击头像 -> 修改资料 -> SSH公钥 [如何生成SSH公钥](http://git.mydoc.io/?t=154712)

	2. 创建自己的空仓储，使用 `git config --global user.name "用户名"` 和 `git config --global user.email ***@**.com` 来全局配置提交时用户的名称和邮箱

	3. 使用 `git init` 在本地初始化项目

	4. 使用 `touch README.md` 和 `touch .gitignore` 来创建项目的说明文件和忽略文件；

	5. 使用 `git add .` 将所有文件托管到 git 中

	6. 使用 `git commit -m "init project"` 将项目进行本地提交

	7. 使用 `git remote add origin 仓储地址`将本地项目和远程仓储连接，并使用origin最为远程仓储的别名

	8. 使用 `git push -u origin master` 将本地代码push到仓储中

002:
	ES6中语法使用总结

	1. 使用 `export default` 和 `export` 导出模块中的成员; 对应ES5中的 `module.exports` 和 `export`

	2. 使用 `import ** from **` 和 `import '路径'` 还有 `import {a, b} from '模块标识'` 导入其他模块

	3. 使用箭头函数：`(a, b)=> { return a-b; }`

001：
	1. `computed`属性的结果会被缓存，除非依赖的响应式属性变化才会重新计算。主要当作属性来使用；

	2. `methods`方法表示一个具体的操作，主要书写业务逻辑；
	
	3. `watch`一个对象，键是需要观察的表达式，值是对应回调函数。主要用来监听某些特定数据的变化，从而进行某些具体的业务逻辑操作；可以看作是`computed`和`methods`的结合体；
