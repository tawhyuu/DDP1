# def power(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x*power(x, n-1)
    
'''CHECKING IF WORD IS PALINDROM'''
# def is_palindrom(word):
#     if len(word) < 2 and len(word) >= 0:
#         return True
#     elif word[0] != word[-1]:
#         return False
#     else:
#         return is_palindrom(word[1:-1])

# print(is_palindrom(''))

# def count(nlst):
#     if len(nlst) == 0:
#         return 0
#     elif type(nlst[0]) == int:
#         return 1 + count(nlst[1:])
#     elif type(nlst[0]) == list:
#         return count(nlst[0]) + count()
    # result = 0
    # for item in nlst:
    #     if type(item) == list:
    #         result += count(item)
    #     elif type(item) == int:
    #         result += 1
    # return result

# print(count([3, [[1, [2]], [], 8], 4, [7, [6, 9]]]))

# def lst_fbc(n):
#     if n <= 1:
#         return [1]
#     else:
#         return lst_fbc(n-1) + [n + n + 1]
# print(lst_fbc(5))



# def is_substring(m, s):
#     '''Return True if sub_string in main_string'''
#     if m[:len(s)].lower() == s.lower():
#         return True
#     elif len(m) < len(s):
#         return False
#     else:
#         return is_substring(m[1:], s)

# print(is_substring('', ''))

# print('ABCD' == True)

'''Menghitung Angka genap dalam sebuah list'''
# def hitung_genap(lst):
#     count = 0
#     for item in lst:
#         if type(item) == list:
#             count += hitung_genap(item)
#         elif type(item) == int:
#             if item % 2 == 0:
#                 count += 1
#     return count
# print(hitung_genap([[1, 4,[3,4,1,[2,4]]],'anjing', [23, 0], [2, -1, 4], [], [7, 4]]))


'''FUNGSI MENGHITUNG KATA DIDALAM SEBUAH KATA'''
# def word_count(lst_word, word, count):
#     if len(lst_word) == 0:
#         return count
#     else:
#         if lst_word[0] == word:
#             count += 1
#         return word_count(lst_word[1:], word, count)
    
# def palindrom_count(lst_word, count):
#     if len(lst_word) == 0:
#         return count
#     else:
#         if is_palindrom(lst_word[0]):
#             count += 1
#         return palindrom_count(lst_word[1:], count)
# print(palindrom_count(['malam', 'apa', 'mengapa', 'a'], 0))

# def sum(lst_numb):
#     sum = 0
#     for item in lst_numb:
#         if type(item) == list:
#             sum += sum(item)
#         elif type(item) == int:
#             sum += item
#     return sum
# print(sum([1 ,[2 ,3 ,[4]]]))

def count_numb(lst_numb):
    count = 0
    for item in lst_numb:
        if type(item) == list:
            count += count_numb(item)
        elif type(item) == int:
            count += 1
    return count
print(count_numb([1 ,[2 ,3 ,[4]]]))

# def average(lst_numb):
#     sum = 0
#     count = 0
#     average = 0.0
#     for element in lst_numb:
#         if type(element) == list: