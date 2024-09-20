from . import messages
from .models import Book


def add_book(title, author):
    """
    Ajouter un livre à la bibliothèque.

    Cette fonction crée un nouveau livre dans la base de données avec le titre et l'auteur fournis.

    Args:
        title (str): Le titre du livre.
        author (str): L'auteur du livre.

    Returns:
        Book: L'objet livre qui a été ajouté à la bibliothèque.
    """
    book = Book.objects.add_to_library(title=title, author=author)
    messages.success(f"Livre ajouté : {title} par {author}")
    return book


def list_books():
    """
    Lister tous les livres de la bibliothèque.

    Cette fonction récupère tous les livres présents dans la base de données et les renvoie sous forme de queryset.

    Returns:
        QuerySet: Un queryset contenant tous les livres de la bibliothèque.
    """
    books = Book.objects.all()
    if not books:
        messages.info("Aucun livre disponible.")
    return books


def search_books_by_title(search_title):
    """
    Rechercher des livres par titre.

    Cette fonction recherche tous les livres dont le titre contient la chaîne de caractères fournie.
    La recherche est insensible à la casse.

    Args:
        search_title (str): La chaîne de caractères à rechercher dans les titres des livres.

    Returns:
        QuerySet: Un queryset contenant les livres correspondants à la recherche.
    """
    books = Book.objects.search_in_title(search_title)
    if not books:
        messages.info("Aucun livre trouvé correspondant à '{search_title}'.")
    return books


def remove_book(book):
    """
    Supprimer un livre de la bibliothèque.

    Cette fonction supprime le livre fourni de la base de données.

    Args:
        book (Book): L'objet livre à supprimer.

    Returns:
        None
    """
    book.delete()
    messages.info(f"Livre supprimé : {book.title} par {book.author}")
