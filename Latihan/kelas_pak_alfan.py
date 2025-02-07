# nama_file = input('Nama file ')
# with open(nama_file,'r') as file:
#     lines = file.readlines()
# str1 = input('Str adalah ')
# count_baris = 0
# for line in lines:
#     count_baris += 1
#     count = 0
#     line = line.split()
#     for word in line:
#         if str1 in word:
#             count += 1
#     print(f'baris {count_baris} ada {count}')

# Definisikan fungsi count_unique(lst) yang mempunyai parameter sebuah list of integers, kemudian mengembalikan list berisi dua buah elemen. 
# Elemen pertama adalah sebuah list of integers -> daftar angka unik
# kedua adalah sebuah list of integers juga -> frekuensi
# kemunculan masing-masing angka unik yang sesuaian

# def count_unique(lst):
#     list_unique = []
#     list_freq = []
#     for i in range(len(lst)):
#         if lst[i] not in list_unique:
#             list_unique.append(lst[i])  
#             list_freq.append(lst.count(lst[i]))
#     return [list_unique, list_freq]

# print(count_unique([4,8,2,4,8,4]))

# lst = [1,2,3,4]
# print(id(lst))
# lst += [5]
# print(lst)
# print(id(lst))
# # lst = lst + [5]
# lst1 = [1,2,3,4,5]
# print(lst1)
# print(id(lst1))

# a = 255556
# b = 255556
# print(a == b)
# print(id(a) == id(b))

# c = 50
# d = 50
# print(c == d)
# print(id(c) == id(d))

# print('f'>'cd')

# a = '10110'
# a = a[::-1]
# dec = 0
# for i in range(len(a)):
#     if a[i] == '1':
#         dec += 2**i
# print(ord('Z'))

# data = [(10, 'genap'), (25, 'Ganjil'), (13, 'GENAP')]
# output = []
# for (x, y) in data:
#     if x % 2 == 0 and y.lower() == 'genap':
#         output.append((x,y,True))
#     elif x % 2 == 1 and y.lower() == 'ganjil':
#         output.append((x,y,True))
#     else:
#         output.append((x,y,False))
# print(output)

# def factorial(int):
#     if int > 0:
#         return int*factorial(int-1)
#     else:
#         return 1
# print(factorial(5))

# def fibonaci(numb):
#     if numb == 1:
#         return [1]
#     elif numb == 2:
#         return [1,1]
#     else:
#         output = [1,1]

# print(fibonaci(7)

# def func(a):
#     if a == 0:
#         return 'mantap'
#     return a - 1

# print(func(func(func(func(func(func(5)))))))