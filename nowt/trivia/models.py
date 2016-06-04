from django.db import models
from django.contrib.sessions.models import Session


class UserSession(models.Model):
    session = models.ForeignKey(Session)  
    game = models.ForeignKey('Game')


class Game(models.Model):
    correct = models.IntegerField(default=0)
    ROUND_CHOICES = (
        (5, 5),
        (10, 10),
        (20, 20),
        (50, 50),
        (100, 100),
        (1000, 1000),
    )
    rounds = models.IntegerField(default=0, choices=ROUND_CHOICES)
    current_round = models.IntegerField(default=1)
    songs_asked = models.ManyToManyField("Song")
    show_title = models.BooleanField(default=True)
    show_artist = models.BooleanField(default=True)

    def __str__(self):
        return "Game: %s" % self.id

class Song(models.Model):
    song_name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    album = models.ForeignKey('Album', null = True, blank=True)

    def __str__(self):
        return self.song_name
class Album(models.Model):
    number = models.IntegerField(default=1)
    pub_year = models.IntegerField(default=1990)
    SEASON_CHOICES = (
            ("FALL", "Fall"),
            ("WNTR", "Winter"),
            ("SPRG", "Spring"),
            ("SUMR", "Summer")
        )
    pub_season = models.CharField(max_length=200, choices=SEASON_CHOICES)

    def __str__(self):
        return "NOW That's What I Call Music! %s" % self.number
