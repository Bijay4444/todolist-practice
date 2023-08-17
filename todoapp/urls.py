
from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('delete/<id>', views.delete),
    path('edit/<id>', views.edit),
    path('mark_completed/<id>', views.mark_completed),
]
