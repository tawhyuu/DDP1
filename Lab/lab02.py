start = input()
# Untuk convert biner, octa, dan hexadec
if start[1] == 'x':
    angka = int(start,16)
elif start[1] == 'o':
    angka = int(start,8)
elif start[1] == 'b':
    angka = int(start,2)
else:
    angka = int(start)
#untuk melakukan cek status code
if angka == 100:
    status_code = 'Continue'
elif angka == 200:
    status_code = 'Ok'
elif angka == 300:
    status_code = 'Multiple Choice'
elif angka == 400:
    status_code = 'Bad Request'
elif angka == 404:
    status_code = 'Not Found'
elif angka == 418:
    status_code = "I'm a teapot"
elif angka == 500:
    status_code = 'Internal Server Error'
else:
    status_code = 'Unknown'

print(f'{status_code} - {angka}')




