from django.db import models


class RightWords(models.Model):
    word = models.CharField(max_length=128, unique=True, default='', verbose_name='Word')
    first_letter = models.CharField(max_length=1, default='', verbose_name='First letter',
                                    help_text='its for custom index', db_index=True, blank=True)
    length = models.IntegerField(default=0, verbose_name='First letter', blank=True,
                                    help_text='its for custom index', db_index=True)
    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Right words'


class WrongWords(models.Model):
    word = models.CharField(max_length=128, unique=True, default='', verbose_name='Word')

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Wrong words'
