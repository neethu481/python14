from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def productinfo(req):
    template=loader.get_template("productinfo.html")
    data={"name":"Vivo",
          "desc":"Smartphone",
          "price":455555
          }
    return HttpResponse(template.render(data,req))

