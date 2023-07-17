
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('display', views.display), 
    path('logout', views.logout),
    path('create', views.create),
    path('create_course', views.create_course),
    path('details/<course_id>', views.details),
    path('delete/<course_id>', views.delete),
    path('edit_show/<course_id>', views.edit_show),
    path('edit/<course_id>', views.edit),
]