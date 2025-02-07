import tkinter as tk
from tkinter import messagebox

class GanjilGenapApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Cek Angka Ganjil Genap")
        self.master.geometry("300x150")
        
        # Membuat IntVar untuk binding
        self.angka = tk.IntVar()
        
        # Membangun interface
        self.create_widgets()
        
    def create_widgets(self):
        # Label
        self.label = tk.Label(
            self.master, 
            text="Masukkan sebuah angka:", 
            font=("Arial", 12)
        )
        self.label.pack(pady=10)
        
        # Membuat validasi untuk input
        # def validate_input(new_value):
        #     if new_value == "":  # Mengizinkan field kosong
        #         return True
        #     try:
        #         int(new_value)
        #         return True
        #     except ValueError:
        #         return False
        
        # vcmd = (self.master.register(validate_input), '%P')
        
        # Entry dengan IntVar binding
        self.entry = tk.Entry(
            self.master,
            textvariable=self.angka,
            font=("Arial", 12),
            # validate='key'
            # validatecommand=vcmd
        )
        self.entry.pack(pady=5)
        
        # Tombol cek
        self.tombol_cek = tk.Button(
            self.master,
            text="Cek Ganjil/Genap",
            command=self.cek_ganjil_genap,
            font=("Arial", 11)
        )
        self.tombol_cek.pack(pady=10)
        
    def cek_ganjil_genap(self):
        try:
            angka = self.angka.get()
            if angka % 2 == 0:
                messagebox.showinfo("Hasil", f"Angka {angka} adalah GENAP")
            else:
                messagebox.showinfo("Hasil", f"Angka {angka} adalah GANJIL")
        except tk.TclError:  # Error yang muncul jika IntVar kosong
            messagebox.showerror("Error", "Mohon masukkan angka yang valid!")

# Membuat dan menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = GanjilGenapApp(root)
    app.pack()
    root.mainloop()