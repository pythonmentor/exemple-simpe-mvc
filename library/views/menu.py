from tkinter import Menu


class AppMenu(Menu):
    def __init__(self, parent):
        super().__init__(parent)

        # Menu "Fichier"
        file_menu = Menu(self, tearoff=0)
        file_menu.add_command(
            label="Ajouter un livre",
            accelerator="Ctrl+N",
            command=parent.open_add_book_modal,
        )
        file_menu.add_command(
            label="Supprimer un livre",
            accelerator="Ctrl+D",
            command=parent.open_remove_book_modal,
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Quitter", accelerator="Ctrl+Q", command=parent.quit
        )

        # Ajouter le menu à la fenêtre principale
        self.add_cascade(label="Fichier", menu=file_menu)

        # Assigner les raccourcis clavier dans la fenêtre principale
        parent.bind_all(
            "<Control-n>", lambda event: parent.open_add_book_modal()
        )
        parent.bind_all(
            "<Control-d>", lambda event: parent.open_remove_book_modal()
        )
        parent.bind_all("<Control-q>", lambda event: parent.quit())
