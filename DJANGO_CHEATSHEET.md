# 🚀 Django Cheatsheet (The Essentials)

**Use this reference to avoid pausing the video every 5 minutes.**

## 💻 Terminal Commands
*Run these in your VS Code Terminal. Ensure your virtual environment `(venv)` is active!*

### 1. Setup & Installation
| Action | Command |
| :--- | :--- |
| **Create Venv** | `python -m venv venv` |
| **Activate Venv (Win)** | `venv\Scripts\activate` |
| **Activate Venv (Mac)** | `source venv/bin/activate` |
| **Install Django** | `pip install django` |
| **Install Markdown** | `pip install markdown2` |

### 2. Project Creation
| Action | Command |
| :--- | :--- |
| **Start Project** | `django-admin startproject PROJECTNAME` |
| **Start App** | `python manage.py startapp APPNAME` |
| **Run Server** | `python manage.py runserver` |

### 3. Database Changes
*(You will need these when you modify models.py)*
| Action | Command |
| :--- | :--- |
| **Prepare Changes** | `python manage.py makemigrations` |
| **Apply Changes** | `python manage.py migrate` |

---

## 🎨 Django Template Language (DTL)
*Use this syntax inside your HTML files.*

### 1. Variables (Printing Data)
*Use double curly braces `{{ }}` to display data sent from `views.py`.*
```html
<h1>Hello, {{ name }}!</h1>

### 2. Logic (Loops & If Statements)
Use curly brace + percent `{% %}` for logic.
```
**Looping through a list:**
```html
<ul>
    {% for entry in entries %}
        <li>{{ entry }}</li>
    {% endfor %}
</ul>
```
**If/Else Conditions:**

```HTML

{% if user_is_logged_in %}
    <p>Welcome back!</p>
{% else %}
    <a href="/login">Log In</a>
{% endif %}
3. Links (The "Safe" Way)
Never hardcode URLs like /wiki/css. Use the name you gave it in urls.py.
```
```HTML

<a href="{% url 'entry' 'CSS' %}">Read about CSS</a>
4. Inheritance (DRY Principle)
In layout.html (The Parent):
```
```HTML

<html>
    <head>...</head>
    <body>
        <nav>...</nav>
        
        {% block body %}
        {% endblock %}
        
    </body>
</html>
```
**In index.html (The Child):**

```HTML

{% extends "encyclopedia/layout.html" %}

{% block body %}
    <h1>Home Page</h1>
    <p>Welcome to the Wiki!</p>
{% endblock %}
```
###🔗 The "wiring" (Connecting Files)
This is the most confusing part. Here is the flow of data.

1. `urls.py` (The Receptionist)
Decides where to send the user based on the URL.

```Python

from django.urls import path
from . import views

urlpatterns = [
    # path(url_text, function_to_run, name_reference)
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry") 
]
```
2. `views.py` (The Brain)
Processes logic and grabs data.

```Python

from django.shortcuts import render
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries() # Sending data to HTML
    })
```
###🛠️ Quick Troubleshooting
"TemplateDoesNotExist": Did you add your app to `INSTALLED_APPS` in `settings.py`?

"CSRF Verification Failed": Did you add `{% csrf_token %}` inside your `<form>`?

Changes not showing?: Save your file! (`Ctrl+S` / `Cmd+S`). The server usually auto-reloads, but only if you save.
