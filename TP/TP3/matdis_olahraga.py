# import itertools

# def find_words_with_ga(base_string, substring, length):
#     # Menghasilkan semua kombinasi dari karakter dalam base_string
#     combinations = set(itertools.permutations(base_string, length))
    
#     # Menyaring kombinasi yang mengandung substring 'GA'
#     valid_words = [''.join(comb) for comb in combinations if substring in ''.join(comb)]
    
#     return valid_words

# # String dasar dan parameter pencarian
# base_string = 'OLAHRAGA'
# substring = 'HAL'
# length = 6

# # Mencari kata-kata yang sesuai
# result = find_words_with_ga(base_string, substring, length)

# # Menampilkan hasil
# print(f"Kata-kata dengan panjang {length} yang mengandung '{substring}':")
# print(result)
# print(len(result))
# # for word in result:
# #     print(word)

# # Menampilkan jumlah kata yang ditemukan
# print(f"\nJumlah kata yang ditemukan: {len(result)}")

from itertools import permutations

def count_words_with_substring(word, length, substrings):
    # Menghasilkan semua kombinasi huruf dari kata yang diberikan
    unique_permutations = set(permutations(word, length))
    
    count = 0
    for perm in unique_permutations:
        perm_word = ''.join(perm)
        # Cek apakah salah satu substring ada di dalam kata
        if any(sub in perm_word for sub in substrings):
            count += 1
    
    return count

# Kata yang diberikan
word = 'OLAHRAGA'
length = 6
substrings = ['GA', 'HAL']

# Hitung jumlah kata yang memenuhi syarat
result = count_words_with_substring(word, length, substrings)
print(f'Jumlah cara kata yang dapat dibentuk: {result}')