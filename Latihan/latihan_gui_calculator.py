import tkinter as tk
from tkinter import ttk, messagebox

class CatInventory(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Pengaturan window utama
        self.title("Cat Inventory")
        self.geometry("400x500")
        
        # Inisialisasi untuk menyimpan data kucing
        self.nama_kucing = tk.StringVar()
        self.umur_kucing = tk.StringVar()
        self.ras_kucing = tk.StringVar()
        self.warna_kucing = tk.StringVar()

        self.setup_gui()
        
    def setup_gui(self):
        # Frame untuk input
        self.input_frame = ttk.LabelFrame(self)
        self.input_frame.pack()
        
        # Entry untuk nama kucing
        ttk.Label(self.input_frame, text="Name:").grid(row=0, column=0)
        self.nama_entry = ttk.Entry(self.input_frame, textvariable=self.nama_kucing, width=30)
        self.nama_entry.grid(row=1, column=0)
        
        # Entry untuk umur kucing
        ttk.Label(self.input_frame, text="Age:").grid(row=2, column=0)
        self.age_entry = ttk.Entry(self.input_frame, textvariable=self.umur_kucing, width=30)
        self.age_entry.grid(row=3, column=0)

        # Entry untuk ras kucing
        ttk.Label(self.input_frame, text="Breed:").grid(row=4, column=0)
        self.breed_entry = ttk.Entry(self.input_frame, textvariable=self.ras_kucing,width=30)
        self.breed_entry.grid(row=5, column=0)

        # Entry untuk warna kucing
        ttk.Label(self.input_frame, text="Color:").grid(row=6, column=0)
        self.color_entry = ttk.Entry(self.input_frame, textvariable=self.warna_kucing, width=30)
        self.color_entry.grid(row=7, column=0)

        # Tombol add cat
        self.add_button = ttk.Button(self.input_frame, text="Add Cat", 
                                   command=self.add_cat)
        self.add_button.grid(row=8, column=0)
        
        # Membuat tableframe untuk menampilkan data kucing
        self.table_frame = ttk.LabelFrame(self)
        self.table_frame.pack(fill="both", expand=True)
        
        # untuk menampilkan data kucing
        self.tree = ttk.Treeview(self.table_frame, 
                                columns=("Name", "Age", "Breed", "Color"),
                                show="headings")
        
        # Mengatur kolom
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Breed", text="Breed")
        self.tree.heading("Color", text="Color")
        
        self.tree.column("Name", width=100)
        self.tree.column("Age", width=100)
        self.tree.column("Breed", width=100)
        self.tree.column("Color", width=100)
        
        # Pack komponen
        self.tree.pack(side="left", fill="both", expand=True)
        
        # Frame untuk tombol aksi
        self.action_frame = ttk.Frame(self)
        self.action_frame.pack()
        
    def add_cat(self):
        nama = self.nama_entry.get()
        umur = self.age_entry.get()
        ras = self.breed_entry.get()
        warna = self.color_entry.get()
        
        # Validasi Input
        if not nama or not umur or not ras or not warna:
            messagebox.showwarning("Peringatan", "Please fill all fields.")
            return
        
        # Validasi umur kucing adalah integer
        if type(umur) != int:
            messagebox.showwarning("Input Error", "Age must be integer")
        
        self.tree.insert("", "end", values=(nama, umur, ras, warna))
        
        # Reset input
        self.nama_entry.delete(0, "end")
        self.age_entry.delete(0, 'end')
        self.breed_entry.delete(0, 'end')
        self.color_entry.delete(0, 'end')

if __name__ == "__main__":
    app = CatInventory()
    app.mainloop()