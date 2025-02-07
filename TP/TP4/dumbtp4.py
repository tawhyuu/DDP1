import tkinter as tk
from tkinter import messagebox, Menu
import random
import datetime

class Chatbot(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.chat_history = []
        self.dark_mode = False

    def create_widgets(self):
        # Create menu
        menubar = Menu(self.master)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Simpan Sesi", command=self.save_session)
        file_menu.add_command(label="Reset Sesi", command=self.reset_session)
        file_menu.add_separator()
        file_menu.add_command(label="Keluar", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        theme_menu = Menu(menubar, tearoff=0)
        theme_menu.add_command(label="Ubah Tema", command=self.change_theme)
        menubar.add_cascade(label="Tema", menu=theme_menu)

        about_menu = Menu(menubar, tearoff=0)
        about_menu.add_command(label="Tentang Aplikasi", command=self.show_about)
        menubar.add_cascade(label="Tentang", menu=about_menu)

        self.master.config(menu=menubar)

        # Create chat area with scrollbar
        self.chat_frame = tk.LabelFrame(self, text="Percakapan", padx=10, pady=10)
        self.chat_frame.pack(padx=10, pady=10)

        self.chat_area = tk.Text(self.chat_frame, width=50, height=20)
        self.chat_area.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.chat_frame, command=self.chat_area.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_area.config(yscrollcommand=self.scrollbar.set)

        self.input_text = tk.Entry(self, width=40)
        self.input_text.pack(pady=5)

        self.send_button = tk.Button(self, text="Kirim", command=self.send_message)
        self.send_button.pack(pady=5)

        # Grid layout for buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=5)

        self.joke_button = tk.Button(button_frame, text="Buat Lelucon", command=self.send_joke)
        self.joke_button.grid(row=0, column=0, padx=5)

        self.time_button = tk.Button(button_frame, text="Tanya Jam", command=self.send_time)
        self.time_button.grid(row=0, column=1, padx=5)

        self.math_button = tk.Button(button_frame, text="Soal Matematika", command=self.send_math_question)
        self.math_button.grid(row=0, column=2, padx=5)

        self.xyz_button = tk.Button(button_frame, text="XYZ", command=self.send_xyz)
        self.xyz_button.grid(row=0, column=3, padx=5)

        self.quit_button = tk.Button(self, text="Keluar", command=self.master.quit)
        self.quit_button.pack(pady=5)

        self.display_welcome_message()

    def display_welcome_message(self):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, "Chatbot: Halo! Ada yang bisa saya bantu?\n")
        self.chat_area.config(state='disabled')

    def send_message(self):
        user_message = self.input_text.get()
        if user_message:
            self.chat_area.config(state='normal')
            self.chat_area.insert(tk.END, f":User  {user_message}\n")
            self.chat_area.config(state='disabled')
            self.chat_history.append(f":User  {user_message}")
            self.input_text.delete(0, tk.END)
            self.respond(user_message)

    def respond(self, message):
        # Simple keyword-based responses
        if "hai" in message.lower() or "halo" in message.lower():
            response = "Chatbot: Hai! Bagaimana kabar Anda?\n"
        elif "apa kabar" in message.lower():
            response = "Chatbot: Saya baik-baik saja, terima kasih! Bagaimana dengan Anda?\n"
        else:
            response = "Chatbot: Maaf, saya tidak mengerti.\n"

        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, response)
        self.chat_area.config(state='disabled')
        self.chat_history.append(response.strip())

    def send_joke(self):
        jokes = [
            "Kenapa buku pelajaran sedih? Karena dia punya banyak masalah! 📖",
            "Kenapa komputer tidak bisa menari? Karena mereka punya terlalu banyak byte!",
            "Mengapa matematika selalu sedih? Karena dia punya banyak masalah!"
        ]
        joke = random.choice(jokes)
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"Chatbot: {joke}\n")
        self.chat_area.config(state='disabled')
        self.chat_history.append(f"Chatbot: {joke}")

    def send_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"Chatbot: Waktu saat ini adalah {current_time}\n")
        self.chat_area.config(state='disabled')
        self.chat_history.append(f"Chatbot: Waktu saat ini adalah {current_time}")

    def send_math_question(self):
        a, b = random.randint(1, 10), random.randint(1, 10)
        self.current_answer = a + b
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"Chatbot: Berapa {a} + {b}?\n")
        self.chat_area.config(state='disabled')
        self.chat_history.append(f"Chatbot: Berapa {a} + {b}?")

    def send_xyz(self):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, "Chatbot: Tombol ini belum dikonfigurasi, silakan coba fitur lain!\n")
        self.chat_area.config(state='disabled')
        self.chat_history.append("Chatbot: Tombol ini belum dikonfigurasi, silakan coba fitur lain!")

    def save_session(self):
        # Implement saving chat history to a file
        if not self.chat_history:
            messagebox.showinfo("Info", "Tidak ada percakapan untuk disimpan.")
            return
        filename = f"chat_session_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        with open(filename, 'w') as f:
            for line in self.chat_history:
                f.write(line + "\n")
        messagebox.showinfo("Info", f"Sesi percakapan disimpan sebagai {filename}.")

    def reset_session(self):
        self.chat_area.config(state='normal')
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state='disabled')
        self.chat_history.clear()
        self.display_welcome_message()

    def change_theme(self):
        if self.dark_mode:
            self.master.config(bg='white')
            self.chat_area.config(bg='white', fg='black')
            self.input_text.config(bg='white', fg='black')
            self.send_button.config(bg='lightgray', fg='black')
            self.dark_mode = False
        else:
            self.master.config(bg='black')
            self.chat_area.config(bg='black', fg='white')
            self.input_text.config(bg='black', fg='white')
            self.send_button.config(bg='gray', fg='white')
            self.dark_mode = True

    def show_about(self):
        messagebox.showinfo("Tentang Aplikasi", "Chatbot sederhana menggunakan tkinter.\nPengembang: NAMA-PENGEMBANG")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chatbot GUI")
    app = Chatbot(master=root)
    app.mainloop()