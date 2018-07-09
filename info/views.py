from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.urls import reverse_lazy
from django.contrib import messages


from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from .models import Info
from .form import Info_Form

class Info_ListView(ListView):
    model = Info
    paginate_by = 10
    #context_object_name = "infos"

class Info_DetailView(DetailView):
    model = Info


class Info_CreateView(CreateView):
    model = Info
    form_class = Info_Form
    #fields = [ "name"  ]
    #sucess_rul = "http://www.yahoo.co.jp"   # ERROR
    #sucess_rul = reverse_lazy("index_info") # ERROR
    # must function define?
    template_name = "info/info_create.html"

    def get_success_url(self):
        url = "http://www.yahoo.co.jp"
        sucess_rul = reverse_lazy("index_info")
        return sucess_rul

    def form_valid(self, form):
        messages.success( self.request, "Saved" )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error( self.request , "Save Filed")
        return super().form_invalid(form)

class Info_UpdateView(UpdateView):
    model = Info
    #fields = ["name"]
    form_class = Info_Form
    template_name = "info/info_update.html"

    def get_success_url(self):
        getID = self.kwargs["pk"]
        url = reverse_lazy( "detail_info" , kwargs = { "pk" : getID } )
        return url

    def form_valid(self, form):
        messages.success( self.request, "Edit Update" )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error( self.request , "Edit Filed")
        return super().form_invalid(form)

class Info_DeleteView(DeleteView):
    model = Info
    def get_success_url(self):
        sucess_rul = reverse_lazy("index_info")
        return sucess_rul

    def delete(self, request, *args, **kwargs):
        messages.success(self.request , "Delete OK" )
        return super().delete(request , *args , **kwargs )

def main(request):
    return HttpResponse( "<b>Sub Main Page</b><br> page info" )


def summary(request):
    return HttpResponse( "info summary summary" )


