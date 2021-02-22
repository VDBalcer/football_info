from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('players/', views.index, name = 'Main'),
    path('players/<int:id>', views.player_page),
]
