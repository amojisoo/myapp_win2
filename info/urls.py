from django.conf.urls import url , include
from django.contrib import admin
from django.contrib.auth import views as auth_views


from info import views
#import  blog.views.CLASS_VIEW  as CLASS_VIEW



urlpatterns = [

    url(r'^$', views.main, name="index_blog"),

    url(r'^summary/$', views.summary , name="None"),
    #url(r"^aa/list$"                                 , CLASS_VIEW.VIEW_LIST.as_view(),     name="aftereffects_list")

]
