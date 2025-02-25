from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('next_page/', views.next_page),
    path('aria-glass-coffee-table/', views.coffee_table),
    path('aurora-5-row-standing-shelf/', views.aurora_shelf),
    path('aurora-pendant-lamp/', views.pendant_lamp),
]