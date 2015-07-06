# a demo of leancloud which use tornado framework


#[leancloud自带文档](https://leancloud.cn/docs/leanengine_guide-python.html)

# 本地运行环境
* [nodejs](http://nodejs.org/)
* [python2.7](https://www.python.org/)
* Windows、Linux 或 MacOS 操作系统

# 本地部署

## 下载源码

`git clone https://github.com/stableShip/leancloud_tornado.git`

## 修改leancloud配置信息
`vi ./configs/development.conf` 将项目的leancloud信息填写进去


## 安装依赖包 
进入目录：
`cd leancloud_tornado`

安装依赖包：
`pip install -Ur requirements.txt`

##运行:
`python wsgi.py` 或者 `avoscloud` 访问[ http://localhost:3000 ]

#部署到leancloud:

##[安装leancloud命令行工具](https://leancloud.cn/docs/cloud_code_commandline.html):
`npm install -g avoscloud-code`

##添加应用信息：

 `cd leancloud_tornado`
 
 `avoscloud add <appName> <appId>`

##设置webhosting:
[相关链接](https://leancloud.cn/docs/leanengine_guide-python.html#Web_Hosting)

##发布到leancloud中:

`avoscloud deploy` 访问 dev.yourAPP.avosapps.com

`avoscloud publish` 访问 yourAPP.avosapps.com




