from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from .models import Info
from .form import Info_Form

class Info_ListView(ListView):
    model = Info

class Info_DetailView(DetailView):
    model = Info


class Info_CreateView(CreateView):
    model = Info
    form_class = Info_Form
    #fields = [ "name"  ]
    #sucess_rul = "http://www.yahoo.co.jp"   # ERROR
    #sucess_rul = reverse_lazy("index_info") # ERROR
    # must function define?
    def get_success_url(self):
        url = "http://www.yahoo.co.jp"
        sucess_rul = reverse_lazy("index_info")
        return sucess_rul

class Info_UpdateView(UpdateView):
    model = Info
    #fields = ["name"]
    form_class = Info_Form

    def get_success_url(self):
        getID = self.kwargs["pk"]
        url = reverse_lazy( "detail_info" , kwargs = { "pk" : getID } )
        return url


class Info_DeleteView(DeleteView):
    model = Info
    def get_success_url(self):
        sucess_rul = reverse_lazy("index_info")
        return sucess_rul


def main(request):
    return HttpResponse( "<b>Sub Main Page</b><br> page info" )


def summary(request):
    return HttpResponse( "info summary summary" )


