decimal = int(input("Masukan decimal: "))
list_hexa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "F"]
decimal_to_biner = decimal
sisa_bagi = decimal
biner = ""
if decimal_to_biner != 0:
    while decimal_to_biner > 0: # Decimal to Biner
        sisa_bagi = decimal_to_biner % 2
        biner += str(sisa_bagi)
        decimal_to_biner //= 2
    print(biner[::-1])
else:
    print("0")
       
if decimal != 0:
    hexa = ""
    while decimal > 0: # Decimal to hexa
        sisa_bagi = decimal % 16
        hexa += str(list_hexa[sisa_bagi])
        decimal //= 16
    print(hexa[::-1])
else:
    print("0")