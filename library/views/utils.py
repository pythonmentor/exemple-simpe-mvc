from PySide6.QtCore import QRect
from PySide6.QtWidgets import QWidget


class CenteredDialogMixin:
    def center_on_parent(self):
        """Centre la fenêtre modale par rapport à la fenêtre parente."""
        parent_instance = (
            self.parent() if callable(self.parent) else self.parent
        )  # Récupérer correctement l'instance du parent
        if isinstance(
            parent_instance, QWidget
        ):  # Vérifier si le parent est un QWidget ou similaire
            parent_geometry = (
                parent_instance.geometry()
            )  # Obtenir la géométrie du parent
            self_geometry = (
                self.geometry()
            )  # Obtenir la géométrie de la fenêtre modale
            x = (
                parent_geometry.x()
                + (parent_geometry.width() - self_geometry.width()) // 2
            )
            y = (
                parent_geometry.y()
                + (parent_geometry.height() - self_geometry.height()) // 2
            )
            self.setGeometry(
                QRect(x, y, self_geometry.width(), self_geometry.height())
            )
        else:
            # Si le parent n'est pas défini, on affiche un avertissement (optionnel)
            print("Aucun parent valide pour centrer la fenêtre.")
