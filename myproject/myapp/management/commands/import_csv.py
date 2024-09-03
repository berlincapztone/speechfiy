import os
import time
import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from myapp.models import VocabularyWord22
from gtts import gTTS, gTTSError

class Command(BaseCommand):
    help = 'Import vocabulary words from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        if not os.path.exists(csv_file):
            self.stderr.write(self.style.ERROR(f"File {csv_file} does not exist."))
            return

        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                word = row['word']
                pronunciation = row['pronunciation']
                example_sentence = row['example_sentence']
                corrected_sentence = row['corrected_sentence']
                image_path = row['image']
                audio_word_path = row['audio_word']
                audio_pronunciation_path = row['audio_pronunciation']
                audio_example_path = row['audio_example']
                audio_corrected_sentence_path = row['audio_corrected_sentence']

                # Create VocabularyWord instance
                vocab_word = VocabularyWord22.objects.create(
                    word=word,
                    pronunciation=pronunciation,
                    example_sentence=example_sentence,
                    corrected_sentence=corrected_sentence,
                    image=image_path if image_path else '',
                    audio_word=audio_word_path if audio_word_path else '',
                    audio_pronunciation=audio_pronunciation_path if audio_pronunciation_path else '',
                    audio_example=audio_example_path if audio_example_path else '',
                    audio_corrected_sentence=audio_corrected_sentence_path if audio_corrected_sentence_path else '',
                )

                # Define paths for audio files
                word_audio_path = os.path.join(settings.MEDIA_ROOT, 'audio', f'{word}_word.mp3')
                pronunciation_audio_path = os.path.join(settings.MEDIA_ROOT, 'audio', f'{word}_pronunciation.mp3')
                example_audio_path = os.path.join(settings.MEDIA_ROOT, 'audio', f'{word}_example.mp3')
                corrected_sentence_audio_path = os.path.join(settings.MEDIA_ROOT, 'audio', f'{word}_corrected_sentence.mp3')

                # Fetch and save audio files with retry mechanism
                self.fetch_audio(word, 'en', word_audio_path)
                self.fetch_audio(pronunciation, 'en', pronunciation_audio_path)
                self.fetch_audio(example_sentence, 'en', example_audio_path)
                self.fetch_audio(corrected_sentence, 'en', corrected_sentence_audio_path)

                # Update the VocabularyWord instance with the audio file paths
                vocab_word.audio_word = os.path.relpath(word_audio_path, settings.MEDIA_ROOT)
                vocab_word.audio_pronunciation = os.path.relpath(pronunciation_audio_path, settings.MEDIA_ROOT)
                vocab_word.audio_example = os.path.relpath(example_audio_path, settings.MEDIA_ROOT)
                vocab_word.audio_corrected_sentence = os.path.relpath(corrected_sentence_audio_path, settings.MEDIA_ROOT)
                vocab_word.save()

    def fetch_audio(self, text, lang, audio_path):
        MAX_RETRIES = 5
        RETRY_DELAY = 5  # seconds

        if not text:
            self.stderr.write(self.style.WARNING(f"Skipping empty text for audio generation: {audio_path}"))
            return

        for attempt in range(MAX_RETRIES):
            try:
                tts = gTTS(text=text, lang=lang)
                tts.save(audio_path)
                self.stdout.write(self.style.SUCCESS(f"Successfully saved audio to {audio_path}"))
                break
            except gTTSError as e:
                self.stderr.write(self.style.ERROR(f"Attempt {attempt + 1} failed: {e}"))
                if attempt < MAX_RETRIES - 1:
                    self.stderr.write(self.style.WARNING(f"Retrying in {RETRY_DELAY} seconds..."))
                    time.sleep(RETRY_DELAY)
                else:
                    self.stderr.write(self.style.ERROR("Max retries reached. Failed to fetch audio."))
                    raise
