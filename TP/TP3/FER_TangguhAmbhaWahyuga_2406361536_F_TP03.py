def partition(lst, low, highest, descending:bool=True):
    """
    Fungsi untuk membagi list menjadi dua bagian berdasarkan pivot.
    """

    x = int(lst[highest]) # Pivot 
    i = low - 1 # Index elemen yg lebih kecil
    if descending:
        # Partisi untuk pengurutan descending
        for j in range(low, highest):
            if int(lst[j]) >= x:
                i = i + 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i+1], lst[highest] = lst[highest], lst[i+1]
        return i+1
    else:
        # Partisi untuk pengurutan ascending
        for j in range(low, highest):
            if int(lst[j]) <= x:
                i = i + 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i+1], lst[highest] = lst[highest], lst[i+1]
        return i+1 #posisi pivot setelah partisi

def QUICKSORT(lst, low, highest, descending:bool=True):
    '''
    Implementasi algoritma QuickSort untuk mengurutkan list
    '''
    if low < highest: #low dan highest disini adalah index
        q = partition(lst, low, highest, descending) # Mendapatkan posisi pivot
        QUICKSORT(lst, low, q-1, descending) # rekursi bagian kiri pivot
        QUICKSORT(lst, q+1, highest, descending) # rekursi bagian kanan pivot
    return lst
    
import time

def main():
    try:
        #validasi input user
        file = input('Input file name: ')
        with open(file, 'r') as file:
            line = file.read()
            line = line.splitlines()

        #output file
        output_file = input('Output file name: ')

        #ascending or descending
        descending = input('Ascending/Descending [A/D]: ')
        if descending.lower() == 'a':
            descending_value = False
        elif descending.lower() == 'd':
            descending_value = True
        else:
            print('Terdapat Variable yang tidak dapat diakses. Pastikan kembali input Anda')
            return
        
        t1 = time.time()
        t = time.process_time()

        print('\nSorting in progress ...')
        sorted_list = QUICKSORT(line, 0, len(line)-1, descending_value)

        cpu_time = time.process_time() - t
        duration = time.time() - t1

        with open(output_file, 'w') as output:
            for numb in sorted_list:
                print(numb, file= output)

        print("CPU time of the quicksort: ", cpu_time)
        print("Clock time of the quicksort: ", duration) 
        
    except FileNotFoundError: # Ketika nama file tidak ditemukan
        print(f'File {file} tidak ditemukan')
    except ValueError: # Throw ke sini ketika terdapat baris dari isi file yang bukan integer
        print('Isi file terdapat tipe selain integer')
    except UnboundLocalError: #Ketika ada lokal variable yang tidak bisa di access/tidak ditemukan
        print('Terdapat variable yang tidak bisa di akses. Periksa kembali input Anda.')


main()
