"""
Django settings for django_primer project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
import environ

# Определение корневой директории проекта и папки приложения
APP_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(APP_DIR)

# Инициализация пакета environ для работы с переменными окружения и .env файлами
env = environ.Env()

# Путь к .env файлу
env_file = os.path.join(BASE_DIR, '.env')

# Чтение настроек из .env файла
environ.Env.read_env(env_file)

# Установка настроек по умолчанию, если они не определены в .env файле
DEBUG = env.bool('DEBUG', default=True)
SECRET_KEY = env.str('SECRET_KEY', default='django-insecure-la*+ov2%-8892pgc-7j4j@q8cialaztat%-jom7(4qimfgxr8$')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

# ...

# Настройки базы данных
db_config = env.db('DATABASE_URL')
DATABASES = {
    'default': db_config
}

# ...

# Настройки логирования
LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db': {
            'level': 'INFO'
        },
    },
}
