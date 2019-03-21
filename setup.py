from distutils.core import setup

setup(
    name='django_spell_checker',
    version='1',
    url='https://github.com/saintbyte/django-spell-checker',
    license='BSD',
    author='sb',
    author_email='admin@ural.im',
    description='',
    install_requires=[
        'Django>=2.0',
        'json',
    ],
    python_requires=">=3.5",
)
