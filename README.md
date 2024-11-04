# Webshop -application with vulnerabilities

A webshop -website developed using Python & Django. The application has 5 vulnerabilities out of the [Owasp top 10](https://owasp.org/Top10/) from 2021. The application is developed for the course [Cyber Security Base](https://cybersecuritybase.mooc.fi/module-3.1).

Note! The project is on branch *master*

<br />

## Vulnerabilities in Product Features

### FLAW 1: Broken Access Control
**Feature:** Admin board  
**OWASP Category:** A01: Broken Access Control  



### FLAW 2: SQL Injection
**Feature:** Product search  
**OWASP Category:** A03: Injection  



### FLAW 3: Cross-Site Request Forgery (CSRF)
**Feature:** Create superuser  
**OWASP Category:** A08: Software and Data Integrity Failures  



### FLAW 4: Sensitive Data Exposure
**Feature:** Shopping basket  
**OWASP Category:** A02: Cryptographic Failures  



### FLAW 5: Insecure Direct Object References (IDOR)
**Feature:** Shopping basket  
**OWASP Category:** A04: Insecure Design  



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

**3. Make migrations. IMPORTANT!**
   
```bash
py manage.py makemigrations
```

```bash
py manage.py migrate
```

**4. Create superuser (admin).**

```bash
 py manage.py createsuperuser
```
<br />



**5. Start server / run application**

```bash
poetry run python manage.py runserver  

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




