from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response



from django.views.generic import ListView
from .models import Info

class InfoListView(ListView):
    model = Info


from django.views.generic import DetailView
class InfoDetailView(DetailView):
    model = Info

def main(request):
    return HttpResponse( "<b>Sub Main Page</b><br> page info" )


def summary(request):
    return HttpResponse( "info summary summary" )


