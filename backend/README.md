# Backend

## Dev Environment Instructions:

### Install python

Use `Python 3.11` It is best to create a new virtual environment. You can use venv, conda, or any other python virtual environment tool.

### Install depedencies:

```
pip install -r requirements.txt
```

### Setup Database:

```
python manage.py migrate
```

### Optional: load starting models

```
python manage.py loaddata startermodels.json
```

### Run Server

```
python manage.py runserver
```

The server defaults to `http://localhost:8000/`. API calls be sent to: `http://localhost:8000/API/`

### Run tests

```
python manage.py test
```

## Production Environment Instructions

### Install Python

Also use `Python 3.11`

### Install Depedencies:

```
pip install -r requirements.txt
```

### Setup Database:

```
python manage.py migrate
```

### Optional: load starting models

```
python manage.py loaddata startermodels.json
```

### Collect static files:

```
python manage.py collectstatic && gunicorn marketingbot.wsgi
```

## Helpful Tips:

Create yourself as a super-user by:

```
python manage.py createsuperuser
```

Then you have access to: `http://localhost:8000/admin`, or if you do this on prod then prod. Here you can change any models.
