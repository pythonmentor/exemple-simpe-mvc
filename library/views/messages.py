from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout

from .utils import CenteredDialogMixin


class MessageDialog(QDialog, CenteredDialogMixin):
    def __init__(self, parent, message, message_type="info"):
        super().__init__(parent)
        self.setWindowTitle("Message")
        self.setGeometry(300, 300, 300, 150)
        self.center_on_parent()

        layout = QVBoxLayout(self)

        label = QLabel(message, self)
        if message_type == "error":
            label.setStyleSheet("color: red;")
        layout.addWidget(label)

        close_button = QPushButton("Fermer", self)
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)
