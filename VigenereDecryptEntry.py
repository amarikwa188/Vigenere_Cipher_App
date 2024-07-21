from tkinter import Tk, Label, Entry, Button, END
from tkinter.scrolledtext import ScrolledText


class DecryptEntry:
    """
    Represents an instance of the decryption entry window.
    """
    def __init__(self) -> None:
        """
        Initialize the window and set up the ui elements and application variables.
        """
        self.root: Tk = Tk()
        self.root.geometry("500x300+350+150")
        self.root.resizable(False, False)
        self.root.title("Decrypt")

        self.FONT: str = "Courier New" 
        self.bg_color: str = "#ddd"

        self.root.config(background=self.bg_color)

        self.enter_key_label: Label = Label(self.root, 
                                            text="Enter Encryption Key -> ", 
                                            background=self.bg_color,
                                            font=(self.FONT, 10))
        self.enter_key_label.place(relx=0.05, rely=0.1, anchor="nw")

        self.key_entry: Entry = Entry(self.root, font=(self.FONT, 10),
                                      justify="center", show="X")
        self.key_entry.place(relx=0.45, rely=0.11, anchor="nw")

        self.enter_text_label: Label = Label(self.root, font=(self.FONT, 10),
                                             text="Enter Encrypted Text: ",
                                             background=self.bg_color)
        self.enter_text_label.place(relx=0.05, rely=0.22, anchor="nw")

        self.text_entry: ScrolledText = ScrolledText(self.root, width=50, 
                                                     height=9, padx=10, pady=5,
                                                     wrap="word", 
                                                     relief="sunken",
                                                     borderwidth=3,
                                                     font=(self.FONT, 10))
        self.text_entry.place(relx=0.05, rely=0.3, anchor="nw")

        self.submit_button: Button = Button(self.root, text="Decrypt",
                                             font=(self.FONT, 8),
                                             command=self.submit)
        self.submit_button.place(relx=0.5, rely=0.91, anchor="center")

        self.menu_button: Button = Button(self.root, text="Back to Menu",
                                          font=(self.FONT, 8), 
                                          command=self.menu)
        self.menu_button.place(relx=0.95, rely=0.91, anchor="e")

        self.decryption_key: str = ''
        self.message_to_decrypt: str = ''

        self.exit_mode: str = ""
        
        self.root.mainloop()

    
    def submit(self) -> None:
        """
        Submit the user entered key and ciphertext and store it in
        class attributes.
        """
        self.decryption_key = self.key_entry.get().upper()
        self.message_to_decrypt = self.text_entry.get("1.0", END)
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
    decrypt: DecryptEntry = DecryptEntry()
    print(decrypt.decryption_key)
    print(decrypt.message_to_decrypt)