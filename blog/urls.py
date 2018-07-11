from django.urls import path
from django.conf.urls import url , include
from django.contrib import admin
from django.contrib.auth import views as auth_views


from blog import views
#import  blog.views.CLASS_VIEW  as CLASS_VIEW

from blog.views import BlogListView
from blog.views import BlogDetailView



urlpatterns = [

    path(''   , views.index    , name="index_blog"),
    path('<int:pk>', BlogDetailView.as_view(), name="detail"),

    path('summary/', views.summary, name="index_blog"),

    path('summary/', views.summary, name="index_blog"),

    path("about", views.about , name="about_blog"),
    path("summary", views.summary ,name="summary_blog"),
    path("contact", views.contact, name="contact_blog"),
    path("post", views.post, name="post_blog"),
    path("posts", views.posts, name="posts_blog"),

    path("forum", views.forum, name="forum_blog"),
    path("forumdetail", views.forum_detail, name="forum_blog"),

    path("one", views.one, name="one_blog"),

    #url(r"^aa/list$"   , CLASS_VIEW.VIEW_LIST.as_view(),     name="aftereffects_list")

]

