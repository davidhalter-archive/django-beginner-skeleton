Simple Django project skeleton for beginners
============================================

This is a small project I give to students that want to learn Python. It's a
very fast and uncomplicated way to get started. It features a way to list
banks.

The goal of this project is to make it easy to get started and not to be
confronted with complicated installations (huge requirements).

This project should also be working on Windows as well as both Python
2.7 and Python >=3.2.

The only Django dependency is `django frontend skeleton
<https://github.com/jonfaustman/django-frontend-skeleton>`_, to make the
bootstrap stuff easy.

Obviously the forms can and should be done differently, check `crispy forms
<https://github.com/maraujop/django-crispy-forms>`_ for that. I removed that
intentionally, since I find it important for beginners to see how forms in
Django work.


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
