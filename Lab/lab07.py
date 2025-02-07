def main_menu():
    print('Selamat datang di PMB Friend!\nBerikut adalah menu yang dapat kamu pilih:\n'
          '1) Tambah user\n' 
          '2) Tambah pertemanan\n'
          '3) Cari teman mutual\n' 
          '4) Sarankan pertemana\n'
          '5) Keluar')

network = {}
def add_user(network, user): 
    if user not in network: 
        network[user] = set() 
        print(f"{user} berhasil ditambahkan sebagai user.") 
    else: print(f"User {user} sudah terdaftar!")

def add_friend(network, user1, user2):
    if user1 not in network.keys() or user2 not in network.keys():
        print(f'User {user1} atau {user2} tidak terdaftar!')
    else:
        network[user1].add(user2) # menambahkan teman di user1
        network[user2].add(user1) # menambahkan teman di user2
        print(f'Pertemanan {user1} dan {user2} berhasil ditambahkan')

def mutual_friends(network, user1, user2):
    if user1 not in network.keys() or user2 not in network.keys():
        print(f'User {user1} atau {user2} tidak terdaftar!')
    else:
        mutual = network[user1].intersection(network[user2]) # himpunan teman yang sama antara user1 dan user2
        if len(mutual) == 0: #Jika tidak ada teman yang sama
            print(f'Tidak ada teman mutual antara {user1} dan {user2}.')
        else:
            print(f'Teman mutual dari {user1} dan {user2}: {mutual}')

def suggest_friend(network, user):
    seluruh_user = set(network.keys())
    suggest_set = seluruh_user - network[user] - {user} # Seluruh user - Teman user - User sendiri
    if user not in network.keys():
        print(f'User {user} tidak terdaftar!')
    else:
        if len(suggest_set) == 0:
            print(f'Tidak ada teman yang dapat disarankan untuk {user} :(')
        else:
            print(f'Teman yang disarankan untuk {user}: {suggest_set}')

# Main Program
main_menu()
quit = False
while quit != True:
    pilihan = input('Masukan menu yang diinginkan (1-5): ')
    if pilihan == '1':
        nama_user = input('Masukkan nama user yang ingin ditambahkan: ')
        add_user(network, nama_user)
        print()
    elif pilihan == '2':
        user1 = input('Masukkan nama user pertama: ')
        user2 = input('Masukkan nama user kedua: ')
        add_friend(network, user1, user2)
        print()
    elif pilihan == '3':
        user_1 = input('Nama user pertama: ')
        user_2 = input('Nama user kedua: ')
        mutual_friends(network, user_1, user_2)
        print()
    elif pilihan == '4':
        user = input('Nama user yang ingin disarankan pertemanannya: ')
        suggest_friend(network, user)
        print()
    elif pilihan == '5':
        print('Terima kasih telah berkunjung ke PMB Friend!')
        quit = True
