from distutils.core import setup
import setuptools
import setuptools.command.test

setuptools.setup(
    name='django_spell_checker',
    version='1.0',
    url='https://github.com/saintbyte/django-spell-checker',
    license='BSD',
    author='sb',
    author_email='admin@ural.im',
    description='',
    install_requires=[
        'Django>=2.0',
    ],
    packages=setuptools.find_packages(exclude=['ez_setup', 't', 't.*']),
    zip_safe=False,
    python_requires=">=3.5",
)
