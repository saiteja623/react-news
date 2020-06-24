from django.urls import path,include
from newsapp import views

urlpatterns = [
    path('getnews<str:category>',views.getnews,name="getnews"),
    path('getrandom<str:query>',views.getrandom,name="getrandom")
]
