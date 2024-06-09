"""
ASGI конфигурация для проекта django_primer.

Этот файл предоставляет ASGI-приложение, которое доступно как переменная уровня модуля с именем ``application``.

Дополнительную информацию можно найти по ссылке:
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Задаем конфигурационный модуль по умолчанию для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{os.path.basename(os.getcwd())}.settings')

# Получаем ASGI-приложение для проекта
application = get_asgi_application()