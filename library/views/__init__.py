import sys

from PySide6.QtWidgets import QApplication

from .main import MainWindow

theme = """
QMainWindow {
    background-color: #1E1E1E;
    color: #D4D4D4;
}

QLabel {
    color: #D4D4D4;
}

QPushButton {
    background-color: #007ACC;
    color: #FFFFFF;
    border: 1px solid #005A9E;
    border-radius: 5px;
    padding: 5px;
}

QPushButton:hover {
    background-color: #005A9E;
}

QPushButton:pressed {
    background-color: #003E6B;
}

QLineEdit, QTextEdit {
    background-color: #2D2D2D;
    color: #D4D4D4;
    border: 1px solid #3C3C3C;
    border-radius: 5px;
}

QMenuBar {
    background-color: #252526;
    color: #D4D4D4;
}

QMenu {
    background-color: #252526;
    color: #D4D4D4;
}

QMenu::item:selected {
    background-color: #373737;
}

/* Fenêtres de dialogue */
QDialog {
    background-color: #1E1E1E;
    color: #D4D4D4;
}

/* Labels et autres widgets dans les dialogues */
QDialog QLabel {
    color: #D4D4D4;
}

/* Boutons dans les dialogues */
QDialog QPushButton {
    background-color: #007ACC;
    color: #FFFFFF;
    border: 1px solid #005A9E;
    border-radius: 5px;
    padding: 5px;
}

QDialog QPushButton:hover {
    background-color: #005A9E;
}

QDialog QPushButton:pressed {
    background-color: #003E6B;
}

QDialog QLineEdit {
    background-color: #2D2D2D;
    color: #D4D4D4;
    border: 1px solid #3C3C3C;
    border-radius: 5px;
}

QDialogButtonBox QPushButton {
    background-color: #007ACC;
    color: #FFFFFF;
    border: 1px solid #005A9E;
    border-radius: 5px;
    padding: 5px;
}

QDialogButtonBox QPushButton:hover {
    background-color: #005A9E;
}

QDialogButtonBox QPushButton:pressed {
    background-color: #003E6B;
}
"""


def main():
    """Point d'entrée principal pour lancer l'application."""
    app = QApplication(sys.argv)
    # Appliquer le thème globalement
    app.setStyleSheet(theme)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
