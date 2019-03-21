from django.shortcuts import render
from .models import RightWords
from .spell import Spell
from django.http import JsonResponse, HttpResponse
from django.utils.safestring import mark_safe
from .utils import copyFormat
import json
def right_words_count():
    return RightWords.objects.all().count()


def index_view(request):
    ctx = {}
    ctx['right_words_count'] = right_words_count()
    return render(request, "django_spell_checker/index.html", ctx)

def generate_select(word,result):
    s = '<select>'
    s = s + '<option selected="selected" style="color:red">'+word+'</option>'
    for w in result[word.lower()]['correction_variants']:
        s = s + '<option>'+copyFormat(word, w[0])+'('+str(w[1])+')</option>'
    s = s + '</select>'
    return s

def spell_view(request):
    ctx = {}
    text = request.POST.get('text', '')
    sp = Spell(text)
    sp.set_dictionary(RightWords)
    result = sp.spell()
    wrong_words = list( result.keys())
    wrong_words.sort()
    ctx['error_words_count'] = len(result.keys())
    ctx['text'] = ''
    word = ''
    new_text = ''
    for char in text:
        if (char in sp.word_split_char_arr):
            if word != '':
                if sp._normalize_word(word) in result.keys():
                    new_text = new_text + generate_select(word,result)+char
                else:
                    new_text = new_text + word+char
                word = ""
                continue
            new_text = new_text + char
            continue
        word= word + char
    ctx['text'] = mark_safe(new_text)
    ctx['wrong_words'] = wrong_words
    ctx['json_text'] = json.dumps(result)
    return render(request, "django_spell_checker/spell.html", ctx)


def spell_view_json(request):
    sp = Spell(request.POST.get('text', ''))
    sp.set_dictionary(RightWords)
    result = sp.spell()
    return JsonResponse(result)
