# myapp/urls.py

from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import vocabulary_list
from .views import animal_list
from.views import foods_list
from.views import school_list
from .views import vocabulary_list_view

urlpatterns = [
    path('', views.home, name='home'),
    path('sightwords/generate/', views.generate_sight_words_level_2, name='generate_sight_words_level_2'),
    path('sightwords/', views.list_sight_words_level_2, name='list_sight_words_level_2'),
    path('important/', views.important_view, name='important'),
    path('histroical/', views.historical_view, name='histroical'),  # Corrected 'histroical' to 'historical'
    path('key-research/', views.key_research_view, name='key_research'),
    path('impact/', views.impact_view, name='impact'),
    path('phonemic-awareness/', views.phonemic_awareness_view, name='phonemic_awareness'),  # Corrected 'phonemic awareness' to 'phonemic-awareness'
    path('reading/', views.reading_view, name='reading'),
    path('login/', views.login_view, name='login'),
    path('sign/', views.sign_view, name='sign'),
    path('write/', views.writing_view, name='writing'),
    path('one/', views.writting1_view, name='writting'),
    path('two/', views.two_view, name='two'),
    path('three/', views.three_view, name='three'),
    path('volcubary/', views.volcubary_view, name='volcubary'),
    path('volc5/', vocabulary_list, name='vocabulary_list1'),
    path('animal/', animal_list, name='volc6'),
    path('foods/', foods_list, name='volc7'),
    path('school/', school_list, name='joe'),
    path('vocabulary/', vocabulary_list_view, name='vocabulary_list'),
]
