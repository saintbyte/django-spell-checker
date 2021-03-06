__author__ = 'sb'
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='django_spell_checker_index_view'),
    path('spell/', views.spell_view, name='django_spell_checker_spel_view'),
    path('spell.json', views.spell_view_json, name='django_spell_checker_spel_view_json'),
]