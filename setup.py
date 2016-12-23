import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()


setup(
    name='pharmacy-api',
    version=0.1,
    description='Pharmacy API',
    long_description=README,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pylons',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application'
    ],
    keywords='web services',
    author='Anton Barkovsky',
    author_email='anton@swarmer.me',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'cornice==2.3.0',
        'waitress==1.0.1',
    ],
    entry_points='''\
    [paste.app_factory]
    main=pharmacy_api:main
    ''',
    paster_plugins=['pyramid']
)
