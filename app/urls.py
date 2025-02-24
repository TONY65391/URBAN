from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('images/', views.images),
    path('next_page/', views.next_page)
]