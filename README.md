## 这是一个自动化报告平台项目
## 包括：登录、注册和结果统计
## 该项目发布在127.0.0.1:8000

## 简单的使用方法：


创建虚拟环境
使用pip安装第三方依赖
修改settings.example.py文件为settings.py
运行migrate命令，创建数据库和数据表
运行python manage.py runserver启动服务器


路由设置：


from django.contrib import admin
from django.urls import path
from django.urls import include
from autoreport import views
from captcha.views import captcha_refresh


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('confirm/', views.user_confirm),
    path('captcha/', include('captcha.urls')),   # 生成验证码
    path('refresh/', captcha_refresh),    # 刷新验证码
]