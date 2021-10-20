from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('room/', views.room, name='room'),
]
