import random

list_mentor = [
    "Jenisa Bunga",
    "Jessica Tandra",
    "Favian Muhammad Rasyad Reswara",
    "Rafi Nazir",
    "Mirza Radithya",
    "Felesia Junelus",
    "Arisa Raezzura Zahra",
    "Christna Yosua Rotinsulu",
    "Tiara Widyaningrum",
    "Naomi Kyla Zahra Siregar",
    "Hazeta Rahmani Wafda",
    "Naira Ammara Putri",
    "Muhammad Hamiz Ghani Ayusha",
    "Raditya Ikhlas Kusuma",
    "Nadila Salsabila Fauziyyah",
    "Adam Rayyan Aryasatya",
    "Marvin De Grein Hoke",
    "Jaysen Lestari",
    "Arya Putra Parikesit",
    "Abigail Namaratonggi Pasaribu",
    "Kalista Wiarta",
    "Ahmad Wasis Shofiyulloh",
    "Roberto Eugenio Sugiarto"
]

list_anak = [
    # Data Anak yang tinggal di panti
    "Jasmine: 4 SD",
    "Yani: 1 SMP",
    "Siti: 1 SMP",
    "Malika: 1 SMP",
    "Kia: 1 SMP",
    "Katrina: 1 SMP",
    "Rini: 1 SMA",
    "Endang: 1 SMA",
    
    # Data Anak yang Tinggal di Luar Asrama
    "Hafidz: 1 SD",
    "Syakil: 1 SD",
    "Raja: 1 SD",
    "Rizky: 1 SD",
    "Arpin: 1 SD",
    "Olivia: 1 SD",
    "Riska: 2 SD",
    "Putri: 2 SD",
    "Atika: 3 SD",
    "Reysha: 5 SD",
    "Aditya: 1 SMP",
    "Alpin: 1 SMP",
    "Hana: 1 SMP",
    "Firza: 2 SMP",
    "Dina: 1 SMA"
]

mentors_assigned = set()  
anak_assigned = set()  

    
list_kelompok = []
counter = 0

while counter != 22:
    validat = False
    indeks_mentor = random.randint(0,22)
    indeks_anak = random.randint(0,22)

    mentor = list_mentor[indeks_mentor]
    anak = list_anak[indeks_anak]

    if mentor in mentors_assigned or anak in anak_assigned:
        continue
    list_kelompok.append((mentor, anak))
    mentors_assigned.add(mentor)
    anak_assigned.add(anak)
    print(f'{mentor} - {anak}')
    counter += 1

