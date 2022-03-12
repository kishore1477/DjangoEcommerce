from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from shop.models import Product
# Create your views here.
data =  Product.objects.all() 
# Pname = data[0].product_name
Pname = data[0]

# print("This is product name of watch" + Pname)
# print("This is product name of watch" + Pname)
print(data[1].desc)
# print(data)
# print(data.product_name)

data =  Product.objects.all() 
P1 =  data[0]
P1_desc  = P1.desc
print(P1.desc)
def index(request):
    # return HttpResponse("This is home page of shop")
    
    params = {'name': 'templete index'}
    return render(request, 'index.html', params)
def   temSindex(request):
    # return HttpResponse("This is home page of shop")
    data =  Product.objects.all() 
    P1 =  data[0]
    P1_desc  = P1.desc
    print(P1.desc)
    
    params = {'Product': P1, 'desc': P1_desc}
    return render(request, 'index_temS.html', params)
def  about(request):
    # return HttpResponse("This is home page of shop")
    params = {'name': 'templete shop  about'}
    return render(request, 'about.html', params)
def   contact(request):
    # return HttpResponse("This is home page of shop")
    params = {'name': 'templete shop   contact'}
    return render(request, 'contact.html', params)
def    tracker(request):
    return HttpResponse("This is  tracker page of shop")
   
    # return render(request, 'contact.html',)
def    search(request):
    return HttpResponse("This is  search page of shop")
    # return render(request, 'contact.html',  )
def     prodView(request):
    return HttpResponse("This is   productView page of shop")
    # return render(request, 'contact.html',  )
def     checkout(request):
    return HttpResponse("This is   checkout page of shop")
    # return render(request, 'contact.html',  )
