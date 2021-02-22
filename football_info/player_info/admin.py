from django.contrib import admin
from .models import Player, Comment, ProfileViewing


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'pub_date', 'text',)
    search_fields = ('author',)
    list_filter = ('pub_date',)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth',)
    search_fields = ('name',)


class ProfileViewingAdmin(admin.ModelAdmin):
    list_display = ('player', 'ip',)
    list_filter = ('player',)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(ProfileViewing, ProfileViewingAdmin)
