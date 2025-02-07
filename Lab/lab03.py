kucing_itb = 'Puss-2-British Shorthair-Orange-Scar-5-Sphynx-White-Jelly-1-American Wirehair-Grey-Yawhi-3-Siamese-White-Mi-3-Munchkin-Ora​nge-Anak-2-Angora-Black-Rav-6-Angora-Brown'

kucing_ui = 'Leon-2-Somali-Grey,Sa-2-American Curl-White,Panda-4-Exotic Shorthair-Black,Lala-3-LaPerm-Black,Ninya-2-Somali-Beige,Vae-1-LaPerm-Grey,Rinny-4-Highlander-Grey​'

print("""Selamat datang di DepeCat!
Berikut list universitas yang menyediakan adopsi kucing:
1) UI
2) ITB """)

action = input('Masukkan pilihan sesuai angka yang tertera di depan nama universitas: ')
if action == "1":
    data_kucing = kucing_ui
elif action == "2":
    data_kucing = kucing_itb
else:
    print("Input tidak valid.")

print("""\nSilahkan pilih menu
1) Cetak semua data kucing
2) Cari kucing""")

pilihan = input("Pilihan: ")
if pilihan == "1":
    print("{:<9} | {:<4} | {:<18} | {:<8} ".format("Nama", "Umur", "Jenis", "Warna"))
    print("{}|{}|{}|{}".format("-"*10, "-"*6, "-"*20, "-"*10))
    list_data_kucing = data_kucing.split(",")
    for i in range(len(list_data_kucing)):
        kucing = list_data_kucing[i]
        list_kucing = kucing.split("-")
        print("{:<9} | {:<4} | {:<18} | {:<8    }".format(list_kucing[0], list_kucing[1], list_kucing[2], list_kucing[3]))
    print("Terima kasih telah menggunakan DepeCat!")

elif pilihan == "2":
    key_word = input("Masukan kata kunci: ")
    key_word = key_word.lower()
    data_kucing_lower = data_kucing.lower()
    index_koma = data_kucing.find(",")
    kucing1 = data_kucing[0:index_koma]
    kucing2 = data_kucing[index_koma+1:data_kucing.find(",",data_kucing.find(",")+1)]
    
        

    