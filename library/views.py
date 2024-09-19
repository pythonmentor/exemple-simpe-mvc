from . import controllers


def show_books():
    """
    Afficher la liste des livres disponibles.

    Cette fonction récupère tous les livres à partir du contrôleur et les affiche.
    Si aucun livre n'est trouvé, un message d'information est affiché.

    Returns:
        function: Retourne la fonction `display_menu` pour revenir au menu principal.
    """
    books = controllers.list_books()
    if not books:
        print("-> Aucun livre disponible.")
    else:
        for book in books:
            print(f"-> {book.title} par {book.author}")
    return display_menu


def prompt_add_book():
    """
    Demander à l'utilisateur d'ajouter un livre.

    Cette fonction demande à l'utilisateur d'entrer le titre et l'auteur d'un livre,
    puis utilise le contrôleur pour ajouter le livre à la bibliothèque. Un message
    de confirmation est affiché après l'ajout.

    Returns:
        function: Retourne la fonction `display_menu` pour revenir au menu principal.
    """
    title = input(">> Entrez le titre du livre : ")
    author = input(">> Entrez l'auteur du livre : ")
    controllers.add_book(title, author)
    print(f"-> Livre ajouté : {title} par {author}")
    return display_menu


def prompt_remove_book():
    """
    Demander à l'utilisateur de rechercher et de supprimer un livre.

    Cette fonction permet de rechercher un livre par titre, puis demande à l'utilisateur
    de confirmer la suppression pour chaque livre trouvé. Si aucun livre n'est trouvé,
    un message est affiché.

    L'utilisateur peut aussi revenir au menu principal en entrant 'm'.

    Returns:
        function: Retourne la fonction `display_menu` pour revenir au menu principal.
    """
    search_title = input(
        ">> Entrez une partie du titre du livre à rechercher (ou m pour revenir au menu): "
    )

    if search_title.strip() == "m":
        return display_menu

    # Recherche les livres correspondants au critère
    books = controllers.search_books_by_title(search_title)

    if not books:
        print(f"-> Aucun livre trouvé correspondant à '{search_title}'.")
        return display_menu

    # Demander confirmation pour chaque livre
    for book in books:
        confirmation = input(
            f">> Voulez-vous supprimer '{book.title}' par {book.author} ? (o/n) ou m pour revenir au menu : "
        ).lower()
        if confirmation == "o":
            controllers.remove_book(book)
            print(f"-> Livre supprimé : {book.title} par {book.author}")
        elif confirmation == "m":
            return display_menu
        else:
            print(f"-> Livre conservé : {book.title} par {book.author}")

    return display_menu


def display_menu():
    """
    Afficher le menu principal de l'application.

    Cette fonction affiche les options disponibles (lister, ajouter, supprimer un livre
    ou quitter). Elle renvoie la fonction correspondante à l'option choisie.

    Returns:
        function: Retourne la fonction choisie par l'utilisateur (ou None pour quitter).
    """
    print("\n1. Lister les livres")
    print("2. Ajouter un livre")
    print("3. Supprimer un livre")
    print("4. Quitter")
    choice = input("\nChoisissez une option : ")

    if choice == "1":
        return show_books
    elif choice == "2":
        return prompt_add_book
    elif choice == "3":
        return prompt_remove_book
    elif choice == "4":
        print("-> Au revoir :)")
    else:
        print("-> Option invalide, veuillez réessayer.")
        return display_menu


def main():
    """
    Point d'entrée principal de l'application.

    Cette fonction lance le programme et affiche le menu en boucle, permettant à
    l'utilisateur de choisir des actions jusqu'à ce qu'il décide de quitter.
    """
    action = display_menu
    while action is not None:
        action = action()
