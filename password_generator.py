import random
import string

def şifre_oluştur(uzunluk = 12):
    harfler = string.ascii_letters
    sayılar = string.digits
    özel_karakterler = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    tüm_karakterler = harfler + sayılar + özel_karakterler
    şifre = ""
    for i in range(uzunluk):
        şifre += random.choice(tüm_karakterler)
    return şifre


while True:
    try:
        uzunluk = int(input("Kaç Karakterli Şifre İstiyorsunuz? (Maks 30): "))
        if 1 <= uzunluk <= 30:
            break  # Geçerli sayı, döngüden çık
        else:
            print("Lütfen 1 ile 30 arasında bir sayı girin!")
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")


sifre = şifre_oluştur(uzunluk)
print("Oluşturulan Şifre:", sifre)