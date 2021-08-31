from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # localhost:8000/index/
    path('index/', views.index, name='index'),
    # greeting
    path('greeting/', views.greeting, name='greeting'),
    # dinner
    path('dinner/', views.dinner, name='dinner'),
    path('dtl-practice/', views.dtl_practice, name='dtl_practice'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<name>/', views.hello, name='hello'),
]
