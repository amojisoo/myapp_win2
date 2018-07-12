from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render


from django.views.generic import ListView
from .models import Blog

class BlogListView(ListView):
    model = Blog

from django.views.generic import DetailView
class BlogDetailView(DetailView):
    model = Blog


def main(request):
    return HttpResponse( "<b>Sub Main Page</b><br> page info" )


def summary(request):
    return HttpResponse( "summary" )


def index(request):
    return render_to_response('ABS_ColorAdmin/BLOG_index.html', {'name': u'Alice'})


#-----------------
def about(request):
    return render_to_response('ABS_ColorAdmin/BLOG_about.html', {'name': u'Alice'})


def contact(request):
    return render_to_response('ABS_ColorAdmin/BLOG_contact.html', {'name': u'Alice'})

def posts(request):
    return render_to_response('ABS_ColorAdmin/BLOG_posts.html', {'name': u'Alice'})

def posts_grid(request):
    return render_to_response('ABS_ColorAdmin/BLOG_posts_grid.html', {'name': u'Alice'})


def post(request):
    return render_to_response('ABS_ColorAdmin/BLOG_post.html', {'name': u'Alice'})


#-----------------

def forum(request):
    return render_to_response('ABS_ColorAdmin/FORUM_index.html', {'name': u'Alice'})

def forum_detail(request):
    return render_to_response('ABS_ColorAdmin/FORUM_detail.html', {'name': u'Alice'})

def forum_list(request):
    return render_to_response('ABS_ColorAdmin/FORUM_list.html', {'name': u'Alice'})

#-----------------


def one(request):
    return render(request, 'ABS_ColorAdmin/ONE_PAGE.html')

#-----------------

def e_index(request):
    return render(request, 'ABS_ColorAdmin/E_index.html')



def e_about(request):
    return render(request, 'ABS_ColorAdmin/E_about.html')

def e_contat(request):
    return render(request, 'ABS_ColorAdmin/E_contact.html')

def e_faq(request):
    return render(request, 'ABS_ColorAdmin/E_faq.html')

def e_account(request):
    return render(request, 'ABS_ColorAdmin/E_account.html')

def e_product(request):
    return render(request, 'ABS_ColorAdmin/E_product.html')

def e_product_detail(request):
    return render(request, 'ABS_ColorAdmin/E_product_detail.html')

def e_search_results(request):
    return render(request, 'ABS_ColorAdmin/E_search_results.html')

def e_checkout_1(request):
    return render(request, 'ABS_ColorAdmin/E_checkout_1.html')

def e_checkout_2(request):
    return render(request, 'ABS_ColorAdmin/E_checkout_2.html')

def e_checkout_3(request):
    return render(request, 'ABS_ColorAdmin/E_checkout_3.html')

def e_checkout_4(request):
    return render(request, 'ABS_ColorAdmin/E_checkout_4.html')









