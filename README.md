#Django Spell Checker

###Зависимости
Зависимости: python 3, django > 2, json 

###Установка к Django
1. Получаем копию
pip install git+https://github.com/saintbyte/django-spell-checker
или 
git clone https://github.com/saintbyte/django-spell-checker

2. Настраиваем Django
Добавляем в INSTALLED_APPS ( в settings.py ) 'django_spell_checker' 

3. Добавляем в urls.py роут 
path('django_spell_checker/', include('django_spell_checker.urls')),
не забывая при это from django.urls import  include

4. Накатываем миграции ./manage.py migrations

5. Качаем словарь:  "Краткий вариант без ударений (562 Кб)" со страницы http://www.speakrus.ru/dict/  

6. Загружаем словарь в базу командой: ./manage.py import_right_words --file=lop2v2.txt --encoding=windows-1251
( Это надолго ) 

7. Делаем ./manage.py runserver и заходим http://127.0.0.1:8000/django_spell_checker/


###Установка standalone
 
Можно попробывать from django_spell_checker import Spell
