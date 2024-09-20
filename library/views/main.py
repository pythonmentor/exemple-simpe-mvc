from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from .. import controllers
from .actions import AddBookDialog, RemoveBookDialog
from .menu import AppMenu
from .messages import MessageDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion de Bibliothèque")
        self.setGeometry(100, 100, 600, 500)

        # Initialiser le menu via la classe AppMenu
        self.menu_bar = AppMenu(self)
        self.setMenuBar(self.menu_bar)

        # Créer un widget central pour afficher les livres et les boutons
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(
            central_widget
        )  # Layout vertical pour tout aligner en haut
        layout.setAlignment(Qt.AlignTop)

        # Bouton "Ajouter un livre"
        self.add_button = QPushButton("Ajouter un livre")
        self.add_button.clicked.connect(self.open_add_book_dialog)
        layout.addWidget(self.add_button)

        # Frame pour afficher la liste des livres
        self.book_frame = QFrame(self)
        self.book_frame_layout = QVBoxLayout(self.book_frame)
        self.book_frame_layout.setAlignment(Qt.AlignTop)
        layout.addWidget(self.book_frame)

        self.load_books()

    def load_books(self):
        """Charge et affiche la liste des livres avec un bouton 'Supprimer'."""
        # Supprimer les widgets précédents dans le layout
        for i in reversed(range(self.book_frame_layout.count())):
            widget = self.book_frame_layout.itemAt(i).widget()
            widget.setParent(None)

        books = controllers.list_books()
        if not books:
            label_no_books = QLabel("Aucun livre disponible.")
            self.book_frame_layout.addWidget(label_no_books)
        else:
            for book in books:
                book_row = QFrame(self.book_frame)
                row_layout = QHBoxLayout(book_row)
                label = QLabel(f"{book.title} par {book.author}")
                row_layout.addWidget(label)

                delete_button = QPushButton("Supprimer")
                delete_button.clicked.connect(
                    lambda checked, b=book: self.confirm_delete([b])
                )
                row_layout.addWidget(delete_button)

                # Ajouter chaque livre à la disposition verticale
                self.book_frame_layout.addWidget(book_row)

    def confirm_delete(self, books):
        """Ouvre une boîte de dialogue de confirmation pour supprimer plusieurs livres."""
        for book in books:
            confirm_dialog = RemoveBookDialog(self, book, self.book_deleted)
            confirm_dialog.exec()

    def open_add_book_dialog(self):
        """Ouvrir la boîte de dialogue pour ajouter un livre."""
        add_book_dialog = AddBookDialog(self)
        add_book_dialog.exec()

    def open_remove_book_dialog(self):
        """Ouvrir une boîte de dialogue pour rechercher des livres à supprimer."""
        search_dialog = SearchBookDialog(self)
        search_dialog.exec()

    def close_application(self):
        """Quitter l'application proprement."""
        self.close()

    def book_deleted(self):
        """Callback après suppression d'un livre. Recharge la liste des livres."""
        self.load_books()


class SearchBookDialog(QDialog):
    """Boîte de dialogue pour rechercher des livres par titre."""

    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Rechercher un livre à supprimer")
        self.setGeometry(400, 200, 300, 100)

        layout = QVBoxLayout(self)

        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Entrez un titre de livre")
        layout.addWidget(self.search_input)

        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.search_input.setFocus()

    def accept(self):
        search_title = self.search_input.text().strip()
        if search_title:
            books = controllers.search_books_by_title(search_title)
            if books:
                self.parent().confirm_delete(books)
            else:
                MessageDialog(self, "Aucun livre trouvé", "info").exec()
        super().accept()
