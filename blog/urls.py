from django.conf.urls import url , include
from django.contrib import admin
from django.contrib.auth import views as auth_views


from blog import views
#import  blog.views.CLASS_VIEW  as CLASS_VIEW



urlpatterns = [

    url(r'^$', views.main, name="index_blog"),
    #url(r"^aa/list$"                                 , CLASS_VIEW.VIEW_LIST.as_view(),     name="aftereffects_list")

]