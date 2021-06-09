from django.shortcuts import render
from django.http import HttpResponse
# from .models import ToDoList, Item

# Create your views here.

def index(response):
    # ls = ToDoList.objects.get(id=id)
    # items = ls.item_set.get(id=1)
    # return HttpResponse("<h1>Home</h1>")
    return render(response, "main/index.html", {})

def about(response):
    return render(response, "main/about.html", {})

def portfolio(response):
    return render(response, "main/portfolio.html", {})
    # return HttpResponse("<h1>porfolio</h1>")

def contact(response):
    # return HttpResponse("<h1>contact</h1>")
    return render(response, "main/contact.html", {})
