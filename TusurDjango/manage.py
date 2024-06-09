#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

This script allows you to run various administrative tasks provided by Django.
For more information, visit: https://docs.djangoproject.com/en/4.1/ref/django-admin/
"""

import os
import sys


def main():
    """Run administrative tasks."""
    # Устанавливаем конфигурационный модуль Django по умолчанию
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_primer.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # В случае ошибки при импорте Django выводим соответствующее сообщение
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Запускаем утилиту командной строки Django с переданными аргументами
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
