# def star_ganjil(val):
#     for i in range(val):
#         print(' '*((val//2)-i) +'*'*((val//2)+i+1))

# star_ganjil(5)

# def remove_consecutive_chars(str):
#     string = ''
#     string_terakhir = str[-1]
#     for i in range(len(str)-1):
#         if str[i] != str[i+1]:
#             string += str[i]
#     string += string_terakhir
#     return string

# word = 'aakuu cintaaaa DDP1'
# a = remove_consecutive_chars(word)
# print(a)

# def acronym(str):
#     acronym = str[0].upper()
#     for i in range(len(str)):
#         if str[i] == ' ' and str[i+1] != ' ':
#             acronym += str[i+1].upper()
#     return acronym

# a = 'Central processing unit'
# print(acronym(a))

# with open('input_lab5.txt', 'r') as file:
#     lines = file.readlines()

# string = input('Kata adalah ')
# list_count = []
# for line in lines:
#     count = 0
#     count = (line.lower()).count(string.lower())
#     list_count.append(count)
# for i in range(len(list_count)):
#     if list_count[i] != 0:
#         print(f'baris {i+1} ada {list_count[i]} buah kata {string}')

# a = 'Halo halo bandung'
# print((a.lower()).count('halo'))