from django.db import models


class BookManager(models.Manager):
    """
    Manager personnalisé pour le modèle Book.

    Ce manager fournit des méthodes utilitaires pour ajouter un livre à la bibliothèque
    et rechercher des livres par titre.
    """

    def add_to_library(self, title, author):
        """
        Ajouter un nouveau livre à la bibliothèque.

        Args:
            title (str): Le titre du livre.
            author (str): L'auteur du livre.

        Returns:
            Book: L'objet livre qui a été créé et ajouté à la bibliothèque.
        """
        return self.create(title=title, author=author)

    def search_in_title(self, search_title):
        """
        Rechercher des livres dont le titre contient une chaîne donnée.

        Args:
            search_title (str): La chaîne de caractères à rechercher dans les titres des livres.

        Returns:
            QuerySet: Un queryset contenant les livres dont le titre correspond à la recherche.
        """
        return Book.objects.filter(title__icontains=search_title)


class Book(models.Model):
    """
    Modèle représentant un livre dans la bibliothèque.

    Attributs:
        title (str): Le titre du livre.
        author (str): L'auteur du livre.
    """

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    objects = BookManager()

    def __str__(self):
        """
        Retourne une représentation textuelle d'un livre.

        Returns:
            str: Le titre du livre suivi de l'auteur.
        """
        return f"{self.title} par {self.author}"
