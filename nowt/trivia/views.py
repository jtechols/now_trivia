from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import *
from .forms import *
from django import forms 
import random

# Create your views here.
def create_game(request):
    if request.method == 'POST':
        form = CreateGame(request.POST)
        if form.is_valid():
            rounds = form.cleaned_data['rounds']
            show_title = form.cleaned_data['show_title']
            show_artist = form.cleaned_data['show_artist']
            new_game = Game(rounds=rounds, show_title=show_title, show_artist=show_artist)
            new_game.save()
            UserSession.objects.get_or_create(
                session_id = request.session.session_key,
                game = new_game 
            )
            return HttpResponseRedirect('/trivia/question')
    else:
        form = CreateGame()
        new_game = Game()
        new_game.save()

    context = {'form': form}
    return render(request, "trivia/create_game.html", context)
def question_view(request):
    user_session = UserSession.objects.filter(session=request.session.session_key)[0]
    current_game = user_session.game
    question_number = current_game.current_round
    correct = current_game.correct
    correct_percentage = (correct * 100) // question_number
    random_idx = random.randint(0, Song.objects.count() - 1)
    song = Song.objects.all()[random_idx]
    i = 0;
    while current_game.songs_asked.filter(id=song.id).exists() and i < Song.objects.count():
        random_idx = random.randint(0, Song.objects.count() - 1)
        song = Song.objects.all()[random_idx]
        i += 1  
    current_game.songs_asked.add(song)
    choice_list = [0,0,0,0]
    index_list = []
    random_i = random.randint(0, 3)
    choice_list[random_i] = song.album.number
    for i in range(4):
        if i != random_i:
            choice = random.randint(0, 58)
            while (choice != song.album.number):
                choice = random.randint(0, 58)
            choice_list[i] = choice
    context = {'game': current_game,'song': song,'correct_percentage': correct_percentage, 'choice_list': choice_list}
    return render(request, "trivia/question.html", context)
def question_answer(request, song_id, answer):
    user_session = UserSession.objects.filter(session=request.session.session_key)[0]
    current_game = user_session.game
    song = Song.objects.filter(id=song_id)[0]
    correct_answer = False
    last_question = False
    if song.album.number == answer:
        correct_answer = True
    if current_game.current_round == current_game.rounds:
        last_question = True
    context = {'correct_answer': correct_answer, 'song': song, 'answer': answer, 'game': current_game, 'last_question': last_question}  
    return render(request, "trivia/answer.html", context)
