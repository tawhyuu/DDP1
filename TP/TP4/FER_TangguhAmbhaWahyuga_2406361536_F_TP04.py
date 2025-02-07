import tkinter as tk
from tkinter import messagebox
import datetime
import random
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO

class Chatbot(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Chatbot sederhana')
        self.master.minsize(500, 500)
        self.history_chat_lst = [] # Menyimpan semua percakapan
        self.msg = tk.StringVar() # Menyimpan str() dari entry
        self.photo = None
        self.dark_theme = False
        self.pack(fill=tk.BOTH, expand=True) # Agar bisa melebar 
        self.create_menu()
        self.create_history_chat()
        self.create_buttons_input()

        # Mengatur grid untuk memperbesar frame saat window diubah ukuran
        self.grid_rowconfigure(0, weight=1)  # Baris untuk chat
        self.grid_columnconfigure(0, weight=1)  # Kolom untuk chat

    def create_menu(self):
        # Membuat container untuk menu
        self.menubar = tk.Menu(self.master)
        self.master['menu'] = self.menubar

        # Membuat menu File
        self.menu1 = tk.Menu(self.menubar, tearoff=0)
        self.menu1.add_command(label= 'Simpan sesi', command=self.save)
        self.menu1.add_command(label= 'Reset sesi', command=self.reset)
        
        self.menu1.add_separator()
        self.menu1.add_command(label= 'Keluar', command=self.quit)
        self.menubar.add_cascade(label= 'File', menu= self.menu1)

        # Membuat menu Tema
        self.menu2 = tk.Menu(self.menubar, tearoff=0)
        self.menu2.add_command(label= ' Ubah tema', command=self.change_theme)
        self.menubar.add_cascade(label= 'Tema', menu=self.menu2)

        # Membuat menu Tentang
        self.menu3 = tk.Menu(self.menubar, tearoff=0)
        self.menu3.add_command(label= 'Tentang Aplikasi', command=self.about)
        self.menubar.add_cascade(label= 'Tentang', menu=self.menu3)

    def save(self):
        # Membuat nama file
        file_output_name = (
            f'chat_session_'
            f'{datetime.datetime.now().strftime("%Y-%m-%d")}'
            f'_{datetime.datetime.now().strftime("%H-%M-%S")}'
            f'.txt'
        )
        
        # Memvalidasi jika tidak ada pesan untuk disimpan
        if len(self.history_chat_lst)-1 == 0:
            messagebox.showinfo('Info', 'Tidak ada sesi untuk disimpan.')
        else:
            with open(file_output_name, 'w', encoding='utf-8') as file_output:
                for chat in self.history_chat_lst:
                    file_output.write(chat)
            messagebox.showinfo('Sukses', 
                                f"Sesi percakapan berhasil disimpan sebagai '{file_output_name}'.")

    def reset(self):
        # Memvalidasi jika hanya terdapat 1 pesan, yaitu pesan welcome chatbot
        if len(self.history_chat_lst)-1 == 0:
            messagebox.showinfo('Info', 'Tidak ada sesi untuk di reset')
        else:
            self.chat['state'] = 'normal'
            self.chat.delete(2.0, tk.END)
            self.chat['state'] = 'disabled'
            self.history_chat_lst = self.history_chat_lst[:1]
            messagebox.showinfo('Reset', 'Sesi telah di reset.')
    
    def quit(self):
        self.master.destroy()

    def change_theme(self):
        if self.dark_theme:
            self.master['bg'] = 'white'
            self.chat_frame['bg']= 'white'
            self.chat['bg'] = 'white'
            self.chat['fg'] = 'black'
            self.question_ent['bg'] = 'white'
            self.question_ent['fg'] = 'black'
            self.dark_theme = False
        else:
            self.master['bg'] = 'black'
            self.chat_frame['bg']='black'
            self.chat['bg'] = 'black'
            self.chat['fg'] = 'white'
            self.question_ent['bg'] = 'black'
            self.question_ent['fg'] = 'white'
            self.dark_theme = True

    def about(self):
        messagebox.showinfo('Tentang Aplikasi', 
                            'Aplikasi Chatbot ini dikembangkan oleh Tangguh-Ambha-Wahyuga dari FASILKOM UI di tahun 2024.\n'
                            'Semoga aplikasi ini dapat menjadi pembelajaran yang bermanfaat, have a great day!')

    def create_history_chat(self):
        # Membuat frame untuk chatbox, scrollbar, dan button
        self.chat_frame = tk.Frame(self, bg='white')
        self.chat_frame.grid(row=0, column=0, sticky='nsew')

        self.chat = tk.Text(self.chat_frame, state='disabled', height=20, width=50)
        self.chat.grid(row=0, column=0, columnspan=7, sticky='nsew', padx=(5,0) , pady=5)

        self.scrollbar = tk.Scrollbar(self.chat_frame, command=self.chat.yview)
        self.scrollbar.grid(row=0, column=7,
                            sticky='ns',
                            pady=5, padx=(0,5))
        
        self.chat.config(yscrollcommand=self.scrollbar.set)
        
        self.insert_msg_to_chat('Chatbot: Halo! ada yang bisa saya bantu?\n')

        # Membuat chatbox dapat melebar
        self.chat_frame.grid_rowconfigure(0, weight=1)

    def insert_msg_to_chat(self, msg):
        # Menampilkan pesan ke history chat
        self.chat['state'] = 'normal' # Mengubah kondisi agar teks dapat diedit/ditambahkan
        self.chat.insert(tk.END, msg)
        self.chat['state'] = 'disabled' # Mengubah kembali ke 'disabled' agar teks tidak dapat diedit
        self.chat.see('end')

        self.history_chat_lst.append(msg)

    def create_buttons_input(self):
        # Mengatur Entry agar bisa melebar
        self.chat_frame.grid_columnconfigure(0, weight=1)

        # Joke Button
        self.joke_btn = tk.Button(self.chat_frame, text='Buat Lelucon', command=self.jokes)
        self.joke_btn.grid(row=1, column=0, 
                           sticky='e', 
                           padx=5, pady=5)

        # Time Button
        self.time_btn = tk.Button(self.chat_frame, text='Tanya Jam', command=self.time)
        self.time_btn.grid(row=1, column=1, 
                           sticky='e', 
                           padx=5, pady=5)

        # Math Button
        self.math_btn = tk.Button(self.chat_frame, text='Soal Matematika', command=self.math_question)
        self.math_btn.grid(row=1, column=2, 
                           sticky='e', 
                           padx=5, pady=5)

        # Donation Button
        self.donation_btn = tk.Button(self.chat_frame, text='Donasi', command=self.donation)
        self.donation_btn.grid(row=1, column=3, 
                          sticky='e', 
                          padx=(5,15), pady=5)

        # User Entry
        self.question_ent = tk.Entry(self.chat_frame, textvariable=self.msg, width=10)
        self.question_ent.grid(row=2, column=0, columnspan=4, 
                               sticky='ew', 
                               padx=(5,15), pady=(5,15))

        # Send Button
        self.send_btn = tk.Button(self.chat_frame, text='Kirim', width=5, command=self.send_msg)
        self.send_btn.grid(row=2, column=5, columnspan=3, 
                           sticky='e', 
                           pady=(5,15), padx=(0,5))

    def send_msg(self):
        # Membuat dictionary untuk chatbot
        self.chatbot_dict = {'buat lelucon': '',
                             'berikan aku soal matematika': '',
                             'tanya jam' : '',
                             'kabarmu' : 'Saya sangat baik dan dalam kondisi prima!.',
                             'halo' : 'Halo! ada yang bisa saya bantu?.',
                             'terimakasih' : 'Sama-sama! Senang bisa membantu Anda.',
                             'terima kasih' : 'Sama-sama! Senang bisa membantu Anda.',
                             'siapa kamu' : 'Saya adalah Chatbot sederhana yang diciptakan untuk Anda.',
                             'bye' : 'Bye-bye!'}
        
        # Mengambil pesan dari entry dan membuat entry kembali kosong
        msg = self.question_ent.get()
        self.question_ent.delete(0,tk.END)
        
        # Memvalidasi jika user tidak mengisi apa-apa di entry
        if msg == '':
            return

        # Menampilkan pesan yang dikirim pada chat
        self.insert_msg_to_chat(f'User: {msg}\n')

        # Cek jika pesan terakhir adalah pertanyaan soal matematika dari chatbot
        for operator in ['+', '-', '*']:
            # Jika pesan terakhir chatbot adalah soal matematika
            if operator in self.history_chat_lst[-2].lower():
                try:
                    if int(msg) == self.math_answer:
                        self.insert_msg_to_chat('Benar! Jawabanmu tepat. 😊\n')

                    elif int(msg) != self.math_answer:
                        self.insert_msg_to_chat(f'Salah, jawaban yang benar adalah {self.math_answer}\n')

                except ValueError:
                    self.insert_msg_to_chat('Masukkan angka yang valid sebagai jawaban.\n')
                return

        # Jika pesan terakhir chatbot bukan soal matematika
        for keyword in self.chatbot_dict.keys():
            if keyword in msg.lower():
                if keyword == 'buat lelucon':
                    self.jokes()
                    return
                elif keyword == 'tanya jam':
                    self.time()
                    return
                elif keyword == 'berikan aku soal matematika':
                    self.math_question()
                    return
                else:
                    self.insert_msg_to_chat(f'Chatbot: {self.chatbot_dict[keyword]}\n')
                    return

        # Jika pesan tidak terdapat di dictionary dan bukan soal matematika
        self.insert_msg_to_chat(f'Chatbot: Maaf, saya belum mengerti pertanyaan itu. Bisa coba yang lain!.\n')

    def jokes(self):
        # Memvalidasi apakah sudah ada perintah buat lelucon pada chat terakhir oleh user
        if 'buat lelucon' not in self.history_chat_lst[-1].lower():
            # Menambahkan User Message pada tampilan chat
            self.insert_msg_to_chat('User: buat lelucon\n')
            
        # Kumpulan Joke
        jokes = [
            'Masak telur selain mata sapi tuh "Sadar" ya?',
            'Kalo perut mules itu tandanya pengen "Break" ya?',
            'Duh kebanyakan garem jadinya "Asing"',
            'Tembok yang gak ada warnanya itu gak di "Chat" ya?',
            'Sekarang hari senin, besok "Selesai"',
            'Kenapa kalau kita olahraga menghapus Kalori? Karena kalau menghapus Memori sulit.',
            'Apa yang harus diperbaiki? Nilai Kalkulus',
            'Kenapa Selai itu enak? Karena kalau Selesai itu gak enak',
        ]

        # Mengacak joke dari kumpulan joke
        joke = random.choice(jokes)

        # Menampilkannya ke chat
        self.insert_msg_to_chat(f'Chatbot: {joke}\n')

    def time(self):
        # Memvalidasi apakah sudah ada perintah 'tanya jam' pada chat terakhir oleh user
        if 'tanya jam' not in self.history_chat_lst[-1].lower():
            # Menambahkan User Message pada tampilan chat
            self.insert_msg_to_chat('User: tanya jam\n')

        self.current_time = datetime.datetime.now().strftime('%H:%M:%S')
        self.insert_msg_to_chat(f'Chatbot: Waktu saat ini adalah {self.current_time}.\n')

    def math_question(self):
        # Mengacak random angka dan operasi
        self.numb1, self.numb2 = random.randint(1, 100), random.randint(1, 100)
        operators = ['+', '-', '*']
        operator = random.choice(operators)

        # Pesan pertanyaan math
        self.math_question_msg = f'Chatbot: Berapa {self.numb1} {operator} {self.numb2}?\n'
        
        # Mencari jawaban dari pertanyaan math
        if '+' in self.math_question_msg:
            self.math_answer = self.numb1 + self.numb2
        if '-' in self.math_question_msg:
            self.math_answer = self.numb1 - self.numb2
        if '*' in self.math_question_msg:
            self.math_answer = self.numb1 * self.numb2

        # Memvalidasi apakah sudah ada perintah buat math question pada chat terakhir oleh user
        if 'beri aku soal matematika' not in self.history_chat_lst[-1].lower():
            # Menambahkan User Message pada tampilan chat
            self.insert_msg_to_chat('User: beri aku soal matematika\n')

        # Menambahkan pertanyaan math pada tampilan chat
        self.insert_msg_to_chat(self.math_question_msg)

    def donation(self):
        # Membuat url yang bisa mengakses filenya
        donation_file_id = '1k6xIracG4SY2pp887DPYFYnHBRB0wlzg'
        url = f'https://drive.google.com/uc?export=view&id={donation_file_id}'

        with urllib.request.urlopen(url) as response:
            # Baca url
            image_data = response.read()
            image = Image.open(BytesIO(image_data))
            image_resized = image.resize((400, 565))

        self.photo = ImageTk.PhotoImage(image_resized)

        donation_window = tk.Toplevel(self)
        donation_window.title('Donasi')
        donation_window.canvas = tk.Canvas(donation_window, bg='black', width=399, height=564)
        donation_window.minsize(398, 563)
        donation_window.maxsize(399, 564)
        donation_window.canvas.pack()
        donation_window.canvas.create_image(0, 0, image = self.photo, anchor='nw')

        def quit_remake():
            messagebox.showinfo('Terimakasih', 'Terimakasih sudah berdonasi. Semoga dilancarkan rezekinya😊🙏.')
            donation_window.destroy()

        donation_window.protocol('WM_DELETE_WINDOW', quit_remake)

chatbot = Chatbot()
chatbot.mainloop()