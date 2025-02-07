class Character:
    def __init__(self, name:str, level:int=1, health:int=100):
        self.__name = name
        self.__level = level
        self.__health = health

    def __str__(self):
        return 'Name: {}, Level: {}, Health: {}'.format(self.__name, self.__level, self.__health)
    
class Physical(Character):
    def __init__(self, name:str, strength:int, level:int=1, health:int=100):
        super().__init__(name, level, health)
        self.__strength = strength

    def __str__(self):
        return Character.__str__(self) + ', Strength: {}'.format(self.__strength)
    
    def attack(self):
        return 'Karakter {} menyerang dengan kekuatan {}'.format(self._Character__name, self.__strength)
    
    
class Magic(Character):
    def __init__(self, name:str, mana:int, level:int=1, health:int=100):
        super().__init__(name, level, health)
        self.__mana = mana

    def __str__(self):
        return Character.__str__(self) + ', Mana: {}'.format(self.__mana)
    
    def attack(self):
        return 'Karakter {} mengeluarkan mantra dengan kekuatan {}'.format(self._Character__name, self.__mana)

    
def main_program():
    print('\n=================================\n'
          'Menu\n'
          '[1] Buat karakter baru\n'
          '[2] Menyerang\n'
          '[3] Mengeluarkan mantra\n'
          '[4] Cetak info karakter\n'
          '[5] Keluar')
    
# Main Program
print('Selamat datang di Desktop Legend: Beng Beng!\n')
quit = False

lst_of_character_information = [] # Untuk menyimpan character information

magic_char = {} # Untuk menyimpan nama character dengan role magic dan mananya

physical_char = {} # Untuk menyimpan nama character dengan role physical dan strenght nya

while not quit: 
    main_program()
    option = input('Pilih menu: ')
    if option == '1':
        role = input('Peran karakter (Physical/Magic): ')
        name = input('Nama karakter: ')

        if role.lower() == 'physical':
            strenght = int(input('Strength: '))
            lst_of_character_information.append(Physical(name, strenght).__str__())
            physical_char.update({name:strenght})
            print(f'Seorang Physical bernama {name} telah di tambahkan')

        elif role.lower() == 'magic':
            mana = int(input('Mana: '))
            lst_of_character_information.append(Magic(name, mana).__str__())
            magic_char.update({name:mana})
            print(f'Seorang Magic bernama {name} telah di tambahkan')

        else:
            print('Maaf role tidak tersedia')

    elif option == '2':
        # meminta input dari user
        attacker = input('Nama karakter yang akan menyerang: ')
        if attacker in physical_char.keys(): # Validasi jika character tersebut adalah physical role
            atk = Physical(attacker, int(physical_char[attacker]))
            print(atk.attack()) # Return methode attack()
        else:
            print('Karakter bukan Physical')

    elif option == '3':
        # meminta input dari user
        caster = input('Nama karakter yang akan menyerang: ')
        if caster in magic_char.keys(): # Validasi jika character tersebut adalah magic role
            cstr = Magic(caster, int(magic_char[caster]))
            print(cstr.attack()) # Return methode attack()

    elif option == '4':
        for character in lst_of_character_information: # Interasi character information di dalam lst_of_char_information
            print(character)

    elif option == '5':
        quit = True
        print('Terimakasih sudah bermain di Desktop : Beng! Beng!')