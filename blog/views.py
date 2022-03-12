 

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("This is home page of shop")
    params = {'name': 'templete index'}
    return render(request, 'index.html', params)
def    aboutBlog(request):
    # return HttpResponse("This is home page of shop")
    params = {'name': 'templete blog about'}
    return render(request, 'aboutB.html', params)
def   contactBlog(request):
    # return HttpResponse("This is home page of shop")
    params = {'name': 'templete blog  contact'}
    return render(request, 'contactB.html', params)
def    temBindex(request):
    # return HttpResponse("This is home page of shop")
    params = {'name': 'templete  blog index'}
    return render(request, 'index_temB.html', params)