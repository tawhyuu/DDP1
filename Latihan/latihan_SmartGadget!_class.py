from datetime import datetime
class Phone:
    def __init__(self, phone_number, battery=100):
        self.phone_number = phone_number
        self.battery = battery

    def getBatteryStatus(self):
        return f'Battery Phone: {self.battery}%'
    
    def call(self, duration):
        consumption = 2 * duration
        if self.battery >= consumption:
            self.battery -= consumption
            print(f'Panggilan berlangsung selama {duration} menit')
        else:
            print('Baterai tidak cukup untuk panggilan')

    def getTime(self):
        return datetime.now().date()
    
class Watch:
    def getTime(self):
        return datetime.now()
    
class SmartWatch(Watch, Phone): 
    # Urutan MROnya SmartWatch, Watch, Phone, Object.
    # Watch di dahulukan agar sw.getTime akan menjalankan getTime dari Watch
    # def __init__(self, phone_number):
    #     # Menjalankan __init__() dari Phone untuk mendapatkan instance var
    #     super().__init__(phone_number)  

    def trackSteps(self, steps):
        consumption = steps//100
        if self.battery >= consumption:
            self.battery -= consumption
            print(f'Langkah tercatat: {steps}')
        else:
            print('Baterai tidak cukup untuk mencatat langkah')

sw = SmartWatch('08815373790')
print('sw.call(5)')
sw.call(5)
print('sw.getBatteryStatus()')
print(sw.getBatteryStatus())
print('sw.getTime()')
print(sw.getTime())
print('sw.trackSteps(1000)')
sw.trackSteps(1000)
print('sw.getBatteryStatus()')
print(sw.getBatteryStatus())