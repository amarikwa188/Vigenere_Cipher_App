from VigenereCipherMenu import Menu
from VigenereEncryptEntry import EncryptEntry
from VigenereEncryptHandler import EncryptionHandler
from VigenereDecryptEntry import DecryptEntry
from VigenereDecryptHandler import DecryptionHandler

"""
The main program allows the user to navigate between the menu and encryption
and decryption classes.
"""

if __name__ == "__main__":
    menu: Menu = Menu()
    while True:
        if menu.option == "E":
            encrypt_entry: EncryptEntry = EncryptEntry()

            exit: str = encrypt_entry.exit_mode
            plaintext: str = encrypt_entry.message_to_encrypt

            if plaintext and exit == "C":
                encrypt_handler: EncryptionHandler = \
                    EncryptionHandler(plaintext)
                exit = encrypt_handler.exit_mode
                if exit != "M":
                    break
                else:
                    menu = Menu()
            elif exit == "M":
                menu = Menu()
            else: break
        elif menu.option == "D":
            decrypt_entry: DecryptEntry = DecryptEntry()

            exit: str = decrypt_entry.exit_mode
            key: str = decrypt_entry.decryption_key
            ciphertext: str = decrypt_entry.message_to_decrypt

            if ciphertext and exit == "C":
                decrypt_handler: DecryptionHandler = \
                    DecryptionHandler(key, ciphertext)
                exit = decrypt_handler.exit_mode
                if exit != "M":
                    break
                else:
                    menu = Menu()
            elif exit == "M":
                menu = Menu()
            else: break
        else: break
