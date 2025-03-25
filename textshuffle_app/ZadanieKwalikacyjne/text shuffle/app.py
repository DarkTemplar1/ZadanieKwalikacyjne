import time
import subprocess
import requests
import tkinter as tk
from tkinter import filedialog

server_process = subprocess.Popen(["python", "manage.py", "runserver"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

time.sleep(2)

def process_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    try:
        response = requests.post("http://127.0.0.1:8000/process/", data={'text': text})
        if response.status_code == 200:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, response.json().get('processed_text', 'Błąd przetwarzania'))
        else:
            result_text.insert(tk.END, "Błąd podczas przetwarzania")
    except requests.exceptions.ConnectionError:
        result_text.insert(tk.END, "Nie można połączyć się z serwerem")

root = tk.Tk()
root.title("Aplikacja Przetwarzania Tekstu")

btn = tk.Button(root, text="Wybierz plik", command=process_file)
btn.pack(pady=10)

result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

def on_close():
    server_process.terminate()  # Zatrzymaj serwer Django
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
