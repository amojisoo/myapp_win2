from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response



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


