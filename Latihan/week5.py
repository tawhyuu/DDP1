nama_file = input("Input nama file: ")
# produk = input("Input nama produk: ")
file = open(nama_file,"r")
# baris_ke = 0

# for line in file:
#     line = line.strip()
#     baris_ke += 1
#     count = 0
#     for char in line:
#         if char == "a" or char == "i" or char == 'u' or char == 'e' or char == 'o':
#             count += 1
#     print(f"baris {baris_ke} ada {count} vokal")  

for line in file:
    for i in range(len(line)):
        sub_genome = line[i:3+i]
        print(sub_genome)
file.close()

# file = open(nama_file,'w')

# file.close()