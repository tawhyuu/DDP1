#Kumpulan list kosong yang nantinya diisi
list_admin = []
list_mahasiswa_terduga = []
list_nama_kasus = []
list_waktu_kasus = []
list_lantai_kasus = []
list_kode_kasus = []
list_tersangka = []
list_persentase = []
lantai_gedbar = ['0', '1', '2', '3', '4', '5', '6', '7']#list lantai di gedung baru

banned = False
logged = False
valid = False


def validasi(isi, list):# Fungsi untuk melihat isi di dalam list
    global valid
    if isi in list:
        valid = True

def validasi_waktu(waktu):# Fungsi untuk memvalidasi format Waktu
    global valid
    if len(waktu) == 5:
        if waktu[:2].isdigit and waktu[2] == ':' and waktu[-2:].isdigit and int(waktu[:2])< 24 and int(waktu[-2:]) < 60:
            valid = True

def check_ban(percobaan):# Fungsi untuk melakukan check percobaan login dan banning
    global banned
    if percobaan == 3:
        print('Maaf, Anda telah gagal login 3 kali. Silakan keluar.\n')
        banned = True


def login():#Fungsi login
    global banned, logged, valid, admin
    percobaan_login = 0
    berhasil_login = False  
    while percobaan_login < 3 and not berhasil_login: #Looping meminta login
        valid = False #Mengembalikan nilai valid menjadi False
        npm_login = input('Masukkan NPM mahasiswa admin yang telah terdaftar: ')
        percobaan_login += 1
        validasi(npm_login, list_admin)

        if valid == True:
            print(f'Selamat datang, mahasiswa dengan NPM {npm_login}!\n')

            indeks_admin = list_admin.index(npm_login)
            admin = list_admin[indeks_admin]
            logged = True
            berhasil_login = True
        else:
            print(f'Maaf, mahasiswa dengan NPM {npm_login} tidak terdaftar pada sistem.')
            check_ban(percobaan_login)
        
            

def wewenang(logged: bool, banned: bool) -> bool:# wewenang untuk akses menu
    if banned == True:  # untuk cek user dalam kondisi ban atau tidak
        print("Maaf, Anda telah gagal login 3 kali. Silakan keluar.\n")
        return False
    if logged == False:  # untuk cek user sudah login atau belum
        print("Silakan untuk login terlebih dahulu.\n")
        return False
    return True  # nilai True jika logged True and Banned False

def execute_logcheck():# fungsi pilihan menu 2
    indeks_call = 0

    print("{:>4} | {:^10} | {:^7} | {:<15}".format("Kode", "Nama", "Waktu", "Lokasi (lantai)"))
    for nama_kasus in range(len(list_nama_kasus)):
        print("{:>4} | {:<10} | {:^7} | {:<15}".format(list_kode_kasus[indeks_call], list_nama_kasus[indeks_call],list_waktu_kasus[indeks_call],list_lantai_kasus[indeks_call]))
        indeks_call += 1
    print()


def kemungkinan_tersangka():#fungsi pilihan 3
    global valid
    while True:
        valid = False #Untuk mengembalikan nilai valid menjadi False
        kode = input("Masukan kode mahasiswa tersangka: ")
        validasi(kode, list_kode_kasus)
        if valid == True:
            break
        else:
            print(f'Maaf, mahasiswa dengan kode {kode} tidak terdaftar pada sistem.')
    
    while True:
        valid = False #Untuk mengembalikan nilai valid menjadi False
        waktu = input("Masukan dugaan waktu kejadian: ")
        validasi_waktu(waktu)
        if valid == True:
            break
        else:
            print('Maaf, format waktu tidak sesuai.')
        
    while True: 
        valid = False #Untuk mengembalikan nilai valid menjadi False       
        lantai = input('Masukan dugaan lokasi (lantai) kejadian: ')
        validasi(lantai,lantai_gedbar)
        if valid == True:
            break
        else:
            print(f"Maaf, lantai {lantai} tidak tersedia.")
            continue
    
    num_code = int(kode[-2:])
    num_time = int(waktu[:2]) * 60 + int(waktu[-2:])
    num_level = int(lantai)
    if num_code == 3:
        mux_code = 15
    else:
        mux_code = 10
    
    #Tersangka acuan : Tesangka ke-4, Waktu 14:31, dan di lantai 2
    persentase = max((mux_code + (45 - abs(871 - num_time)) + (40 - abs(2 - num_level)*5)),0)
    list_tersangka.append(list_mahasiswa_terduga[num_code])
    list_persentase.append(persentase)
            
    nama_call = list_mahasiswa_terduga[int(kode[-2:])]# memanggil nama dengan kode
    print(f'Berhasil meninjau tersangka pada mahasiswa dengan nama {nama_call} pada pukul {waktu} di lantai {lantai}.')
    print()

def hasil_tinjau():#fungsi pilihan menu 4
    tersangka = None
    if len(list_persentase) == 0:
        tersangka = "Tidak ada"
    else:
        print("{:>6} | {:^10} | {:<25}".format("Dugaan", "Nama", "Persentase Menjadi Pelaku"))
        for i_tersangka in range(len(list_tersangka)):
            print("{:>6} | {:^10} | {:<25}".format(i_tersangka+1, list_tersangka[i_tersangka], str(list_persentase[i_tersangka])+'%'))
            if sum(list_persentase) // len(list_persentase) >= 40:
                indeks_tersangka = list_persentase.index(max(list_persentase))# menetapkan indeks tersangka dengan presentasi yang paling besar
                tersangka = list_tersangka[indeks_tersangka]
            else:
                tersangka = admin + ' (admin)'
    print (f'Nama/NPM mahasiswa tersangka yang paling mungkin: {tersangka}\n')



def tanya_admin():#Fungsi untuk menanyakan admin
    jumlah_admin = int(input(f'Masukkan banyaknya mahasiswa admin: '))
    for x in range(jumlah_admin):#looping untuk npm admin
        npm_admin = input(f'NPM mahasiswa admin ke-{x+1}: ')
        list_admin.append(npm_admin)

def tanya_terduga():#fungsi untuk menanyakan jumlah dan nama mahasiswa yang terduga 
    jumlah_terduga = int(input('\nMasukan banyaknya mahasiswa tersangka: '))
    for a in range(jumlah_terduga):#looping untuk nama mahasiswa
        nama_terduga = input(f'Nama mahasiswa tersangka ke-{a+1}: ')
        list_mahasiswa_terduga.append(nama_terduga)

def tanya_kasus():#fungsi untuk menanyakan kasusnya
    global indeks_nama, valid
    jumlah_kasus = int(input('\nMasukkan banyaknya data yang terekam CCTV: '))
    for b in range(jumlah_kasus):#looping untuk menanyakan kasus
        print(f'{"="*10} ke-{b+1} {"="*10}')

        while True:# Looping kasus nama tersangka
            valid = False # untuk mengembalikan nilai valid menjadi False
            nama_kasus = input('Nama mahasiswa: ')
            validasi(nama_kasus, list_mahasiswa_terduga)
            if valid:
                list_nama_kasus.append(nama_kasus)
                break
            else:
                print(f'Maaf, {nama_kasus} tidak terdaftar pada mahasiswa tersangka.')
        
        while True:# looping waktu kasus tersangka
            valid = False # untuk mengembalikan nilai valid menjadi False
            waktu_kasus = input('Waktu terdeteksi (HH:MM): ')
            validasi_waktu(waktu_kasus)
            if valid:
                list_waktu_kasus.append(waktu_kasus)
                break
            else:
                print('Maaf, format waktu tidak sesuai.')

        while True:# looping lantai kasus tersangka
            valid = False
            lantai_kasus = input('Lantai tempat terdeteksi (0-7): ')
            validasi(lantai_kasus, lantai_gedbar)
            if valid:
                list_lantai_kasus.append(lantai_kasus)
                break
            else:
                print(f"Maaf, lantai {lantai_kasus} tidak tersedia.")

        #Kode nama tersangka
        indeks_nama = 0
        for nama_in_kasus in list_mahasiswa_terduga:
            if nama_kasus in list_mahasiswa_terduga: #untuk mengecek jika Nama terdapat pada list
                indeks_nama = list_mahasiswa_terduga.index(nama_kasus)
        kode_nama = lantai_kasus + "{:02d}".format(indeks_nama)
        list_kode_kasus.append(kode_nama)
    print()

def tampilan_utama():
    print("="*20 + " Selamat datang di PacilSeeker! " + "="*20 + "\n"
    "(1) Masuk\n"
    "(2) Lihat riwayat CCTV\n"
    "(3) Tinjau kemungkinan tersangka\n"
    "(4) Cetak ringkasan tersangka\n"
    "(5) Keluar")

tanya_admin()
tanya_terduga()
tanya_kasus()

while True:
    tampilan_utama()
    pilihan = int(input("Masukan pilihan menu: "))
    print("="*72)
    
    if pilihan == 1:
        if banned == True:
            print("Maaf, Anda telah gagal login 3 kali. Silakan keluar.\n")
            continue

        login()
    
    elif pilihan == 2:
        if wewenang(logged, banned) == False:
            continue
        execute_logcheck()

    elif pilihan == 3:
        if wewenang(logged, banned) == False:
            continue
        kemungkinan_tersangka()

    elif pilihan == 4:
        if wewenang(logged, banned) == False:
            continue
        hasil_tinjau()
    
    elif pilihan == 5:
        print("Terima kasih telah menggunakan PacilSeeker!")
        break
    
    else:
        print('Maaf, pilihan menu Anda tidak diketahui.\n')