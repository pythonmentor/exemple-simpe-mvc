import customtkinter as ctk

from .. import controllers
from .actions import AddBookModal, RemoveBookModal
from .menu import AppMenu


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de Bibliothèque")
        self.geometry("600x500")

        # Initialiser le menu via la classe AppMenu
        self.menu_bar = AppMenu(self)
        self.config(menu=self.menu_bar)

        # Créer un bouton "Ajouter" en haut qui prend toute la largeur
        self.add_button = ctk.CTkButton(
            self, text="Ajouter un livre", command=self.open_add_book_modal
        )
        self.add_button.pack(fill="x", padx=20, pady=10)

        # Frame pour afficher la liste des livres
        self.book_frame = ctk.CTkFrame(self)
        self.book_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.load_books()  # Charger la liste des livres

    def load_books(self):
        """Charge et affiche la liste des livres avec un bouton 'Supprimer'."""
        for widget in self.book_frame.winfo_children():
            widget.destroy()

        books = controllers.list_books()
        if not books:
            label_no_books = ctk.CTkLabel(
                self.book_frame, text="Aucun livre disponible."
            )
            label_no_books.pack(pady=10)
        else:
            for book in books:
                book_row = ctk.CTkFrame(self.book_frame)
                book_row.pack(fill="x", pady=5)

                book_label = ctk.CTkLabel(
                    book_row, text=f"{book.title} par {book.author}"
                )
                book_label.pack(side="left", padx=10)

                delete_button = ctk.CTkButton(
                    book_row,
                    text="Supprimer",
                    command=lambda b=book: self.confirm_delete(b),
                )
                delete_button.pack(side="right", padx=10)

    def confirm_delete(self, book):
        """Ouvre une modale de confirmation pour supprimer un livre."""
        from .actions import ConfirmDeleteModal

        ConfirmDeleteModal(self, book, self.book_deleted).grab_set()

    def book_deleted(self):
        """Callback après suppression d'un livre. Recharge la liste des livres."""
        self.load_books()

    def open_add_book_modal(self):
        """Ouvrir la fenêtre modale pour ajouter un livre."""
        AddBookModal(self).grab_set()

    def open_remove_book_modal(self):
        """Ouvrir la fenêtre modale pour supprimer un livre."""
        RemoveBookModal(self).grab_set()
