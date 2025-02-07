class Animal():
    legs = 4
    def __init__(self):
        self.kingdom = 'Animalia'
        print('Ini test 1')
        # super().__init__()

    def speak(self):
        print('Unable to speak')

class WalkingAnimal():
    def __init__(self):
        self.walking = 'WALK!!'
        print('Ini test 3')

class FlyingAnimal():
    def __init__(self):
        self.flying = 'FLY!!!'
        print('Ini test 2')
        # super().__init__()
        
    def fly(self):
        print('Flyin!')

class Bat(Animal, FlyingAnimal, WalkingAnimal):
    def __init__(self):
        super().__init__()
        super(FlyingAnimal, self).__init__()
        # Animal.__init__(self)
        # FlyingAnimal.__init__(self)
        # WalkingAnimal.__init__(self)

bat = Bat()
print(bat.kingdom)
print()