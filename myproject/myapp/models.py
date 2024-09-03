# models.py
from django.db import models

class Phoneme(models.Model):
    name = models.CharField(max_length=2)
    audio_file = models.FileField(upload_to='phoneme_audios')

    def __str__(self):
        return self.name

class Word(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word

class SightWord(models.Model):
    word = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='sight_word_audios')

    def __str__(self):
        return self.word

class SightWord1(models.Model):
    word = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='sight_word_audios_level_2')

    def __str__(self):
        return self.word

class SightWord2(models.Model):
    word = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='sight_word_audios_level_3')

    def __str__(self):
        return self.word
from django.db import models

class SightWord4(models.Model):
    word = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='sight_word_audios_level_4')

    def __str__(self):
        return self.word


from django.db import models
from gtts import gTTS
import os
from django.conf import settings

class VocabularyWord(models.Model):
    word = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=100)
    example_sentence = models.TextField()
    image = models.ImageField(upload_to='images/')
    audio_word = models.FileField(upload_to='audio/words/', blank=True)
    audio_pronunciation = models.FileField(upload_to='audio/pronunciation/', blank=True)
    audio_example = models.FileField(upload_to='audio/example/', blank=True)

    def save(self, *args, **kwargs):
        
        word_audio_dir = os.path.join(settings.MEDIA_ROOT, 'audio/words')
        pronunciation_audio_dir = os.path.join(settings.MEDIA_ROOT, 'audio/pronunciation')
        example_audio_dir = os.path.join(settings.MEDIA_ROOT, 'audio/example')
        
        os.makedirs(word_audio_dir, exist_ok=True)
        os.makedirs(pronunciation_audio_dir, exist_ok=True)
        os.makedirs(example_audio_dir, exist_ok=True)

        
        tts_word = gTTS(text=self.word, lang='en')
        audio_word_path = os.path.join(word_audio_dir, f'{self.word}.mp3')
        tts_word.save(audio_word_path)
        self.audio_word.name = f'audio/words/{self.word}.mp3'

        
        tts_pronunciation = gTTS(text=self.pronunciation, lang='en')
        audio_pronunciation_path = os.path.join(pronunciation_audio_dir, f'{self.word}_pronunciation.mp3')
        tts_pronunciation.save(audio_pronunciation_path)
        self.audio_pronunciation.name = f'audio/pronunciation/{self.word}_pronunciation.mp3'

        
        tts_example = gTTS(text=self.example_sentence, lang='en')
        audio_example_path = os.path.join(example_audio_dir, f'{self.word}_example.mp3')
        tts_example.save(audio_example_path)
        self.audio_example.name = f'audio/example/{self.word}_example.mp3'

        super().save(*args, **kwargs)

from django.db import models
from gtts import gTTS
import os
from django.conf import settings

class AnimalWords(models.Model):
    
    word = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=100)
    example_sentence = models.TextField()
    image = models.ImageField(upload_to='images/')
    audio_word = models.FileField(upload_to='audio/words/', blank=True)
    audio_pronunciation = models.FileField(upload_to='audio/pronunciation/', blank=True)
    audio_example = models.FileField(upload_to='audio/example/', blank=True)

    def save(self, *args, **kwargs):
    
        word_audio_dir = os.path.join(settings.MEDIA_ROOT, 'audio/words')
        pronunciation_audio_dir = os.path.join(settings.MEDIA_ROOT, 'audio/pronunciation')
        example_audio_dir = os.path.join(settings.MEDIA_ROOT, 'audio/example')
        
        os.makedirs(word_audio_dir, exist_ok=True)
        os.makedirs(pronunciation_audio_dir, exist_ok=True)
        os.makedirs(example_audio_dir, exist_ok=True)

        
        tts_word = gTTS(text=self.word, lang='en')
        audio_word_path = os.path.join(word_audio_dir, f'{self.word}.mp3')
        tts_word.save(audio_word_path)
        self.audio_word.name = f'audio/words/{self.word}.mp3'

        
        tts_pronunciation = gTTS(text=self.pronunciation, lang='en')
        audio_pronunciation_path = os.path.join(pronunciation_audio_dir, f'{self.word}_pronunciation.mp3')
        tts_pronunciation.save(audio_pronunciation_path)
        self.audio_pronunciation.name = f'audio/pronunciation/{self.word}_pronunciation.mp3'

        
        tts_example = gTTS(text=self.example_sentence, lang='en')
        audio_example_path = os.path.join(example_audio_dir, f'{self.word}_example.mp3')
        tts_example.save(audio_example_path)
        self.audio_example.name = f'audio/example/{self.word}_example.mp3'

        super().save(*args, **kwargs)

import os
import requests
from django.db import models
from django.conf import settings
from gtts import gTTS

class Foodswords(models.Model):
    word = models.CharField(max_length=100)
    corrected_word = models.CharField(max_length=100, blank=True)
    pronunciation = models.CharField(max_length=100, blank=True)
    example_sentence = models.TextField()
    corrected_sentence = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    audio_word = models.FileField(upload_to='audio/words/', blank=True)
    audio_pronunciation = models.FileField(upload_to='audio/pronunciation/', blank=True)
    audio_example = models.FileField(upload_to='audio/example/', blank=True)
    corrected_paragraph = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.ensure_media_directories_exist()
        self.generate_audio_files()
        self.correct_text_fields()

        super().save(*args, **kwargs)

    def ensure_media_directories_exist(self):
        for dir_path in [
            os.path.join(settings.MEDIA_ROOT, 'audio/words'),
            os.path.join(settings.MEDIA_ROOT, 'audio/pronunciation'),
            os.path.join(settings.MEDIA_ROOT, 'audio/example'),
        ]:
            os.makedirs(dir_path, exist_ok=True)

    def generate_audio_files(self):
        self.generate_audio(self.word, 'word', self.audio_word)
        self.generate_audio(self.example_sentence, 'example', self.audio_example)
        if not self.pronunciation:
            self.generate_pronunciation()

    def generate_audio(self, text, prefix, audio_field):
        if text and audio_field:
            try:
                tts = gTTS(text=text, lang='en')
                audio_path = os.path.join(settings.MEDIA_ROOT, f'audio/{prefix}s', f'{self.word}_{prefix}.mp3')
                tts.save(audio_path)
                setattr(self, audio_field.name, f'audio/{prefix}s/{self.word}_{prefix}.mp3')
            except Exception as e:
                print(f"Error generating {prefix} audio: {e}")

    def generate_pronunciation(self):
        try:
            tts = gTTS(text=self.word, lang='en')
            audio_pronunciation_path = os.path.join(settings.MEDIA_ROOT, 'audio/pronunciation', f'{self.word}_pronunciation.mp3')
            tts.save(audio_pronunciation_path)
            self.audio_pronunciation.name = f'audio/pronunciation/{self.word}_pronunciation.mp3'
            self.pronunciation = ''  # Set the pronunciation field if you want to store it
        except Exception as e:
            print(f"Error generating pronunciation audio: {e}")

    def correct_text_fields(self):
        self.corrected_word = self.correct_text(self.word)
        self.corrected_sentence = self.correct_text(self.example_sentence)
        self.corrected_paragraph = self.correct_text(f'{self.word} {self.example_sentence}')

    def correct_text(self, text):
        try:
            response = requests.post('https://api.languagetool.org/v2/check', data={'text': text, 'language': 'en'})
            matches = response.json().get('matches', [])
            corrected_text = list(text)
            for match in sorted(matches, key=lambda x: x['offset'], reverse=True):
                offset = match['offset']
                length = match['length']
                replacement = match['replacements'][0]['value']
                corrected_text[offset:offset + length] = list(replacement)
            return ''.join(corrected_text)
        except Exception as e:
            print(f"Error correcting text: {e}")
            return text

    def __str__(self):
        return self.word



from django.db import models
from gtts import gTTS
import os
from django.conf import settings

class schoolwords(models.Model):
    word = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=100)
    example_sentence = models.TextField()
    image = models.ImageField(upload_to='images/')
    audio_word = models.FileField(upload_to='audio/words/', blank=True)
    audio_pronunciation = models.FileField(upload_to='audio/pronunciation/', blank=True)
    audio_example = models.FileField(upload_to='audio/example/', blank=True)

    def save(self, *args, **kwargs):
        # Ensure audio directories exist
        word_audio_dir = os.path.join(settings.MEDIA_ROOT, 'audio/words')
        pronunciation_audio_dir = os.path.join(settings.MEDIA_ROOT, 'audio/pronunciation')
        example_audio_dir = os.path.join(settings.MEDIA_ROOT, 'audio/example')
        
        os.makedirs(word_audio_dir, exist_ok=True)
        os.makedirs(pronunciation_audio_dir, exist_ok=True)
        os.makedirs(example_audio_dir, exist_ok=True)

        # Generate audio using gTTS for word
        tts_word = gTTS(text=self.word, lang='en')
        audio_word_path = os.path.join(word_audio_dir, f'{self.word}.mp3')
        tts_word.save(audio_word_path)
        self.audio_word.name = f'audio/words/{self.word}.mp3'

        # Generate audio using gTTS for pronunciation
        tts_pronunciation = gTTS(text=self.pronunciation, lang='en')
        audio_pronunciation_path = os.path.join(pronunciation_audio_dir, f'{self.word}_pronunciation.mp3')
        tts_pronunciation.save(audio_pronunciation_path)
        self.audio_pronunciation.name = f'audio/pronunciation/{self.word}_pronunciation.mp3'

        # Generate audio using gTTS for example sentence
        tts_example = gTTS(text=self.example_sentence, lang='en')
        audio_example_path = os.path.join(example_audio_dir, f'{self.word}_example.mp3')
        tts_example.save(audio_example_path)
        self.audio_example.name = f'audio/example/{self.word}_example.mp3'

        super().save(*args, **kwargs)




# myproject/myapp/models.py

from django.db import models

class VocabularyWord22(models.Model):
    word = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=100, blank=True)
    example_sentence = models.TextField(blank=True)
    corrected_sentence = models.TextField(blank=True)
    image = models.ImageField(upload_to='vocab_images/', blank=True)
    audio_word = models.FileField(upload_to='vocab_audio/', blank=True)
    audio_pronunciation = models.FileField(upload_to='vocab_audio/', blank=True)
    audio_example = models.FileField(upload_to='vocab_audio/', blank=True)
    audio_corrected_sentence = models.FileField(upload_to='vocab_audio/', blank=True)

    def __str__(self):
        return self.word
