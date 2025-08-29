print("""*******************************

ATM Makinesine Hoşgeldiniz

İşlemler:

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme


Programdan Çıkmak İçin 'q' Tuşuna Basınız.
*******************************
""")

bakiye = 10000

while True:
    işlem = input("İşlemi Giriniz:")

    if (işlem == "q"):
        print("Programdan Çıkılıyor...")
        break

    elif (işlem == "1"):
        print("Bakiyeniz {} ".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Miktarı Giriniz:"))
        bakiye += miktar

    elif (işlem == "3"):
        miktar = int(input("Miktarı Giriniz:"))

        if (bakiye - miktar < 0):
            print("Eksik Bakiye")
            continue
        bakiye -= miktar


    else:
        print("Geçersiz İşlem")