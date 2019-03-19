from django.db import models


class RightWords(models.Model):
    word = models.CharField(max_length=128, unique=True, default='', verbose_name='Word')

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
