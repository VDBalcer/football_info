from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Comment
from .forms import CommentForm


def index(request):
    players_list = Player.objects.all().order_by('name')
    return render(request, 'player_info/main_page.html', {'players': players_list})


def player_page(request, id):
    player = Player.objects.filter(id=id)[0]
    comments = Comment.objects.filter(player=player)
    message = ''

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.player = player
            new_comment.save()
            message = 'Комментарий успешно создан'
        else:
            message = 'Хьюстон, у нас пролемы с заполнением'

    form = CommentForm()
    context = {
        'player': player,
        'comments': comments,
        'message': message,
        'form': form
    }

    return render(request, 'player_info/player_page.html', context)
