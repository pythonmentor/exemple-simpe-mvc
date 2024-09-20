from functools import wraps

import typer
from django.core.management import call_command

from library import controllers, messages

app = typer.Typer()


def display_messages():
    """
    Affiche une liste de messages avec un symbole distinctif selon le type de message.

    Affiche:
        Les messages avec un symbole distinctif pour chaque type:
        - ✅ pour succès.
        - ❌ pour erreur.
        - ℹ️ pour information.
    """
    for message in messages.get_messages():
        msg_type = message.get("type")
        msg_text = message.get("text")

        if msg_type == "success":
            typer.echo(f"\n✅ Succès : {msg_text}")
        elif msg_type == "error":
            typer.echo(f"\n❌ Erreur : {msg_text}")
        elif msg_type == "info":
            typer.echo(f"\nℹ️ Info : {msg_text}")
        else:
            typer.echo(f"\n🔔 Autre : {msg_text}")


@app.command()
def init():
    """
    Initialiser la base de données en appliquant les migrations.

    Cette commande exécute les migrations nécessaires pour initialiser la base de données.
    """
    call_command("migrate")
    messages.info("Base de données initialisée.")
    display_messages()


@app.command()
def makemigrations():
    """
    Créer les migrations pour la base de données.

    Cette commande génère les migrations basées sur les modifications apportées aux modèles.
    """
    call_command("makemigrations")
    messages.info("Les migrations ont été créées avec succès.")
    display_messages()


@app.command()
def add_book(title: str, author: str):
    """
    Ajouter un nouveau livre à la base de données.

    Cette commande ajoute un livre avec un titre et un auteur fournis par l'utilisateur.

    Args:
        title (str): Le titre du livre.
        author (str): L'auteur du livre.

    Example:
        $ python manage.py add_book "Le Petit Prince" "Antoine de Saint-Exupéry"
    """
    book = controllers.add_book(title, author)
    display_messages()


@app.command()
def list_books():
    """
    Lister tous les livres dans la base de données.

    Cette commande affiche la liste de tous les livres actuellement dans la base de données.
    Si aucun livre n'est trouvé, un message informatif est affiché.
    """
    books = controllers.list_books()
    for book in books:
        typer.echo(f"- {book.title} par {book.author}")
    display_messages()


@app.command()
def remove_books(in_title_search: str):
    """
    Supprimer plusieurs livres correspondant à une recherche.

    Cette commande permet de rechercher des livres dans la base de données en fonction d'une chaîne de caractères dans le titre.
    L'utilisateur est invité à confirmer la suppression pour chaque livre trouvé.

    Args:
        in_title_search (str): Une chaîne de caractères pour rechercher des livres par titre.

    Example:
        $ python manage.py remove_books "Prince"
    """
    books = controllers.search_books_by_title(in_title_search)
    for book in books:
        confirm = typer.confirm(
            f">> Êtes-vous sûr de vouloir supprimer le livre '{book.title}'?"
        )
        if confirm:
            controllers.remove_book(book)
        else:
            messages.info(f"-> La suppression de '{book.title}' annulée.")
        display_messages()

    display_messages()


@app.command()
def remove_all_books():
    """
    Supprimer tous les livres de la base de données.

    Cette commande demande confirmation avant de supprimer chaque livre présent dans la base de données.
    """
    books = controllers.list_books()
    for book in books:
        confirm = typer.confirm(
            f">> Êtes-vous sûr de vouloir supprimer le livre '{book.title}'?"
        )
        if confirm:
            controllers.remove_book(book)
        else:
            messages.info(f"La suppression de '{book.title}' annulée.")
        display_messages()

    display_messages()


if __name__ == "__main__":
    app()
