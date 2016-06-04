from django.conf.urls import include, url
from trivia import views

urlpatterns = [
    url(r'^$', views.create_game, name='create_game'),
    url(r'question/', views.question_view, name='question'),
    url(r'(?P<song_id>[0-9]+)/(?P<answer>[0-9]+)$/', views.question_answer, name='question_answer')
]