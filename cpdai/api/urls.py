from django.urls import path, include
from .views import *

urlpatterns = [
    path("", HelloWorldView.as_view(), name="hello-world"),
  
]