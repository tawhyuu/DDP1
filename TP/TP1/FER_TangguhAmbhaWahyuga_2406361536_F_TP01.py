import turtle as t
import random

'''
==== Catatan Penting ====
Radius lingkaran = 50
Jarak antara 2 lingkaran = 20
Panjang keseluruhan lingkaran = 340
'''

# Warna khusus untuk cincin olimpiade
blue = (0, 129/255, 200/255)
yellow = (252/255, 177/255, 49/255)
black = (0,0,0)
green = (0, 166/255, 81/255)
red = (238/255, 51/255, 78/255)

def draw_square(color):
    t.down()
    t.color(color)
    t.begin_fill()
    for sisi in range(4):
        t.setheading(sisi*-90)
        t.fd(sisi_square)
    t.end_fill()
    t.up()

def draw_big_square():
    global coord_text
    # Untuk melakukan set start coordinate di pojok kiri atas
    start_coordx = -(sisi_big_square/2)
    start_coordy = -(start_coordx)-200
    t.up()
    t.pensize(1)
    t.speed(10)
    for baris in range(int(rows)):
        for kolom in range(int(rows)):
            color = (random.random(), random.random(), random.random())
            t.goto(start_coordx + (sisi_square*kolom), start_coordy)
            draw_square(color)
        start_coordy = start_coordy - sisi_square
    
    '''
    Menyimpan coordinate setelah menggambar kotak paling bawah akan di panggil 
    ketika ingin menulis Text dibawah Big Square
    '''
    coord_text = t.pos() 

def print_text():
    t.up()
    t.pencolor('blue')
    t.goto(0,coord_text[1]-(sisi_square + 40))
    t.write(f'Olympic Logo and Colorful Chessboard of {int(rows)**2} Squares',
            align='center',
            font=('Arial', 14, 'normal'))

def draw_half_circle(color, radius, heading, degree):
    t.pensize(8)
    t.down()
    t.color(color)
    t.setheading(heading)
    t.circle(radius, degree)
    t.up()

def circle_chain():
    start_circlex = 170
    start_circley = 0
    color = red, green, black, yellow, blue
    t.speed(10)
    t.up()
    for i in range(5):
        t.goto(start_circlex - (60*i), start_circley)
        draw_half_circle(color[i], 50, 90, 180)
    for j in range(5):
        t.goto(-start_circlex + (60*j), start_circley)
        draw_half_circle(color[-1-j], 50, -90, 180)

def draw_circle_3_per_4(color, radius, heading, degree):
    t.pensize(8)
    t.down()
    t.color(color)
    t.setheading(heading)
    t.circle(radius, degree)
    t.up()

def draw_circle_1_per_4(color, radius, heading, degree):
    t.pensize(8)
    t.down()
    t.color(color)
    t.setheading(heading)
    t.circle(radius, degree)
    t.up()

def circle_ring():
    '''
    Menggambar logo cincin olympic dengan menggunakan kombinasi
    3/4 lingkaran dan 1/4 lingkaran.
    '''

    t.penup()
    t.speed(10)

    '''
    Mentetapkan titik mulai di arah jam 7.30 dari titik pusat atau 225 derajat
    dengan menggunakan pythagoras dihasilkan
    radius^2 = x^2 + x^2 == (radius^2/2) = x^2 == (radius^2/2)**0.5 = x
    '''

    start_circlex_atas = 170 - (50 + ((50**2)/2)**0.5)
    start_circley_atas = -(((50**2)/2)**0.5) + 225 

    # Mencari titik koordinat x dan y untuk circle bawah
    # Coordinate X dan Y awal - (radius + setengah jarak lingkaran)
    start_circlex_bawah = start_circlex_atas - (50 + 10)
    start_circley_bawah = start_circley_atas - (50 + 10)

    color = red, green, black, yellow, blue
    for i in range(3):
        t.goto(start_circlex_atas - (120*i), start_circley_atas)
        draw_circle_3_per_4(color[i*2], 50, -45, -270)
        if i == 2:
            continue
        t.goto(start_circlex_bawah - (120*i), start_circley_bawah)
        draw_circle_3_per_4(color[i*2+1], 50, -45, 270)
        if i == 1: 
            # ketika selesai menggambar lingkaran 3/4 ke-2 bagian bawah save position
            start_circlex_bawah = t.pos()
    # Menyimpan coordinate setelah menggambar lingkaran 3/4 terakhir
    start_circlex_atas = t.pos()

    for j in range(3):
        t.goto(start_circlex_atas[0] + (120*j), start_circley_atas)
        draw_circle_1_per_4(color[-1-(j*2)], 50, 45, -90)
        if j == 2:
            continue
        t.goto(start_circlex_bawah[0] + (120*j),start_circley_bawah)
        draw_circle_1_per_4(color[-2-(j*2)], 50, -45, -90)

# Judul window turtle
t.title("Omlympic Logo and Colorful Chessboard")        
t.hideturtle()

# Meminta input dari user
rows = t.numinput('Olympic Logo and Colorful Chessboard',
                  'Enter the number of rows:', 
                  minval=2, maxval=25)
size_square = t.numinput('Olympic Logo and Colorful Chessboard',
                         'Enter the square size (pixel):',
                         minval=5, maxval=50)

# Menghitung ukuran kotak (Sisi kotak kecil dan sisi kotak besar)
sisi_square = ((size_square)**0.5)*4
sisi_big_square = (rows*sisi_square)

circle_ring()
circle_chain()
draw_big_square()
print_text()
t.exitonclick()