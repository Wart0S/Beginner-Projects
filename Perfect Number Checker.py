while True:
    sayı = int(input("Sayı: "))

    i = 1
    toplam = 0

    while i < sayı:
        if sayı % i == 0:
            toplam += i
        i += 1

    if toplam == sayı:
        print(sayı, "Mükemmel Bir Sayıdır.")
        break
    else:
        print(sayı, "Mükemmel Bir Sayı Değildir! Tekrar deneyin.")