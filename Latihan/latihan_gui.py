'''Materi GUI'''
# Window 

# Widgets, selalu mempunyai properties, placement, variable
# Properties adalah tulisannya, warnanya, dll.
# Placement adalah mau ditaruh dimana widgetsnya agar rapih
# Variable bisa nenampung input user, variable di Tkinter memiliki\
# perbedaan dengan variable di python

# Event, Event driven programming
# Event source adalah sumber dari dimana event itu berlangsung
# contoh : mencet tombol add, artinya tombol add sumber eventnya
# Event object adalah segala detail event kita.
# Event handler/callback function, kita harus ngapain ketika klik sesuatu.

# Mainloop adalah GUI akan selalu terbuka

'''Untuk menambahkan widget'''
# Widgets harus disimpen ke suatu variable
# contoh : tkinter.Button(Master) 
# Master adalah container mana yang mau menampung button tsb
# kemudian variable tersebut harus di .pack()

'''Membuat Class Inherit tk.Frame'''
# Normalnya parameter __init__(self, master=None)
# super().__init__(master)

'''Ketika kita ingin event programming'''
# def function terlebih dahulu yang isi parameternya(self, event)
# contoh : print('Hello World')
# kata kuncinya adalah variable.bind('Eventnya', function)

# 
import tkinter as tk

window = tk.Tk()
print(dir(window))
window.title('Ini Adalah Judul Window')
window.geometry('500x100') # Geometry adalah size fleksibel. Sedangkan .maxsize(str) exact size
button = tk.Button(window, text='Halo Fitto', fg='#0000FF', bg='#FF0000')
button.pack() # Secara by default akan menaruh object di atas oleh python

# Berguna agar program tidak langsung exit ketika dijalankan
window.mainloop()
