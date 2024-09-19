# Exemples de micro-applications Python MVC

Cet exemple montre comment structurer un mini-projet en ligne de commande selon
un pattern architectural comme MVC.

Cet exemple utilise Django pour la gérer la base de données et la logique métier.
Ainsi, la séparation des préoccupation rend relativement aisé la transformation de
cette application en une application web.

## Installation des dépendances

Pour installer les dépendances du projet, commencer par **créer et activez un environnement
virtuel**. 

Ensuite, installez les dépendances de l'exemple avec `pip install -r requirements.txt`.

## Initialisation de la base de données

Pour initialiser la base de données, il suffit d'exécuter la commande `python manage.py init` dans 
l'environnement virtuel activé.

## Démarrer l'application

Une fois que la base de données a été initialisée, l'application se lance avec la commande `python -m library`.