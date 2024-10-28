# admin.py
from django.contrib import admin
from .models import Phoneme, Word, SightWord, SightWord1, SightWord2

admin.site.register(Phoneme)
admin.site.register(Word)
admin.site.register(SightWord)
admin.site.register(SightWord1)
admin.site.register(SightWord2)
from django.contrib import admin
from .models import SightWord4

admin.site.register(SightWord4)
from django.contrib import admin

from django.contrib import admin
from .models import VocabularyWord, AnimalWords,Foodswords,schoolwords

admin.site.register(VocabularyWord)

admin.site.register(AnimalWords)

admin.site.register(Foodswords)
admin.site.register(schoolwords)


from django.contrib import admin
from .models import VocabularyWord22

admin.site.register(VocabularyWord22)



from django.contrib import admin
from .models import PhoneticSymbol

admin.site.register(PhoneticSymbol)



from django.contrib import admin
from .models import PhoneticRepresentation

admin.site.register(PhoneticRepresentation)



# myapp/admin.py

from django.contrib import admin
from .models import SpeechSound

class SpeechSoundAdmin(admin.ModelAdmin):
    list_display = ('phoneme', 'word')
    search_fields = ('phoneme', 'word')

admin.site.register(SpeechSound, SpeechSoundAdmin)
