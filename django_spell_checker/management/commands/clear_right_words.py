__author__ = 'sb'
from django.core.management.base import BaseCommand
from django_spell_checker.models import RightWords

class Command(BaseCommand):
    help = 'delete ALL right words'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start'))
        RightWords.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('End'))