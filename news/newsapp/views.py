from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def getnews(request,category):
    print("category=",category)
    url="http://newsapi.org/v2/top-headlines?country=in&language=en&category="+ category +"&apiKey=9bbf7a4120b44ab1baa67adc9d561c5b"
    response=requests.get(url)
    res=response.json()
    result=res['articles']
    return JsonResponse({'articles':result})

@csrf_exempt
def getrandom(request,query):
    print("query=",query)
    url="http://newsapi.org/v2/everything?q="+ query+ "&from=2020-05-24&sortBy=publishedAt&apiKey=9bbf7a4120b44ab1baa67adc9d561c5b"
    response=requests.get(url)
    res=response.json()
    result=res['articles']
    return JsonResponse({'articles':result})