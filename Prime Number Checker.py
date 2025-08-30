def asalsayımı(sayı):
    if (sayı == 1):
        return False
    elif (sayı == 2):
        return True

    else:
        for i in range(2,sayı):
            if (sayı % i == 0):
                return False
        return True

while True:
    sayı = input("Sayı:")

    if (sayı == "q"):
        print("Programdan Çıkılıyor..")
        break


    else:
        sayı = int(sayı)

        if (asalsayımı(sayı)):
            print(sayı,"Asal Bir Sayıdır.")

        else:
            print(sayı,"Asal Bir Sayı Değildir.")