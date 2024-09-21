# Webshop -application with vulnerabilities


A webshop -website developed using Python & Django. The application has 5 vulnerabilities out of [Owasp top 10](https://owasp.org/Top10/). Using list from 2021. The application is developed for course [Cyber Security Base](https://cybersecuritybase.mooc.fi/module-3.1).

Note! The project is on branch *master*

<br />

## Product features and respective vulnerabilities

- registration & login
- shopping cart session
- product search - form submission without CSRF




## Installation, compilation and excecution
<br />

1. Navigate to /csb_webshop and add dependencies

```bash
poetry install
```


<br />

2. Activate shell

```bash
poetry shell
```

<br />

3. Start server / run application

```bash
poetry run python csb/manage.py runserver  

```

<br />

## Admin credentials

<br />

1. Username

```bash
csb_user
```
2. Password
```bash
csb2024
```

<br />

## Superuser credentials

<br />

1. Username

```bash
admin_csb
```
2. Password
```bash
admin321
```

## Database migrations

<br />


```bash
py manage.py makemigrations
```

```bash
py manage.py migrate
```


## Shell

<br />

```bash
py manage.py shell
```

```bash
from django.contrib.sessions.models import Session
s=Session.objects.get(pk='<insert key here>')
s.get_decoded()




