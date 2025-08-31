import random
import time

print("""**************************

Sayı Tahmin Oyunu

**************************""")

rastgele_sayı = random.randint(1, 100)
tahmin_hakkı = 9

while True:

    tahmin = int(input("Tahmin: "))

    if (tahmin < rastgele_sayı):
        print("Bilgiler Doğrulanıyor..")
        time.sleep(1)

        print("Daha Büyük Sayı Seçiniz.")
        tahmin_hakkı -= 1

    elif (tahmin > rastgele_sayı):
        print("Bilgiler Doğrulanıyor..")
        time.sleep(1)

        print("Daha Küçük Sayı Seçiniz.")
        tahmin_hakkı -= 1


    else:
        print("Tebrikler Doğru Rakamı Buldunuz!")
        break

    if (tahmin_hakkı == 0):
        print("Tahmin Hakkınız Bitti.")
        print("Doğru Cevap:",rastgele_sayı)
        break