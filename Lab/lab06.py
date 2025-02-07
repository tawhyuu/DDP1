def tambah_barang(kode, nama, stok_awal):
    lst_kode = [] # Untuk menyimpan lst kode pada lst_barang
    if len(lst_barang) == 0: # Akan menambahkan barang pertama
        lst_barang.append((kode, nama))
        lst_stok.append(stok_awal)
        print(f'BERHASIL! Barang {kode, nama} berjumlah {stok_awal} berhasil ditambahkan ke dalam storage')
    else:   
        for (kode_barang, nama_barang) in lst_barang: # Looping menambahkan kode ke lst_kode
            lst_kode.append(kode_barang)
        if kode in lst_kode: # Validasi jika list kode sudah terdaftar di sistem
            print(f'GAGAL! Kode barang {kode} sudah ada di dalam sistem.')
        else:
            lst_barang.append((kode, nama))
            lst_stok.append(stok_awal)
            print(f'BERHASIL! Barang {kode, nama} berjumlah {stok_awal} berhasil ditambahkan ke dalam storage')

def kurang_barang(kode, stok):
    lst_kode = []
    if len(lst_barang) == 0: # Akan memvalidasi jika daftar barang di sistem masih kosong
        print('GAGAL! Kode barang tidak di dalam sistem.')
    else:
        for (kode_item, nama) in lst_barang: # looping menambahkan kode ke dalam lst_kode
            lst_kode.append(kode_item)
        if kode in lst_kode: # Memvalidasi kode yang sudah terdaftar
            index = lst_kode.index(kode)
            lst_stok[index] -= stok 
            stock_akhir = lst_stok[index]
            # Tiga kondisi ketika stock_akhir negatif(Tidak mencukupi)/Nol (Habis)/Positif (Tersisa)
            if stock_akhir == 0:
                lst_barang.pop(index)
                print(f'BERHASIL! Barang ID {kode} dihapus dari sistem.')
            elif stock_akhir < 0:
                lst_stok[index] += stok
                print(f'GAGAL! Jumlah barang {kode} tidak cukup.')
            else:
                print(f'BERHASIL! Stok barang ID {kode} tersisa {stock_akhir}.')
                
        else:
            print('GAGAL! Kode barang tidak di dalam sistem.')



# Main Program
lst_barang = []
lst_stok = []
quit = False
while quit != True:
    opsi = input('Masukkan Opsi yang diinginkan (T/K/Q) : ')
    if opsi == 'T':
        kode = input('Kode barang: ')
        nama = input('Nama barang: ')
        stok = int(input('Stok barang: '))
        if stok <= 0: # Validasi agar input harus postif
            print('Stok barang harus Integer positif')
            continue
        tambah_barang(kode, nama, stok)
    elif opsi == 'K':
        kode = input('Kode barang: ')
        jumlah = int(input('Jumlah barang yang ingin dikurangi: '))
        if jumlah <= 0: # Validasi input harus postif
            print('Jumlah harus Integer positif')
            continue
        kurang_barang(kode, jumlah)
    elif opsi == 'Q':
        print('Bye-Bye!')
        quit = True
    else:
        print('Opsi tidak ditemukan')

