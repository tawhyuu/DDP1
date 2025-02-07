# Part I
def unique_words(words):
    '''Menyimpan Kata Yang Muncul dalam bentuk lower sekali saja'''
    list_unique_words = []
    for item in words:
        if item.lower() not in list_unique_words:
            list_unique_words.append(item.lower())
    return list_unique_words

# Part II
def count_words(word, words):
    '''Menghitung Jumlah Kata Dalam List of String'''
    count = 0
    for item in words:
        if item.lower() == word.lower():
            count += 1
    return count

# Part III
def word_freqs(ws, words):
    '''Mencari Frekuensi string di dalam List of String, Jika string terdapat di dalam List of String'''
    list_freqs_word = []
    for i in range(len(ws)):
        count = count_words(ws[i].lower(), words)
        list_freqs_word.append(count)
    return list_freqs_word

# Part IV

# nama_file = input("nama file = ")
# with open(nama_file) as file:
#     content = file.read()

#     words = content.split()
#     unique_ws = unique_words(words)
#     freqs_ws = word_freqs(unique_ws, words)

#     print("Daftar kata unik:")
#     for (w, freq) in zip(unique_ws, freqs_ws):
#         print(w, freq)

# Program ini memiliki run-time error ketika file yang di input user
# tidak terdeteksi di file user
# oleh karena itu hal ini bisa diatasi dengan try-except


# -------Main Program------
valid = True
while valid == True:
    try:
        nama_file = input("nama file = ")
        with open(nama_file) as file:
            content = file.read()

            words = content.split()
            unique_ws = unique_words(words)
            freqs_ws = word_freqs(unique_ws, words)

            print("Daftar kata unik:")
            for (w, freq) in zip(unique_ws, freqs_ws):
                print(w, freq)
            print(len(content))
            valid = False # Mengakhiri program

    except FileNotFoundError:
        print('File tidak ditemukan. Ulangi lagi!\n')
    except: # Sapu Jagat
        print('Ada error\n')