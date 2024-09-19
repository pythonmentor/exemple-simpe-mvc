import os

import django

# Définir la variable d'environnement pour Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Initialiser Django
django.setup()
