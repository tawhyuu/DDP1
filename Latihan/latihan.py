keliling_lingkaran = lambda r: 2 * 3.14 * r

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Menjalankan {func.__name__} dengan argumen {args} {kwargs}")
        hasil = func(*args, **kwargs)
        print(f"Hasil: {hasil}")
        return hasil
    return wrapper

@logging_decorator
def pangkat(x,y):
    return x**y

@logging_decorator
def tambah(c,d):
    return c+d

def gen_fibonaci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

a = keliling_lingkaran(7)
b = pangkat(2,3)
c = tambah(5,5)
fib = list(gen_fibonaci(5))