import customtkinter as ctk
from .. import controllers
from .messages import MessageModal
from .utils import CenteredModalMixin


class AddBookModal(ctk.CTkToplevel, CenteredModalMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Ajouter un livre")
        self.geometry("400x300")
        self.center_window(parent)

        # Champs pour le titre
        self.label_title = ctk.CTkLabel(self, text="Titre du livre")
        self.label_title.pack(pady=10)
        self.entry_title = ctk.CTkEntry(self)
        self.entry_title.pack(pady=10)

        # Champs pour l'auteur
        self.label_author = ctk.CTkLabel(self, text="Auteur du livre")
        self.label_author.pack(pady=10)
        self.entry_author = ctk.CTkEntry(self)
        self.entry_author.pack(pady=10)

        # Bouton pour ajouter le livre
        self.add_button = ctk.CTkButton(
            self, text="Ajouter le livre", command=self.add_book
        )
        self.add_button.pack(pady=20)

        self.grab_set()

    def add_book(self):
        """Vérifie les champs avant d'ajouter un livre et demande les informations manquantes si nécessaire."""
        title = self.entry_title.get().strip()  # Supprimer les espaces vides
        author = self.entry_author.get().strip()

        if not title or not author:
            missing_fields = []
            if not title:
                missing_fields.append("titre")
            if not author:
                missing_fields.append("auteur")

            # Afficher un message avec les champs manquants
            MessageModal(
                self,
                message=f"Veuillez fournir un {', '.join(missing_fields)}.",
                message_type="error",
            ).grab_set()
        else:
            # Si les deux champs sont fournis, ajoutez le livre via le contrôleur
            controllers.add_book(title, author)
            self.parent.load_books()  # Mettre à jour la liste des livres
            self.destroy()


class RemoveBookModal(ctk.CTkToplevel, CenteredModalMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Supprimer un livre")
        self.geometry("400x300")
        self.center_window(parent)

        # Champ de recherche
        self.label_search = ctk.CTkLabel(
            self, text="Rechercher un livre par titre"
        )
        self.label_search.pack(pady=10)
        self.entry_search = ctk.CTkEntry(self)
        self.entry_search.pack(pady=10)

        # Bouton pour rechercher et supprimer un livre
        self.search_button = ctk.CTkButton(
            self, text="Rechercher et supprimer", command=self.search_books
        )
        self.search_button.pack(pady=20)

        self.grab_set()

    def search_books(self):
        """Rechercher les livres par titre et demander confirmation pour suppression."""
        search_title = self.entry_search.get()
        books = controllers.search_books_by_title(search_title)

        if not books:
            from .messages import MessageModal

            MessageModal(
                self, message="Aucun livre trouvé", message_type="info"
            ).grab_set()
        else:
            ConfirmDeleteModal(
                self, books, self.parent.book_deleted
            ).grab_set()


class ConfirmDeleteModal(ctk.CTkToplevel, CenteredModalMixin):
    def __init__(self, parent, book, callback):
        super().__init__(parent)
        self.book = book
        self.callback = callback
        self.title("Confirmation de suppression")
        self.geometry("300x200")
        self.center_window(parent)

        message = f"Voulez-vous supprimer le livre '{book.title}' par {book.author} ?"
        self.label_confirm = ctk.CTkLabel(self, text=message, wraplength=250)
        self.label_confirm.pack(pady=20)

        # Boutons
        self.yes_button = ctk.CTkButton(
            self, text="Oui", command=self.delete_book
        )
        self.yes_button.pack(side="left", padx=10, pady=20)
        self.no_button = ctk.CTkButton(self, text="Non", command=self.close)
        self.no_button.pack(side="right", padx=10, pady=20)

        self.grab_set()

    def delete_book(self):
        """Supprimer le livre via le contrôleur et fermer."""
        controllers.remove_book(self.book)
        self.callback()
        self.close()

    def close(self):
        """Ferme la fenêtre modale."""
        self.destroy()
