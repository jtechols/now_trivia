from django.contrib import admin
from .models import *

# Register your models here.
class SongAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Song Info", {'fields': ['song_name', 'artist', 'album']}),
        ("File Info", {'fields': ['file_name']})
    ]
class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Game Info", {'fields': ['rounds', 'correct', 'current_round', 'show_title', 'show_artist']})
    ]
class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Album Info", {'fields': ['number', 'pub_year', 'pub_season']})
    ]
admin.site.register(Song, SongAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Album, AlbumAdmin)