__author__ = 'sb'
from django.core.management.base import BaseCommand
from django_spell_checker.models import RightWords
from django.core.management import call_command
from django.conf import settings
import sys

class Command(BaseCommand):
    help = 'import right words'

    def add_arguments(self, parser):
        parser.add_argument('--file', nargs='+', help="File for parse")
        parser.add_argument('--encoding', nargs='+', help="File for parse", default='utf-8') #windows-1251

    def normalize_word(self, word):
        #TODO: more normalize word =)
        return word.strip().lower()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start'))
        fh = open(options['file'][0], 'r', encoding=options['encoding'][0])
        for line in fh:
            word = self.normalize_word(line)
            if settings.DEBUG:
                self.stdout.write(word)
            try:
                RightWords(word=word).save()
            except:
                 if settings.DEBUG:
                     (e,v, tb ) = sys.exc_info()
                     self.stdout.write('Exception:')
                     self.stdout.write(str(e))
                     self.stdout.write(str(v))
        fh.close()
        self.stdout.write(self.style.SUCCESS('create_custom_index_right_words'))
        call_command('create_custom_index_right_words')
        self.stdout.write(self.style.SUCCESS('End'))