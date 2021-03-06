from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin_console', views.admin_console, name="admin_console"),
    path('<int:pk>/details/', views.details, name="details"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    #path('confirm_delete/', views.confirmed, name="confirmed"),
    path('add_profile/', views.add_profile, name="add_profile"),
]
