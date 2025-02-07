valid = True
while valid == True:
    try: #Untuk melakukan cek apabila ada error FileNotFound atau error lainnya
        nama_file_input = input('nama file input = ')
        nama_file_output = input('nama file output = ')
        with open(nama_file_input, 'r') as file:
            list_line = file.readlines()
        valid = False
    except FileNotFoundError:
        print(f"Folder dengan nama {nama_file_input} tidak ditemukan.")
    except:
        print('Ada Error!!')

with open(nama_file_output, 'w') as file_output:
    count_huruf = 0
    baris_kosong = 0
    
    for i in range(len(list_line)): # Looping Untuk setiap baris dalam list baris menghitung hurufnya
        for char in list_line[i]:
            if char.isalpha():
                count_huruf += 1
        
        if list_line[i] == '\n':# Untuk menghitung baris yang kosong
            baris_kosong += 1
        
        print_baris = '{:03d}'.format((i+1))+'. ' + list_line[i]
        file_output.write(print_baris)
    
    baris_isi = len(list_line)-baris_kosong
    file_output.write(f'\n\nTotal banyaknya huruf = {count_huruf} huruf')
    file_output.write(f'\nBanyaknya baris tidak kosong = {baris_isi} baris')

print(f'\nakhir program, silakan buka isi {nama_file_output}')
print(list_line)