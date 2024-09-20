from PySide6.QtWidgets import (QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QVBoxLayout)

from .. import controllers
from .messages import MessageDialog
from .utils import CenteredDialogMixin


class AddBookDialog(QDialog, CenteredDialogMixin):
    """Boîte de dialogue pour ajouter un livre à la bibliothèque."""

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Ajouter un livre")
        self.setGeometry(300, 300, 400, 200)
        self.center_on_parent()

        layout = QVBoxLayout(self)

        # Saisie du titre
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Titre du livre")
        layout.addWidget(self.title_input)

        # Saisie de l'auteur
        self.author_input = QLineEdit(self)
        self.author_input.setPlaceholderText("Auteur du livre")
        layout.addWidget(self.author_input)

        # Boutons d'action (Ajouter, Annuler)
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self
        )
        buttons.accepted.connect(self.add_book)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def add_book(self):
        """Ajoute un livre si les informations sont valides."""
        title = self.title_input.text().strip()
        author = self.author_input.text().strip()

        if not title or not author:
            # Si le titre ou l'auteur est manquant, afficher une erreur
            missing_fields = []
            if not title:
                missing_fields.append("titre")
            if not author:
                missing_fields.append("auteur")

            MessageDialog(
                self,
                f"Veuillez fournir un {', '.join(missing_fields)}.",
                message_type="error",
            ).exec()
        else:
            controllers.add_book(
                title, author
            )  # Appel au contrôleur pour ajouter le livre
            self.parent.load_books()  # Met à jour la liste des livres dans la fenêtre principale
            self.accept()


class RemoveBookDialog(QDialog, CenteredDialogMixin):
    """Boîte de dialogue pour confirmer la suppression d'un livre."""

    def __init__(self, parent, book, callback):
        super().__init__(parent)
        self.book = book
        self.callback = callback
        self.setWindowTitle("Confirmation de suppression")
        self.setGeometry(300, 300, 300, 150)
        self.center_on_parent()

        layout = QVBoxLayout(self)

        # Message de confirmation
        message = QLabel(
            f"Voulez-vous supprimer le livre '{self.book.title}' par {self.book.author} ?",
            self,
        )
        layout.addWidget(message)

        # Boutons Oui / Non
        button_layout = QHBoxLayout()
        yes_button = QPushButton("Oui", self)
        yes_button.clicked.connect(self.delete_book)
        button_layout.addWidget(yes_button)

        no_button = QPushButton("Non", self)
        no_button.clicked.connect(self.reject)
        button_layout.addWidget(no_button)

        layout.addLayout(button_layout)

    def delete_book(self):
        """Supprime le livre et recharge la liste après suppression."""
        controllers.remove_book(self.book)
        self.callback()  # Recharge la liste des livres dans la fenêtre principale
        self.accept()


class SearchBookDialog(QDialog, CenteredDialogMixin):
    """Boîte de dialogue pour rechercher des livres par titre pour suppression."""

    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Rechercher un livre à supprimer")
        self.setGeometry(400, 200, 300, 100)
        self.center_on_parent()

        layout = QVBoxLayout(self)

        # Champ de saisie pour la recherche
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Entrez un titre de livre")
        layout.addWidget(self.search_input)

        # Boutons Rechercher / Annuler
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.search_input.setFocus()

    def accept(self):
        """Recherche les livres correspondant au titre et demande confirmation pour chaque suppression."""
        search_title = self.search_input.text().strip()
        if search_title:
            books = controllers.search_books_by_title(search_title)
            if books:
                # Confirmation pour chaque livre trouvé
                self.parent().confirm_delete(books)
            else:
                MessageDialog(self, "Aucun livre trouvé", "info").exec()
        super().accept()
