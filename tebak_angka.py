import random

def tebak(x):
    angka_random = random.randint(1, x)
    angka = 0
    while angka_random != angka:
        angka = int(input('masukan tebakan : '))
        print(f"tebakan kamu : {angka}")
        if angka > angka_random:
            print("angka kamu terlalu besar")
        elif angka < angka_random:
            print("angka kamu telalu kecil")
    print(f"tebakan kamu benar : {angka}")

tebak(12)
