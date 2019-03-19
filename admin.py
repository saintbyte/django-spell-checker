from django.contrib import admin
from .models import RightWords, WrongWords


class RightWordsAdmin(admin.ModelAdmin):
    pass


admin.site.register(RightWords, RightWordsAdmin)


class WrongWordsAdmin(admin.ModelAdmin):
    pass


admin.site.register(WrongWords, WrongWordsAdmin)
