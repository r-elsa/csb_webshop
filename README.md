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

**1. Navigate to /csb_webshop and add dependencies**

```bash
poetry install
```


<br />

**2. Activate shell**

```bash
poetry shell
```

<br />

**3. Create superuser (admin). You can leave email field empty.**

```bash
 py manage.py createsuperuser
```
<br />

**4. Make migrations**
   
```bash
py manage.py makemigrations
```

```bash
py manage.py migrate
```


**5. Start server / run application**

```bash
poetry run python manage.py runserver  

```

<br />

## Admin credentials

superuser
super321

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

## Shell

<br />

```bash
py manage.py shell
```

```bash
from django.contrib.sessions.models import Session
s=Session.objects.get(pk='<insert key here>')
s.get_decoded()




