# Registre centralisé des messages
_message_registry = []


def success(message):
    """Ajoute un message de succès dans le registre."""
    _message_registry.append({"type": "success", "text": message})


def error(message):
    """Ajoute un message d'erreur dans le registre."""
    _message_registry.append({"type": "error", "text": message})


def info(message):
    """Ajoute un message d'information dans le registre."""
    _message_registry.append({"type": "info", "text": message})


def get_messages():
    """Générateur qui retourne et supprime les messages du registre un par un."""
    while _message_registry:
        # Utiliser pop(0) pour récupérer et supprimer le premier message de la liste
        yield _message_registry.pop(0)
