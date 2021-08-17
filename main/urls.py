from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    # other paths can be added here
]