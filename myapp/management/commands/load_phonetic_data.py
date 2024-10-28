from phonemizer.separator import Separator
from phonemizer import phonemize
import csv
import os
import requests
from django.core.management.base import BaseCommand
from myapp.models import SpeechSound
from django.conf import settings
import pyttsx3
import nltk

# Ensure NLTK resources are downloaded
nltk.download('cmudict')
from nltk.corpus import cmudict

class Command(BaseCommand):
    help = 'Load phonetic data from a CSV file and generate audio files for phonemes and words'

    def handle(self, *args, **kwargs):
        # Path to the CSV file containing phonetic symbols and words
        csv_file_path = os.path.join(settings.BASE_DIR, 'myapp', 'data', 'phonetic_symbols.csv')
        
        # Load phonetic data from the CSV file
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Create or update SpeechSound object
                speech_sound, created = SpeechSound.objects.update_or_create(
                    phoneme=row['phoneme'],
                    defaults={'word': row['word']},
                )
                # Generate audio files for phonemes and words
                self.generate_audio(speech_sound)

        self.stdout.write(self.style.SUCCESS('Successfully loaded phonetic data and generated audio'))

    def generate_audio(self, speech_sound):
        sounds_dir = os.path.join(settings.MEDIA_ROOT, 'phonemes/sounds')
        os.makedirs(sounds_dir, exist_ok=True)
        
        # Generate and save audio for phoneme
        phoneme_pronunciation = self.get_pronunciation(speech_sound.phoneme)
        speech_sound.sound_phoneme = self.create_audio_file(phoneme_pronunciation, sounds_dir, 'phoneme', is_phoneme=True)
        
        # Generate and save audio for word
        word_pronunciation = speech_sound.word
        speech_sound.sound_word = self.create_audio_file(word_pronunciation, sounds_dir, 'word')
        
        # Save the updated SpeechSound object with audio file paths
        speech_sound.save()

    def get_pronunciation(self, phoneme):
        """Get the desired pronunciation for the phoneme."""
        # Define a mapping of phonemes to their pronunciations
        phoneme_map = {
            '/k/': 'kat',
            '/b/': 'beg',
            '/d/': 'doe',
            '/f/': 'fall',
            '/g/': 'goal',
            '/h/': 'has',
            '/j/': 'job',
            '/l/': 'lip',
            '/m/': 'map',
            '/n/': 'net',
            '/p/': 'pin',
            '/r/': 'run',
            '/s/': 'sat',
            '/t/': 'toe',
            '/v/': 'vin',
            '/w/': 'wait',
            '/y/': 'yam',
            '/z/': 'zip'
        }
        return phoneme_map.get(phoneme, phoneme.strip('/'))  # Return the mapped value or the phoneme itself if not found.

    def create_audio_file(self, text, sounds_dir, audio_type, is_phoneme=False):
        # Initialize pyttsx3 for generating audio files
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Regular speed for pronunciation
        engine.setProperty('volume', 1)
        
        # Sanitize text for filename
        filename = f"{text.strip()}.mp3".replace('/', '_').replace(' ', '_')
        file_path = os.path.join(sounds_dir, filename)
        
        try:
            # Use pyttsx3 to generate audio file
            engine.save_to_file(text, file_path)
            engine.runAndWait()
            # Log the saved file path
            self.stdout.write(self.style.SUCCESS(f'Saved {audio_type} audio to: {file_path}'))
            return f'phonemes/sounds/{filename}'
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error generating {audio_type} audio for "{text}": {e}'))
            return None


