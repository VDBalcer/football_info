from django.shortcuts import render
from django.http import HttpResponse
from .models import Player


def index(request):
    players_list = Player.objects.all()
    return render(request, 'player_info/main_page.html', {'players': players_list})
