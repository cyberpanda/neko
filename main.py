import tkinter as tk
import os

from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from cryptography.fernet import Fernet

title = 'Neko File Encrypt'
white = "#fff"
black = "#000"
green = "#ccfcc0"

# Ideas for later use
# load_animation = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
# button_or_label.set(f'waiting [{"..."}]') # TODO: add animation
# button_or_label.set('Arigato gozaimasu!')


def encrypt_file():
    file = askopenfile(parent=root, mode='rb', title="Select file",filetypes=(("", "*.*"), ("all files", "*.*")))
    if file:
        key = Fernet.generate_key()
        with open("neko.key", "wb") as key_file:
            key_file.write(key)
        # encrypt file with key
        with open(file.name, "rb") as file_to_encrypt:
            contents = file_to_encrypt.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        # write encrypted file
        with open(f"{file.name}.meow", "wb") as encrypted_file:
            encrypted_file.write(contents_encrypted)
            os.remove(file.name)


def decrypt_file():
    file = askopenfile(parent=root, mode='rb', title="Select file",
                       filetypes=(("", "*.meow"), ("all files", "*.*")))
    if file:
        key = Fernet.generate_key()
        with open("neko.key", "rb") as key_file:
            key = key_file.read()
        # decrypt file with key
        with open(file.name, "rb") as file_to_decrypt:
            contents = file_to_decrypt.read()
        contents_decrypted = Fernet(key).decrypt(contents)
        # write decrypted file
        with open(f"{file.name[:-5]}", "wb") as decrypted_file:
            decrypted_file.write(contents_decrypted)
            os.remove(file.name)


# main window
root = tk.Tk()
root.title(title)
canvas = tk.Canvas(root, width=400, height=600)
canvas.grid(columnspan=3, rowspan=3)


# logo
open_logo = Image.open('logo.png')
#resized_logo = open_logo.resize((300, 105))
convert_to_compatible_image = ImageTk.PhotoImage(open_logo)
logo_label = tk.Label(image=convert_to_compatible_image)
logo_label.grid(column=1, row=0)

# some text
instructions = tk.Label(
    root, text='Select a file to encrypt/decrypt', font='Arial')
instructions.grid(columnspan=3, column=0, row=1)


# encrypt btn
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, font='Arial',
                       height=2, width=15, border=0, bg=green, command=lambda: encrypt_file())
browse_text.set('Encrypt')
browse_btn.grid(column=1, row=2)

# decrypt btn
decrypt_text = tk.StringVar()
decrypt_btn = tk.Button(root, textvariable=decrypt_text, font='Arial',
                        height=2, width=15, border=0, bg=green, command=lambda: decrypt_file())
decrypt_text.set('Decrypt')
decrypt_btn.grid(column=1, row=3, pady=10)


if __name__ == '__main__':
    root.mainloop()
