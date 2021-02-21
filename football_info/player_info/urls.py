from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.index),
    path('players/<int:id>', views.player_page),
]
