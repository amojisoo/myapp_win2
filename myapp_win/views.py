from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

import datetime

def main(request):
    html = """
"Main Page  DJango"
    <br><a href = "./blog/"> blog </a>
    <br><a href = "./info/"> info </a>

    """

    return HttpResponse( html  )


def time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def jump(request):
    return HttpResponseRedirect("http://www.yahoo.co.jp/")

def temp(request):
    return render_to_response('ABS_ColorAdmin/ONE_PAGE.html', {'name': u'Alice'})

def forum(request):
    return render_to_response('ABS_ColorAdmin/FORUM_index.html', {'name': u'Alice'})

def login(request):
    html = "<html><body>Login</body></html>"
    return HttpResponse(html)