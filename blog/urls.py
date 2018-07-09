from django.urls import path
from django.conf.urls import url , include
from django.contrib import admin
from django.contrib.auth import views as auth_views


from blog import views
#import  blog.views.CLASS_VIEW  as CLASS_VIEW

from blog.views import BlogListView
from blog.views import BlogDetailView

urlpatterns = [

    path(''   , BlogListView.as_view()    , name="list"),
    path('<int:pk>', BlogDetailView.as_view(), name="detail"),

    path('summary/', views.summary, name="index_blog"),

    #url(r"^aa/list$"   , CLASS_VIEW.VIEW_LIST.as_view(),     name="aftereffects_list")

]

