# zhihu-answers-spider
知乎付费答主爬虫及数据分析与图表展示

> 简介：该系统基于Python2.7，使用了Django框架搭建web站点，主要爬取知乎各个类别付费答主的信息，
并利用Echarts图标分析了各类别的性别比例，平均收入及答主top3推荐。

## 快速开始
1. 克隆项目：
```
git clone https://github.com/nlpdz/zhihu-answers-spider.git
```
2. 安装pip，通过pip安装Django：

```
pip install Django
```
3. 进入到zhihu-answers-spider根目录，运行命令：

```
python manage.py runserver
```
4. 访问各个功能页面，地址为：

```
127.0.0.1:8000/spider                      (开始爬取数据)
127.0.0.1:8000/sex                         (各类别性别分析)
127.0.0.1:8000/pay_money_statistics        (各类别收入分析)
127.0.0.1:8000/top3                        (各类top3答主推荐)
```

## 目录说明

```
├──zhihu----------------------------------根目录</br>
├────zhihu--------------------------------Django项目的核心</br>
├-----└──settings-------------------------配置文件</br>
├-----└──urls-----------------------------路由</br>
├────zhihu_master-------------------------我们创建的app项目</br>
├-----└──migrations-----------------------数据库迁移文件</br>
├-----└──models---------------------------数据库配置文件</br>
├-----└──urls-----------------------------局部路由</br>
├-----└──views----------------------------函数控制文件</br>
├────templates----------------------------html页面集合</br>
├────db.sqlite3---------------------------数据库</br>
├────manage.py----------------------------入口
```

## 开发流程

1. 创建页面  
Templates文件夹下创建html页；
views.py中return页面；
urls.py中注册路径；

2. 创建model  
models.py中建类
确定settings中注册app；
python manage.py makemigrations（保存临时）；
python manage.py migrate（真正创建）；
在views.py中实现相关功能；

3. 修改model  
在models.py中修改；
python manage.py makemigrations；
python manage.py migrate；
更新model失败：给字段增加参数null=True，重新运行；

***未提及的部分请善用开源Django文档以及网络。***
