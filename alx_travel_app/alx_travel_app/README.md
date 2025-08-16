# Django Project Core

This directory contains the core configuration and setup files for the Django project.

## 📁 Structure

<project_name>/
├── init.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py

yaml
Copy
Edit

## 📄 File Descriptions

### `__init__.py`
Marks this directory as a Python package. Required for importing modules properly.

### `settings.py`
Contains all the configuration settings for your Django project.  
Includes database setup, installed apps, middleware, templates, time zone, static files, etc. Note that the database has been configured to use MySQL instead of the default SQLite3. Apps such as the listings app, and django restframework are registered in the installed apps section

> To customize project behavior, this is the main file to modify.

### `urls.py`
Controls the URL routing for the entire project.  
It maps URL paths to views either directly or by including app-specific `urls.py`.

### `wsgi.py`
Entry-point for WSGI-compatible web servers (e.g., Gunicorn, uWSGI) to serve your Django app.

Used when deploying to production environments.

### `asgi.py`
Entry-point for ASGI-compatible servers (e.g., Daphne, Uvicorn), enabling support for async features like WebSockets.

Used in modern Django deployments needing async capabilities.

---

## ⚙️ Typical Usage

When running common commands like:

```bash
python manage.py runserver
python manage.py migrate
python manage.py shell
