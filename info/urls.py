from django.urls import path
from django.conf.urls import url , include
from django.contrib import admin
from django.contrib.auth import views as auth_views


from info import views
#import  blog.views.CLASS_VIEW  as CLASS_VIEW

from info.views import Info_ListView
from info.views import Info_DetailView
from info.views import Info_CreateView
from info.views import Info_UpdateView

urlpatterns = [

    path(''             , Info_ListView.as_view()        , name="index_info"),
    path('<int:pk>/'         , Info_DetailView.as_view()     , name="detail_info"),
    path('<int:pk>/update'    , Info_UpdateView.as_view()     , name="update_info"),
    path('create'    , Info_CreateView.as_view()      , name="create"),

    path('summary', views.summary, name="index_bloag"),

    #url(r"^aa/list$"   , CLASS_VIEW.VIEW_LIST.as_view(),     name="aftereffects_list")

]

