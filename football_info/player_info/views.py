from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Player, Comment, ProfileViewing
from .forms import CommentForm
from django.views.generic import RedirectView


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    if request.method == 'GET' and request.GET.get('q'):
        players_list = Player.objects.filter(name__contains=request.GET.get('q')).order_by('name')
    else:
        players_list = Player.objects.all().order_by('name')
    return render(request, 'player_info/main_page.html', {'players': players_list})


def player_page(request, id):
    player = Player.objects.filter(id=id)[0]
    comments = Comment.objects.filter(player=player)
    views_count = ProfileViewing.objects.filter(player=player).count()
    message = ''

    if request.method == 'GET':
        viewing = ProfileViewing()
        viewing.ip = get_client_ip(request)
        viewing.player = player
        is_exist_view = ProfileViewing.objects.filter(player=player, ip=viewing.ip).exists()
        if not is_exist_view:
            viewing.save()
            views_count += 1

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.player = player
            new_comment.save()
            message = 'Комментарий успешно создан'
            return HttpResponseRedirect(reverse('Main'))
        else:
            message = 'Хьюстон, у нас пролемы с заполнением'

    form = CommentForm()
    context = {
        'player': player,
        'comments': comments,
        'message': message,
        'form': form,
        'views_count': views_count
    }
    return render(request, 'player_info/player_page.html', context)
