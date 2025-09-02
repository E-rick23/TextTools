import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageGrab
import pytesseract
import requests
from io import BytesIO
import pyperclip
import os, sys
import webbrowser

# Detecta o caminho do executável mesmo quando empacotado com PyInstaller
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

tesseract_path = os.path.join(base_path, "Tesseract-OCR", "tesseract.exe")
pytesseract.pytesseract.tesseract_cmd = tesseract_path

def show_about():
    # Cria uma nova janela
    about_win = tk.Toplevel(root)
    about_win.title("Sobre")
    about_win.geometry("350x150")
    
    tk.Label(about_win, text="TextTools (v0.1)", font=("Arial", 14, "bold")).pack(pady=5)
    tk.Label(about_win, text="Programa que converte imagens em texto copiável.\nSuporta arquivos, clipboard e links.", wraplength=330, justify="center").pack(pady=5)
    
    # Link clicável
    def open_github(event):
        webbrowser.open_new("https://github.com/E-rick23/TextTools")  # substitua pelo seu link
    
    tk.Label(about_win, text="Feito por e-rick23(Github)", font=("Arial", 14, "bold")).pack(pady=5)
    link = tk.Label(about_win, text="Repositório do Github!", fg="blue", cursor="hand2")
    link.pack(pady=5)
    link.bind("<Button-1>", open_github)
    
    tk.Button(about_win, text="Fechar", command=about_win.destroy).pack(pady=5)

# Função de OCR
def ocr_from_image(img):
    try:
        text = pytesseract.image_to_string(img, lang='eng+por')  # inglês + português
        return text
    except Exception as e:
        messagebox.showerror("Erro", str(e))
        return ""

# Escolher arquivo de imagem
def choose_file():
    path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp")])
    if path:
        img = Image.open(path)
        text = ocr_from_image(img)
        display_text(text)

# Captura imagem da área de transferência
def from_clipboard():
    img = ImageGrab.grabclipboard()
    if isinstance(img, Image.Image):
        text = ocr_from_image(img)
        display_text(text)
    else:
        messagebox.showerror("Erro", "Não há imagem na área de transferência.")

# Captura imagem de link
def from_url():
    url = url_entry.get()
    if url:
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            text = ocr_from_image(img)
            display_text(text)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir a imagem do link: {e}")

# Exibe o texto e copia para área de transferência
def display_text(text):
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, text)
    pyperclip.copy(text)  # copia automaticamente

# GUI
root = tk.Tk()
root.title("TextTools (v0.1)")

tk.Button(root, text="Escolher Arquivo", command=choose_file).pack(pady=5)
tk.Button(root, text="Imagem da Área de Transferência", command=from_clipboard).pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)
tk.Button(root, text="Abrir Imagem do Link", command=from_url).pack(pady=5)

text_box = tk.Text(root, height=15, width=60)
text_box.pack(pady=5)
tk.Button(root, text="Sobre", command=show_about).pack(pady=5)


root.mainloop()
