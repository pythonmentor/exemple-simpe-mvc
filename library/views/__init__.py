import customtkinter as ctk

from .main import MainWindow


def main():
    """Point d'entrée principal pour lancer l'application."""
    ctk.set_appearance_mode("dark")  # Activer le mode sombre
    ctk.set_default_color_theme("dark-blue")  # Personnalisation des couleurs
    app = MainWindow()
    app.mainloop()
