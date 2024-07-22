from tkinter import Tk, Label, Button, END
from tkinter.scrolledtext import ScrolledText

from string import ascii_lowercase as l_case, ascii_uppercase as u_case
from itertools import cycle

import subprocess


class DecryptionHandler:
    """
    Represents an instance of the decryption handler.
    """
    def __init__(self, key: str, message: str) -> None:
        """
        Initializes an instance of the decryption handler, receives the
        decryption key and the message to be decrypted and sets up the
        ui elements.

        :param key: the decryption key.
        :param message: the ciphertext to be decrypted.
        """
        self.root: Tk = Tk()
        self.root.geometry("500x300+350+150")
        self.root.resizable(False, False)
        self.root.title("Decryption")

        self.FONT: str = "Courier New"
        self.bg_color: str = "#ddd"

        self.root.config(background=self.bg_color)

        self.message_label: Label = Label(self.root, text="Decrypted Text: ", 
                                          font=(self.FONT, 10),
                                          background=self.bg_color)
        self.message_label.place(relx=0.05, rely=0.05, anchor="nw")

        self.message_display: ScrolledText = ScrolledText(self.root, width=50,
                                                          height=12, padx=10,
                                                          pady=5, relief="sunken",
                                                          font=(self.FONT, 10),
                                                          borderwidth=3,
                                                          state="disabled",
                                                          wrap="word")
        self.message_display.place(relx=0.05, rely=0.15, anchor="nw")

        self.copy_message: Button = Button(self.root, text="Copy", 
                                           font=(self.FONT, 8),
                                           width=5,
                                           command=self.copy_text)
        self.copy_message.place(relx=0.06, rely=0.88, anchor="nw")

        self.menu_button: Button = Button(self.root, text="Back to Menu", 
                                          font=(self.FONT, 8),
                                          command=self.menu)
        self.menu_button.place(relx=0.95, rely=0.91, anchor="e")
        
        self.decryption_key: str = key.upper()
        self.ciphertext: str = message

        self.decryption_text: str = str()

        self.decrypt()

        self.exit_mode: str = ""

        self.root.mainloop()

    
    def decrypt(self) -> None:
        """
        Decrypt the given ciphertext.
        """
        # create full key
        key_letters: list[str] = list(self.decryption_key)
        full_key: str = ''

        index: int = 0
        for _ in range(len(self.ciphertext.strip())):
            full_key += key_letters[index % len(key_letters)]
            index += 1
        
        # remove whitespace and line breaks from the key
        final_key: str = ''
        for letter in full_key:
            if letter.isalpha():
                final_key += letter

        # decrypt each letter
        decrypted_message: str = ""
        roster: cycle = cycle(final_key)
        for char in self.ciphertext:
            if char.isalpha():
                shift_key: str = next(roster)
                shift = u_case.index(shift_key)

                new_letter: str = self.decrypt_letter(shift, char)
                decrypted_message += new_letter
            else: 
                decrypted_message += char

        # display decrypted text in the scrolled text widget
        self.message_display.config(state="normal")
        self.message_display.insert(1.0, decrypted_message)
        self.message_display.config(state="disabled")

        self.decryption_text = decrypted_message


    def decrypt_letter(self, shift: int, letter: str) -> str:
        """
        Decrypt a specific letter with a given right-ward shift applied.

        :param shift: the original right ward shift.
        :param letter:  the letter to be decrypted.
        :return: the decrypted letter.
        """
        if letter.islower():
            shift_index: int = l_case.index(letter)
            ref: str = l_case[shift_index+1:] + l_case[:shift_index+1]
            decrypted_letter: str = ref[-shift-1]
        else:
            shift_index: int = u_case.index(letter)
            ref: str = u_case[shift_index+1:] + u_case[:shift_index+1]
            decrypted_letter: str = ref[-shift-1]
        
        return decrypted_letter


    def copy_text(self) -> int:
        """
        Copy the decrypted text to the clipboard.

        :return: the exit code of the cmd subprocess.
        """
        text: str = str(self.message_display.get(1.0, END)).strip()
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
    handler: DecryptionHandler = DecryptionHandler("DPTFSXPJ", "dimfuh pc gpps")
