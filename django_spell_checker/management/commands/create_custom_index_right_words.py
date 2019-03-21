__author__ = 'sb'
"""
Because not all database can create custom indexes - emulate it =)
"""
from django.core.management.base import BaseCommand
from django_spell_checker.models import RightWords
from django.db.models import Q
class Command(BaseCommand):
    help = 'delete ALL right words'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start'))
        for word in RightWords.objects.filter(Q(first_letter='') or Q(length=0)):
            word.first_letter=word.word[0]
            word.length=len(word.word)
            word.save()
        self.stdout.write(self.style.SUCCESS('End'))