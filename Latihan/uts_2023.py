''' Diamond Star '''
# try:
#     val = int(input('Masukkan Angka Ganjil : '))

#     if val%2 == 1:
#         for i in range(val//2+1):
#             print(' '*((val//2)-i), end='')
#             print('*'*(2*i+1))
#         for i in range(val//2):
#             print(' '*(i+1), end='')
#             print('*'*(val-(2*(i+1))))
# except ValueError:
#     print('Input harus berupa Int')

'''dec to biner'''
# def dec_to_signed_biner(x_dec):
#     x_bin = ''
#     if '-' in str(x_dec):
#         sign = '1'
#     else:
#         sign = '0'
#     x_dec = abs(x_dec)
#     while x_dec != 0:
#         x_bin = str(x_dec%2) + x_bin
#         x_dec //= 2
#     return sign + ('0'*(7-len(x_bin))) + x_bin

# print(dec_to_signed_biner(127))

'''Acronym'''
# def acronym(str):
#     acronym = str[0].upper()
#     for i in range(len(str)):
#         if str[i] == ' ' and str[i+1] != ' ':
#             acronym += str[i+1].upper()
#     return acronym

# a = 'Central processing unit'
# print(acronym(a))

'''File String'''
# nama_file = input('Nama File: ')
# kata = input('Sebuah kata')
# try:
#     with open(nama_file, 'r') as file:
#         lines = file.readlines()
#         lst_freq = []
#         for line in lines:
#             lst_freq.append((line.lower()).count(kata.lower()))
#         print(lst_freq)

#         for i in range(len(lst_freq)):
#             if lst_freq[i] == 0:
#                 continue
#             else:
#                 print(f'baris {i+1} ada {lst_freq[i]} buah kata {kata}')

# except:
#     print("Error")

'''Hastag'''
# def extract_hastag(str):
#     content = str.split()
#     lst_hashtags = []
#     for word in content:
#         if '#' in word.lower():
#             lst_hashtags.append(word.lower())
#     return lst_hashtags

# def count_hashtags(content, str):
#     lst_hashtags = extract_hastag(content)
#     return lst_hashtags.count("#"+str.lower())

# with open('uts1.txt', 'r') as file:
#     content = file.read()
#     print(extract_hastag(content))
#     print(count_hashtags(content, 'FAsilkomUI'))

# print("{:>02s}".format("1"))  # Padding dengan spasi)

'''counting negation in list of lists'''
# def count_neg_v2(lst_of_lsts):
#     lst_neg = []
#     for lst in lst_of_lsts:
#         count = 0
#         for item in lst:
#             if '-' in str(item):
#                 count += 1
#         lst_neg.append(count)
#     return lst_neg

# print(count_neg_v2 ([[0, -1], [-2,-4],[5,5],[4,-4]]))

# n = 5
# output = ''
# for i in range(n):
#     output += str(n)
#     n += 1
# print(output)

# mylist =['you','i','we']
# for word in mylist:
#     print('{:0>10}'.format(word))

# x = [3,2,1]
# y = x
# z = y
# y.append(7)
# z.remove(1)
# print(x)

print((10%2) and (10>None))
print(0 and True)