nama_file = input(': ')
file = open(nama_file,'r')
sum = 0
for line in file:
    count = 0
    for i in line:
        if i=='a' or i=='u' or i=='e' or i =='o' or i =='i':
            count += 1
    sum += count
print(sum)
file.close()