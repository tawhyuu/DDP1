import tkinter as tk

class Chatbot(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Chatbot sederhana')
        # self.master.geometry('600x600')
        self.pack()
        self.create_menu()
        self.create_history_chat()
        # self.create_buttons_input()

    def create_menu(self):
        # Membuat container untuk menu
        self.menubar = tk.Menu(self.master)
        self.master['menu'] = self.menubar

        # Membuat menu 1
        self.menu1 = tk.Menu(self.menubar, tearoff=0)
        self.menu1.add_command(label= 'Simpan sesi')
        self.menu1.add_command(label= 'Reset sesi')
        
        self.menu1.add_separator()
        self.menu1.add_command(label= 'Keluar', command=self.quit)
        self.menubar.add_cascade(label= 'File', menu= self.menu1)

        # Membuat menu 2
        self.menu2 = tk.Menu(self.menubar, tearoff=0)
        self.menu2.add_command(label= ' Ubah tema', command=self.change_theme)
        self.menubar.add_cascade(label= 'Tema', menu=self.menu2)

        # Membuat menu 3
        self.menu3 = tk.Menu(self.menubar, tearoff=0)
        self.menu3.add_command(label= 'Tentang Aplikasi')
        self.menubar.add_cascade(label= 'Tentang', menu=self.menu3)

    def create_history_chat(self):
        # Membuat container/frame untuk history chat
        # self.history_chat = tk.LabelFrame(self, borderwidth=0, bg='black', fg='white') # Biar gak keliatan dia di dalem frame
        # self.history_chat.pack(padx= 10, pady= 10, expand=True, fill=tk.BOTH)
        
        # Membuat tampilan teks pada history_chat dengan scrollbar
        # self.chat = tk.Text(self.history_chat, state='disabled', height=20, width=50, bg='black', fg='white')
        # self.chat.pack(side=tk.LEFT)
        self.chat = tk.Text(self, state='disabled', height=20, width=50)
        self.chat.pack(padx=5, pady=5)
        # self.chat.grid(row=0, column=0, columnspan=7, pady=5)

        # self.scrollbar = tk.Scrollbar(self.history_chat, command=self.chat.yview)
        # self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # self.chat.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar = tk.Scrollbar(self, command=self.chat.yview)
        self.scrollbar.pack()
        # self.scrollbar.grid(row=0, column=7)
        self.chat.config(yscrollcommand=self.scrollbar.set)

        # Membuat Button
        self.welcome_msg()

    # def create_buttons_input(self):
    #     # Membuat frame untuk input dan button
    #     # self.input_frame = tk.LabelFrame(self, borderwidth=0)
    #     # self.input_frame.pack(fill=tk.X, side=tk.RIGHT)

    #     # Joke Button
    #     # self.joke_btn = tk.Button(self.input_frame, text='Buat Lelucon')
    #     # self.joke_btn.grid(row=0, column=0, sticky='e', padx=5, pady=5)
    #     self.joke_btn = tk.Button(self, text='Buat Lelucon')
    #     self.joke_btn.grid(row=1, column=0, sticky='e', padx=5, pady=5)

    #     # Time Button
    #     # self.time_btn = tk.Button(self.input_frame, text='Tanya Jam')
    #     # self.time_btn.grid(row=0, column=1, sticky='e', padx=5, pady=5)
    #     self.time_btn = tk.Button(self, text='Tanya Jam')
    #     self.time_btn.grid(row=1, column=1, sticky='e', padx=5, pady=5)

    #     # Math Button
    #     # self.math_btn = tk.Button(self.input_frame, text='Soal Matematika')
    #     # self.math_btn.grid(row=0, column=2, sticky='e', padx=5, pady=5)
    #     self.math_btn = tk.Button(self, text='Soal Matematika')
    #     self.math_btn.grid(row=1, column=2, sticky='e', padx=5, pady=5)

    #     # XYZ Button
    #     # self.xyz_btn = tk.Button(self.input_frame, text='XYZ')
    #     # self.xyz_btn.grid(row=0, column=3, sticky='e', padx=5, pady=5)
    #     self.xyz_btn = tk.Button(self, text='XYZ')
    #     self.xyz_btn.grid(row=1, column=3, sticky='e', padx=5, pady=5)

    #     # User Entry
    #     # self.question_ent = tk.Entry(self.input_frame, width=10) # Masih gatau gimana cara ngebuat dia seusai sama frame
    #     # self.question_ent.grid(row=1, column=0, columnspan=4, sticky='we', padx=5, pady=5)
    #     self.question_ent = tk.Entry(self, width=10) # Masih gatau gimana cara ngebuat dia seusai sama frame
    #     self.question_ent.grid(row=2, column=0, columnspan=4, sticky='we', padx=5, pady=5)

    #     # Send Button
    #     # self.send_btn = tk.Button(self.input_frame, text='Kirim', width=5)
    #     # self.send_btn.grid(row=1, column=4, sticky='e', padx=10, pady=5)
    #     self.send_btn = tk.Button(self, text='Kirim', width=5)
    #     self.send_btn.grid(row=2, column=5, columnspan=3, sticky='e', pady=5)
        
    def welcome_msg(self):
        # Menampilkan pesan welcome di frame historychat
        self.chat.config(state='normal') # Mengubah kondisi agar teks dapat diedit/ditambahkan
        self.chat.insert(tk.END, 'Chatbot: Halo! ada yang bisa saya bantu?')
        self.chat.config(state='disabled') # Mengubah kembali ke 'disabled' agar teks tidak dapat diedit

        pass
    def save(self):
        pass

    def reset(self):
        pass
    
    def change_theme(self):
        self.master.config(bg='black')
        self.chat.config(bg='black', fg='white')
        # self.joke_btn.config(bg='black', fg='white')
        # self.question_ent.config(bg='black', fg='white')

    def quit(self):
        self.master.destroy()

chatbot = Chatbot()
chatbot.mainloop()
