from tkinter import Tk, Label, Button, END
from tkinter.scrolledtext import ScrolledText


class EncryptEntry:
    """
    Represents an instance of the encryption entry window.
    """
    def __init__(self) -> None:
        """
        Initialize the window and set up the ui elements and class attributes.
        """
        self.root: Tk = Tk()
        self.root.geometry("500x300+350+150")
        self.root.resizable(False, False)
        self.root.title("Encrypt")

        self.FONT: str = "Courier New"
        self.bg_color: str = "#ddd"

        self.root.config(background=self.bg_color)

        self.message_label: Label = Label(self.root, text="Enter a message:", 
                                          font=(self.FONT, 10), 
                                          background=self.bg_color)
        self.message_label.place(relx=0.05, rely=0.1, anchor="w")

        self.message_input: ScrolledText = ScrolledText(self.root, height=12, 
                                                        width=50, padx=10, pady=5,
                                                        font=(self.FONT, 10),
                                                        wrap="word",
                                                        relief="sunken", 
                                                        borderwidth=3)
        self.message_input.place(relx=0.05, rely=0.15, anchor="nw")
        self.message_input.focus()

        self.submit_button: Button = Button(self.root, text="Encrypt", 
                                            command=self.submit,
                                            font=(self.FONT, 10), width=10)
        self.submit_button.place(relx=0.5, rely=0.92, anchor="center")

        self.menu_button: Button = Button(self.root, text="Back to Menu", 
                                          font=(self.FONT, 8),
                                          command=self.menu)
        self.menu_button.place(relx=0.95, rely=0.92, anchor="e")
        
        self.message_to_encrypt: str = ""

        self.exit_mode: str = ""

        self.root.mainloop()

    
    def submit(self) -> None:
        """
        Submit the user entered plaintext and store it in the class attribute.
        """
        self.message_to_encrypt = self.message_input.get("1.0", END)
        self.exit_mode = "C"
        self.root.destroy()

    
    def menu(self) -> None:
        """
        Set the exit mode to 'M' in order to open the main menu when the
        window is closed.
        """
        self.exit_mode = "M"
        self.root.destroy()


if __name__ == "__main__":
    # test runs the application
    encrypt: EncryptEntry = EncryptEntry()
    print(encrypt.message_to_encrypt)
