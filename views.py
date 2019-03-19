from django.shortcuts import render
from .models import RightWords
from .utils import Spell

def right_words_count():
    return RightWords.objects.all().count()


def index_view(request):
    ctx = {}
    ctx['right_words_count'] = right_words_count()
    if request.POST:
        sp = Spell(request.POST.get('spellit',''))
        sp.set_dictionary(RightWords)
        sp.spell()
    return render(request, "django_spell_checker/index.html", ctx)
