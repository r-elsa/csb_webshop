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

**4. Create admin user. IMPORTANT!**

```bash
 py manage.py createsuperuser
```
<br />



**5. Start server / run application**

```bash
poetry run python manage.py runserver  

```
<br />

**5. What to do next?**

- Click on **Admin** or navigate to /admin.
- Create a few categories of products (e.g. **laptops** and **headphones**)
- Create a few products to each categories (e.g. **Laptops**: Mac Book, ThinkPad, Asus. **Headphones**: AirPods, Beats Studio Pro). Fill in all necessary fields.
- Navigate back to *http://127.0.0.1:8000/*
- Explore the webshop: Filter products by category, search for product by product title, view product and add a selected amount to your shopping basket. View basket by clicking on the basket. Go to admin and add a few more categories and/or products. Try inserting a script to Product search -field or make a GET -requst to *http://127.0.0.1:8000/basket/add* from postman...
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




