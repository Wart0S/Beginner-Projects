toplam = 0

while True:
    sayı = input("Sayı:")

    if (sayı == "q"):
        break

    sayı = int(sayı)

    toplam += sayı

print("Girdiğiniz Sayıların Toplamı",toplam)