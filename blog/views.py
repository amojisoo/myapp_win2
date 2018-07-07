from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response


def main(request):
    return HttpResponse( "<b>Sub Main Page</b><br> page info" )