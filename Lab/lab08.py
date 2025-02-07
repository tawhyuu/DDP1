courses = {
    "MPK Agama": [],
    "MPK B. Inggris": [],
    "Kalkulus 1": [],
    "Matematika Diskret 1": [],
    "Dasar-Dasar Pemrograman 1": [],
    "Manajemen Bisnis": [],
    "Komunikasi Bisnis dan Teknis": [],
    "MPKT": [],
    "Matematika Diskret 2": [],
    "Dasar-Dasar Pemrograman 2": ["Dasar-Dasar Pemrograman 1"],
    "Dasar-Dasar Arsitektur Komputer": [],
    "Prinsip Prinsip Sistem Informasi": [],
    "Pemrograman Berbasis Platform": ["Dasar-Dasar Pemrograman 1"],
    "Struktur Data & Algoritma": ["Dasar-Dasar Pemrograman 1"],
    "Aljabar Linear": [],
    "Pengantar Sistem Informasi": ["Dasar-Dasar Arsitektur Komputer"],
    "Pengantar Statistika": [
        "Kalkulus 1",
        "Matematika Diskret 1"
    ],
    "Basis Data": ["Dasar-Dasar Pemrograman 2"],
    "Sistem Interaksi": ["Pemrograman Berbasis Platform"],
    "Pengantar Keamanan Perangkat Lunak": ["Dasar-Dasar Pemrograman 2"],
    "Manajemen Proyek TI": [
        "Prinsip Prinsip Sistem Informasi",
        "Manajemen Bisnis"
    ],
    "Sistem Informasi Perusahaan dan Akuntansi": ["Manajemen Bisnis"],
    "Arsitektur dan Pemrograman Aplikasi Perusahaan": [
        "Pemrograman Berbasis Platform",
        "Basis Data",
        "Struktur Data & Algoritma"
    ],
    "Jaringan Komunikasi dan Data": ["Pengantar Sistem Informasi"],
    "Manajemen Sistem Informasi": [
        "Prinsip Prinsip Sistem Informasi",
        "Pengantar Sistem Informasi"
    ],
    "Analisis dan Perancangan Sistem Informasi": [
        "Basis Data",
        "Prinsip Prinsip Sistem Informasi"
    ],
    "MPPI": [],
    "Proyek Pengembangan Sistem Informasi": [
        "Sistem Interaksi",
        "Arsitektur dan Pemrograman Aplikasi Perusahaan",
        "Analisis dan Perancangan Sistem Informasi",
        "Basis Data"
    ],
    "KASDAD": [
        "Struktur Data & Algoritma",
        "Aljabar Linier",
        "Pengantar Statistika"
    ],
    "TA Individu / TA Kelompok": ["MPPI"],
    "Kerja Praktik": [],
    "Komputer & Masyarakat": [],
}

def find_main_prerequisite(course, syarat=''):
    if len(courses[course]) == 0:
        # Ketika Matkul tidak memili matakuliah syarat maka dia akan menambahkan string kosong.
        syarat += ''
    for matkul in courses[course]:
        syarat += matkul + ', ' # Menambahkan syarat mata kuliah ke dalam variable syarat
        syarat = find_main_prerequisite(matkul, syarat) #Rekursif case
    return syarat


# Main program
nama_mata_kuliah = input('Masukkan Nama Mata Kuliah: ')
syarat = find_main_prerequisite(nama_mata_kuliah)
if len(syarat) < 1:
    print('Mata kuliah ini tidak memiliki prasyarat')
else:
    print(f'Mata kuliah ini memiliki syarat {syarat[:-2]}.') #Ini :-2 agar ', ' di akhir syarat tidak ikut.

# Bonus
syarat_temp = set(syarat[:-2].split(',')) #Mengubah ke dalam list dengan split dan 
syarat_not_dupe = ''
for matkul_syarat in syarat_temp:
    syarat_not_dupe += matkul_syarat + ', '
print()
print('------INI ADALAH MATAKULIAH TANPA DUPLIKAT-------')
print(f'Mata kuliah ini memiliki syarat {syarat_not_dupe[:-2]}.') #Ini :-2 agar ', ' di akhir syarat tidak ikut.