#!/usr/bin/env python

from distutils.core import setup


setup(name='python-c-cex',
      version='0.1.1',
      packages=['ccex'],
      modules=['ccex'],
      description='Python bindings for C-CEX API.',
      author='Ben Stadium',
      author_email='mp3it.eu@gmail.com',
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: MIT License',
          'Development Status :: 3 - Alpha',
          'Topic :: Office/Business :: Financial',
      ])
