# def is_contain_vowel(word):
#     for char in word:
#         if char.lower() in 'aiueo':
#             return True
#     return False

# def count_word_with_vowel(sentence):
#     count = 0
#     for word in sentence.split():
#         if is_contain_vowel(word):
#             count +=1
#     return count

# nama_file = input('Nama File: ')

# with open(nama_file, 'r') as file:
#     count = 0
#     for sentence in file:
#         count += count_word_with_vowel(sentence)
#     print(count)

# Program menerima input 5 buah integer
# a, b , c, d
# tampilkan nilai paling besar diantara 


# def max_value(a,b,c,d,e):
#     max = a
#     if b>a>c>d>e:
#         max = b
#     elif c>a>d>e:
#         max = c
#     elif d>a>e:
#         max = d
#     elif e>a:
#         max = e
#     return max

# #Program Utama
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# d = int(input('d = '))
# e = int(input('e = '))
# print(max_value(a,b,c,d,e))

# def reverse_str(num):
#     b = str(num)[::-1]
#     return b

# def get_digit(num, i):
#     return reverse_str(num)[i]

# def get_digits(numb, pos):
#     return (numb//(10**pos))%10


# print(get_digits(73954, 2))

file = open('vibrio_cholerae.txt', 'r')
isi = file.read()
print(len(isi))