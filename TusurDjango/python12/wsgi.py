"""
WSGI config for django_primer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Задаем конфигурационный модуль по умолчанию для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{os.path.basename(os.getcwd())}.settings')

# Получаем WSGI-приложение для проекта
application = get_wsgi_application()
