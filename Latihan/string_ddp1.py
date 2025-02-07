# Pembandingan string dengan operasi logika akan membandingkan nilai
# ASCII dengan fungsi ord()

# dosen = 'Pak Alfan'
# dosen = dosen.join("A")
# print(dosen)

# def common_end(a, b):
#   if a[0:-2:-1] == b[0:-2:-1]:
#     print(a[0:-2:-1],b[0:-2:-1])
#     return True
#   else:
#     return False

# common_end([1, 2, 3],[7, 3, 2])

# listint = [1, 2, 3]
# inte = [7, 3, 2]
# print(listint[0])

# # Code untuk mengecek palindrom atau bukan
# kata = input("Masukkan kata: ")
# kata = kata.lower()
# pol_kata = ""
# for i in range(len(kata)):
#     pol_kata += kata[-i-1]

# if pol_kata == kata:
#     print("Palindrom")
# else:
#     print("Bukan Palindrom")

# # Code untuk menghitung huruf vokal pada kalimat
# count = 0
# for j in kata:
#     if j == 'a' or j == 'i' or j == 'u' or j == 'e' or j == 'o':
#         count += 1
# print(f"Banyak huruf vokal ada {count}")

# star = int(input("Masukan int positif: "))
# for i in range(star):
#     print("*"*(i+1))
# for j in range(star):
#     print(f"{star:>{star}}".format("*"*(j+1)))