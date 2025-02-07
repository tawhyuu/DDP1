# import math as m
# class Cone(object):
#     def __init__(self, tinggi=4, radius=3) -> None:
#         self.__tinggi = tinggi
#         self.__alas = (radius**2)*m.pi
    
#     def __str__(self) -> str:
#         return 'Kerucut dengan tinggi {} dan alas {}'.format(self.__tinggi, self.__alas)
    
#     def get_volume(self):
#         return 'Volume Kerucut adalah {}'.format((self.__alas*self.__tinggi)/3)
    
#     def set_radius(self, radius):
#         self.__alas = (radius**2)*m.pi

#     def set_tinggi(self, tinggi):
#         self.__tinggi = tinggi
        
# kerucut = Cone()
# print(kerucut)
# print(kerucut.get_volume())

# class MyClass:  
#     pass 
# print(dir(MyClass)) 
# my_instance = MyClass()  
# print(type(my_instance)) 
# print(dir(my_instance))
# print(my_instance.__class__)
'''Kuis Tanggal 18/11/2024'''
# class Makanan():
#     def __init__(self, nama:str, harga:int, pedas=False, bumbu=[]):
#         self.__nama = nama
#         self.__harga = harga
#         self.__bumbu = bumbu
#         if pedas == True:
#             self.__pedas = 'pedas'
#         else:
#             self.__pedas = 'tidak pedas'

#     def getDetails(self):
#         return ('Makanan {} dengan rasanya {} dengan kombinasi bumbu:{}').format(self.__nama, self.__pedas, self.__bumbu)

#     def buatPedas(self, pedas:bool):
#         if pedas == True:
#             self.__pedas = 'pedas'
#             print('Seuhaaah!')
#         else:
#             self.__pedas = 'tidak pedas'
#             print('Yahhh Lemah')

#     def tambahBumbu(self, bumbu:str):
#         self.__bumbu.append(bumbu)
#         print(f'Bumbu sedap {bumbu}')

# makanan  = Makanan('sate padang', 17000)
# print(makanan.getDetails())
# makanan.buatPedas(True)
# makanan.tambahBumbu('lada')
# print(makanan.getDetails())

'''Latihan PPT Slide Introduction OOP 34'''
# class NewClass(object):
#     def __init__(self, param_int=1):
#         self.the_int = param_int
#         if param_int%2 == 0:
#             self.parity = 'even'
#         else:
#             self.parity = 'odd'

#     def process(self, instance):
#         sum_int = self.the_int + instance.the_int
#         if sum_int < 0:
#             return 'negative'
#         elif sum_int%2 == 0:
#             return 'even'
#         else:
#             return 'odd'
        
#     def __str__(self):
#         return 'Value {} is {}'.format(self.the_int, self.parity)


'''Tentukan Output dibawah'''
# inst1 = NewClass(4)
# inst2 = NewClass(-5)
# inst3 = NewClass()
# print(inst1)
# print(inst1.parity)
# print(inst1.process(inst2))
# print(inst3.process(inst1))

'''Assign object sama saja menjalankan __init__ dari si class tsb'''
class A(object):
    a = 1
    def __init__(self):  
        self.a = 10

class B(A):
    pass

class C(B):
    pass

a1 = C()
print(a1.a)

'''Latihan BankAccount'''
# class BankAccount(object):
#     def __init__(self, account_number=None, owner=None, initial_balance=0):
#         self.__account_number = account_number
#         self.__owner = owner
#         self.__balance = initial_balance
    
#     def __str__(self):
#         return 'Account {} owned by {} has balance of {}'.format(self.__account_number, self.__owner, self.__balance)
    
#     def deposit(self, amount:int):
#         self.__balance += amount
    
#     def withdraw(self, amount:int):
#         self.__balance -= amount

#     def get_balance(self):
#         return self.__balance

# bankacc1 = BankAccount('Kafi9', 'KafiFawazAdabi', 10000)
# print(bankacc1)
# bankacc1.deposit(50000)
# print(bankacc1)
# bankacc1.withdraw()
