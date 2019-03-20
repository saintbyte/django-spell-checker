from django.shortcuts import render
from .models import RightWords
from .utils import Spell
from django.http import JsonResponse,HttpResponse
def right_words_count():
    return RightWords.objects.all().count()


def index_view(request):
    ctx = {}
    ctx['right_words_count'] = right_words_count()
    return render(request, "django_spell_checker/index.html", ctx)

def spell_view(request):
    sp = Spell(request.POST.get('text',''))
    sp.set_dictionary(RightWords)
    result = sp.spell()
    return JsonResponse(result)
