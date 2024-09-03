import os
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from gtts import gTTS
from django.http import HttpResponse




from .models import SightWord1

import logging
logger = logging.getLogger(__name__)



def generate_sight_words_level_2(request):
    sight_words = [
        "about", "again", "always", "around", "because", "been", "before", "best", "both",
        "buy", "call", "cold", "does", "don't", "fast", "first", "five", "found", "gave",
        "goes", "green", "its", "made", "many", "off", "or", "pull", "read", "right",
        "sing", "sit", "sleep", "tell", "their", "these", "those", "upon", "us", "use",
        "very", "wash", "which", "why", "wish", "work", "would", "write", "your"
    ]
    audio_directory = os.path.join(settings.MEDIA_ROOT, 'sight_word_audios_level_2')
    os.makedirs(audio_directory, exist_ok=True)

    def text_to_speech(text, filename):
        tts = gTTS(text=text, lang='en')
        tts.save(filename)

    for word in sight_words:
        file_path = os.path.join(audio_directory, f"{word}.mp3")
        text_to_speech(word, file_path)
        sight_word_obj, created = SightWord1.objects.get_or_create(word=word)
        sight_word_obj.audio_file.name = f'sight_word_audios_level_2/{word}.mp3'
        sight_word_obj.save()

    return redirect('list_sight_words_level_2')


def list_sight_words_level_2(request):
    sight_words = SightWord1.objects.all()
    return render(request, 'sight_words/list_level_2.html', {'sight_words': sight_words})

from myapp.models import SightWord1



def home(request):
    return render(request, 'front.html')

def important_view(request):
    return render(request, 'important.html')

def historical_view(request):
    return render(request, 'histroical.html') 

def key_research_view(request):
    return render(request, 'key research.html')

def impact_view(request):
    return render(request, 'impact.html')

def phonemic_awareness_view(request):
    return render(request, 'phonemic awareness.html')  

def reading_view(request):
    return render(request, 'reading.html')

def login_view(request):
    return render(request, 'login.html')

def volcubary_view(request):
    return render(request, 'volcubary.html' )
 
def sign_view(request):
    return render(request, 'sign.html')

def writing_view(request):
    return render(request, 'writing.html' )

def writting1_view(request):
    return render(request, 'writting1.html' )

def two_view(request):
    return render(request, 'two.html' )

def three_view(request):
    return render(request, 'three.html' )


from .models import VocabularyWord


def vocabulary_list(request):
    words = VocabularyWord.objects.all()
    return render(request, 'myapp/vocabulary_list.html', {'words': words})

from .models import AnimalWords

def animal_list (request):
    words = AnimalWords.objects.all()
    return render(request, 'myapp/animal.html', {'words': words})

from .models import Foodswords

def foods_list (request):
    words = Foodswords.objects.all()
    return render(request, 'myapp/food.html', {'words': words})

from .models import schoolwords

def school_list (request):
    words = schoolwords.objects.all()
    return render(request, 'myapp/school.html', {'words': words})

from django.shortcuts import render
from .models import VocabularyWord22

def vocabulary_list_view(request):
    vocabulary_words = VocabularyWord22.objects.all()
    return render(request, 'vocabulary_list.html', {'vocabulary_words': vocabulary_words})


