Simple django project skeleton for beginners
============================================

This is a small project I give to students that want to learn Python. It's a
very fast and uncomplicated way to get started. It features a way to list
banks.

The goal of this project is to make it easy to get started and not to be
confronted with complicated installations (huge requirements).


Dependencies
------------

- sqlite3
- python/pip


Installation
-------------

On Linux:

    sudo pip install -r requirements.txt

On Windows:

    sudo pip install -r requirements.txt

You might want to use `Active Python
<http://www.activestate.com/activepython>`_ on Windows, because it comes with
pip and the whole `PATH` issues are resolved.


Usage
-----

python manage.py syncdb
python manage.py runserver
