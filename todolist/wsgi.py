"""
WSGI config for todolist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import dotenv
from pathlib import Path
from django.core.wsgi import get_wsgi_application

BASEDIR = Path(__file__).resolve().parent.parent
ENV_FILE_PATH = BASEDIR / '.env'

dotenv.read_dotenv(str(ENV_FILE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todolist.settings')

application = get_wsgi_application()
