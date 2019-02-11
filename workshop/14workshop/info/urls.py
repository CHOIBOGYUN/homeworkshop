from django.urls import path
from . import views

urlpatterns = [
    path("", views.info),    
    path("student/<str:title>",views.student),
]