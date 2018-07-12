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





    path("about", views.about , name="about_blog"),
    path("summary", views.summary ,name="summary_blog"),
    path("contact", views.contact, name="contact_blog"),

    path("post", views.post, name="post_blog"),
    path("posts", views.posts, name="posts_blog"),
    path("posts_grid", views.posts_grid, name="posts_grid_blog"),

    path("forum", views.forum, name="forum_blog"),
    path("forum_detail", views.forum_detail, name="forumdetail_blog"),
    path("forum_list", views.forum_list, name="forumlist_blog"),

    path("one", views.one, name="one_blog"),

    path("e_index", views.e_index, name="index_e"),

    path("e_about", views.e_about, name="about_e"),
    path("e_contact", views.e_contat, name="contact_e"),
    path("e_faq", views.e_faq, name="faq_e"),
    path("e_account", views.e_account, name="account_e"),
    path("e_product", views.e_product, name="product_e"),
    path("e_product_detail", views.e_product_detail, name="product_detail_e"),
    path("e_search_results", views.e_search_results, name="search_results__e"),

    path("e_checkout_1", views.e_checkout_1, name="checkout_1"),
    path("e_checkout_2", views.e_checkout_2, name="checkout_2"),
    path("e_checkout_3", views.e_checkout_3, name="checkout_3"),
    path("e_checkout_4", views.e_checkout_4, name="checkout_4"),

    #url(r"^aa/list$"   , CLASS_VIEW.VIEW_LIST.as_view(),     name="aftereffects_list")



]

