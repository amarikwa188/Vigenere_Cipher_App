from tkinter import Tk, Label, StringVar, Button, END
from tkinter.scrolledtext import ScrolledText

from string import ascii_uppercase as u_case, ascii_lowercase as l_case
import random as rng
from itertools import cycle

import subprocess


class EncryptionHandler:
    """
    Represents an instance of the encryption handler.
    """
    def __init__(self, message: str) -> None:
        """
        Initializes an instance of the encryption handler, receives the message
        to be encrypted and sets up the ui elements.

        :param message: the plaintext to be encrypted.
        """
        self.root: Tk = Tk()
        self.root.geometry("500x300+350+150")
        self.root.resizable(False, False)
        self.root.title("Encryption")

        self.FONT: str = "Courier New"
        self.bg_color: str = "#ddd"

        self.root.config(background=self.bg_color)

        self.key_label: Label = Label(self.root, text="KEY -> ",
                                      background=self.bg_color,
                                      font=(self.FONT, 10))
        self.key_label.place(relx=0.05, rely=0.12, anchor="w")

        self.key_display: Label = Label(self.root, text="XXXXX", 
                                        relief="sunken", width=15,
                                        font=(self.FONT, 13),
                                        justify="center")
        self.key_display.place(relx=0.18, rely=0.12, anchor="w")

        self.key_copy_button: Button = Button(self.root, text="Copy",
                                              command=self.copy_key,
                                              font=(self.FONT, 8))
        self.key_copy_button.place(relx=0.52, rely=0.1205, anchor="w")

        self.message_label: Label = Label(self.root, text="Encrypted Text:", 
                                          background=self.bg_color,
                                          font=(self.FONT, 10))
        self.message_label.place(relx=0.05, rely=0.26, anchor="w")

        self.message_text: ScrolledText = ScrolledText(self.root, height=9,
                                                       width=50, padx=10, pady=5,
                                                       font=(self.FONT, 10),
                                                       wrap="word",
                                                       relief="sunken",
                                                       borderwidth=3,
                                                       state="disabled") 
        self.message_text.place(relx=0.05, rely=0.3, anchor="nw")

        self.copy_message_button: Button = Button(self.root, text="Copy",
                                                  command=self.copy_message,
                                                  width=7, font=(self.FONT, 8))
        self.copy_message_button.place(relx=0.06, rely=0.91, anchor="w")

        self.menu_button: Button = Button(self.root, text="Back to Menu",
                                          font=(self.FONT, 8),
                                          command=self.menu)
        self.menu_button.place(relx=0.95, rely=0.91, anchor="e")

        self.key_value: StringVar = StringVar(value=self.generate_key())
        self.plaintext: str = message

        self.encrypted_text: str = str()

        self.encrypt()

        self.exit_mode: str = ""

        self.root.mainloop()


    def generate_key(self) -> str:
        """
        Genereates a random key to be used for encryption.

        :return: a 4-8 digit capital letter key.
        """
        length: int = rng.randint(4, 8)
        key: str = ''

        for _ in range(length):
            key += rng.choice(u_case)
 
        self.key_display.config(text="X"*len(key))

        return key


    def encrypt(self) -> None:
        """
        Encrypt the given plaintext using the Vigenere cipher algorithm.
        """
        # create full key of the length of plaintext
        key_letters: list[str] = list(self.key_value.get())
        full_key: str = ''

        index: int = 0
        for _ in range(len(self.plaintext.strip())):
            full_key += key_letters[index % len(key_letters)]
            index += 1

        # encrypt each letter
        encrypted_message: str = ""
        roster: cycle = cycle(full_key)
        for char in self.plaintext:
            if char.isalpha():
                shift_key: str = next(roster)
                shift = u_case.index(shift_key)

                new_letter: str = self.encrypt_letter(shift, char)
                encrypted_message += new_letter
            else:
                encrypted_message += char
        
        # display encrypted text in the scrolled text widget
        self.message_text.config(state="normal")
        self.message_text.insert(1.0, encrypted_message)
        self.message_text.config(state="disabled")

        self.encrypted_text = encrypted_message

    
    def encrypt_letter(self, shift: int, letter: str) -> str:
        """
        Encrypt a specific letter with a given right-ward shift value.

        :param shift: the right ward shift.
        :param letter: the letter to be encrypted.
        :return: the encrypted letter.
        """
        if letter.islower():
            ref: str = l_case[shift:] + l_case[:shift]
            encrypted_letter: str = ref[l_case.index(letter)]
        else:
            ref: str = u_case[shift:] + u_case[:shift]
            encrypted_letter: str = ref[u_case.index(letter)]

        return encrypted_letter


    def copy_key(self) -> int:
        """
        Copy the encryption key to the clipboard.

        :return: the exit code of the cmd subprocess.
        """
        text: str = self.key_value.get().strip()
        cmd: str = f"echo {text}|clip"
        return subprocess.check_call(cmd, shell=True)


    def copy_message(self) -> int:
        """
        Copy the encrypted text to the clipboard.

        :return: the exit code of the cmd subprocess.
        """
        text: str = self.encrypted_text.strip()
        cmd: str = f"echo {text}|clip"
        return subprocess.check_call(cmd, shell=True)
    

    def menu(self) -> None:
        """
        Set the exit mode to 'M' in order to open the main menu when the
        window is closed.
        """
        self.exit_mode = "M"
        self.root.destroy()


if __name__ == "__main__":
    # message: str = "attacking tonight"
    message: str = "attack at dawn"
    handler: EncryptionHandler = EncryptionHandler(message)