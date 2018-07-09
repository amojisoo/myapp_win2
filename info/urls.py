from django.urls import path
from django.conf.urls import url , include
from django.contrib import admin
from django.contrib.auth import views as auth_views


from info import views
#import  blog.views.CLASS_VIEW  as CLASS_VIEW

from info.views import InfoListView
from info.views import InfoDetailView

urlpatterns = [

    path(''   , InfoListView.as_view()    , name="lista"),
    path('<int:pk>', InfoDetailView.as_view(), name="detaila"),

    path('summary', views.summary, name="index_bloag"),

    #url(r"^aa/list$"   , CLASS_VIEW.VIEW_LIST.as_view(),     name="aftereffects_list")

]

