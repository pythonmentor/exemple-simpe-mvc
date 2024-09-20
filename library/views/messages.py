import customtkinter as ctk
from .utils import CenteredModalMixin


class MessageModal(ctk.CTkToplevel, CenteredModalMixin):
    def __init__(self, parent, message, message_type="info"):
        super().__init__(parent)
        self.title("Message")
        self.geometry("300x200")
        self.configure(fg_color="white")

        if message_type == "error":
            self.message_label = ctk.CTkLabel(
                self, text=message, font=("Arial", 20), text_color="red"
            )
        else:
            self.message_label = ctk.CTkLabel(
                self, text=message, font=("Arial", 20), text_color="black"
            )

        self.message_label.place(relx=0.5, rely=0.4, anchor="center")

        close_button = ctk.CTkButton(self, text="Fermer", command=self.close)
        close_button.place(relx=0.5, rely=0.6, anchor="center")

        self.grab_set()

    def close(self):
        self.destroy()
