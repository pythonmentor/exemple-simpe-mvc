import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar


class AppMenu(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)

        # Menu "Fichier"
        file_menu = self.addMenu("Fichier")

        # Action "Ajouter un livre"
        add_book_action = QAction("Ajouter un livre", self)
        add_book_action.setShortcut("Ctrl+N")
        add_book_action.triggered.connect(parent.open_add_book_dialog)
        file_menu.addAction(add_book_action)

        # Action "Supprimer un livre"
        remove_book_action = QAction("Supprimer un livre", self)
        remove_book_action.setShortcut("Ctrl+D")
        remove_book_action.triggered.connect(parent.open_remove_book_dialog)
        file_menu.addAction(remove_book_action)

        file_menu.addSeparator()

        # Action "Supprimer un livre"
        quit_action = QAction("Quitter", self)
        quit_action.setShortcut("Ctrl+Q")
        quit_action.triggered.connect(parent.close_application)
        file_menu.addAction(quit_action)
