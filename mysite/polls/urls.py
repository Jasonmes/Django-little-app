#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

"""
3
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index")
]

"""
4 下一步是要在根 URLconf 文件中指定我们创建的 polls.urls 模块。
在 mysite/urls.py 文件的 urlpatterns 列表里插入一个 include()

"""