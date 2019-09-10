# Contact Book

CRUD API for contact book
Postman link : [https://www.getpostman.com/collections/43b4db810ebf145f1e00]
# Pre requisite
1. Install Python 2.7
2. Install virtualenv

# Project Setup

1. Create and activate your virtual env.
```
$ virtualenv venv
$ source env/bin/activate
```

2. Install requirements.txt
```
$ python install -r requirements.txt
```

3. Create database "contact_book"

```
$ mysql -u root -p
$ mysql> create database contact_book
```

4. export DATABASE variables
```
$ export DB_NAME=contact_book
$ export DB_USER=root
$ export DB_PASSWORD=test@123
```

4. Run the integration tests by:
```
$ export ENVIRONMENT=development;export DJANGO_SETTINGS_MODULE=application.src.db.settings.development; export PYTHONPATH=$PWD
$ python application/src/db/manage.py test
```
5. Run the Django migrations:
```
$ export ENVIRONMENT=development;export DJANGO_SETTINGS_MODULE=application.src.db.settings.development; export PYTHONPATH=$PWD
$ python application/src/db/manage.py migrate
```

5. Run application by:
```
$ export ENVIRONMENT=development;export DJANGO_SETTINGS_MODULE=application.src.db.settings.development; export PYTHONPATH=$PWD
$ python application/src/launcher.py
```
