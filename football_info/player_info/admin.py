from django.contrib import admin
from .models import Player, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'pub_date', 'text')
    search_fields = ('author',)
    list_filter = ('pub_date',)
    empty_value_display = "-Гость-"


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth')
    search_fields = ('name',)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Player, PlayerAdmin)
