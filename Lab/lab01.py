print('''>>==============================================<<
||                     $$$$                     ||
||               WELCOME TO UIMart              ||
||                 Receipt Printer              ||
||                     $$$$                     ||
>>==============================================<<''')
print()
# untuk meminta user menginput data barang yang dibeli.
nama_produk = input('Masukkan nama produk: ')
jumlah_produk = int(input('Jumlah produk: '))
harga_produk = int(input('Masukkan harga produk: '))
presentase_diskon = int(input('Masukkan diskon (dalam presentase 1-100): '))
tanggal_kadaluwarsa = input('Kapan tanggal expirednya?: ')
bulan_kadaluwarsa = input('Kapan bulan expirednya?: ')
nama_bank = input('Masukkan nama bank: ')
nominal_saldo_awal = int(input('Masukkan saldo awal: '))

kode_serial = nama_produk + tanggal_kadaluwarsa + bulan_kadaluwarsa + str(jumlah_produk) + nama_bank
kode_serial_upper = kode_serial.upper()

#Menghitung minggu dan hari sampai tanggal kadaluwarsa
# asumsi 1 bulan 30 hari dan pembelian 1 September dan tahun kadaluwarsa sama dengan tahun pembelian
selisih_bulan_kadaluwarsa = int(bulan_kadaluwarsa)-9 # 9 ini september
total_hari_kadaluwarsa = (30*selisih_bulan_kadaluwarsa + int(tanggal_kadaluwarsa))-1 # -1 karena dianggap membeli pada 1 september
minggu_kadaluwarsa = total_hari_kadaluwarsa // 7
hari_kadaluwarsa = total_hari_kadaluwarsa % 7

# menghitung total belanja dan saldo akhir buyer
total_belanja = harga_produk*jumlah_produk*(1 - presentase_diskon/100) #Total harga produk dikali (presentasi setelah diskon)
saldo_akhir = nominal_saldo_awal - (total_belanja)
saldo_akhir = float(saldo_akhir)

print()
print('''>>==============================================<<
||                     UIMart                   ||
>>==============================================<<''')
print()
# mencetak serial code dan ringkasan barang yang di beli buyer.
print('Serial Code:', kode_serial_upper)
print(f'{nama_produk} sejumlah {jumlah_produk} berhasil dibeli!')
print(f'Produk akan expired dalam {minggu_kadaluwarsa} minggu dan {hari_kadaluwarsa} hari.')
print(f'Saldo {nama_bank} anda sisa {saldo_akhir}.')

