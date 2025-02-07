# def count_neg(lst):
#     count = 0
#     for val in lst:
#         if val < 0:
#             count += 1
#     return count
# l = [2,-2,7,-3,-4,9]
# print(count_neg(l))

# def is_sorted(lst):
#     val = True
#     for i in range(len(lst)-1):
#         if lst[i] <= lst[i+1]:
#             val = True
#         else:
#             val = False
#             break
#     return val
# j = [2,2,2]
# print(is_sorted(j))

# with open('week8.txt', 'r') as file:
#     all_line = file.readlines()
# word_set = []
# for i in range(len(all_line)):
#     line = all_line[i].lower()
#     word_in_line = line.split()
#     for word in word_in_line:
#         # if '\n' in word:
#         #     word_set.append(word[:-1])
#         if word not in word_set:
#             word_set.append(word)
# print(word_set)

integer = int(input(''))