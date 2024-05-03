from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:user_id>/', views.update, name='update'),
    path('create/', views.create_user, name='create_user'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
]
