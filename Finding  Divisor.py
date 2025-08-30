def tambölen_bulma(sayi):
    tambolenler = []
    for i in range(2, sayi):
        if sayi % i == 0:
            tambolenler.append(i)
    return tambolenler

while True:
    girdi = input("Sayı (çıkmak için 'q'): ")

    if girdi.lower() == "q":
        print("Programdan Çıkılıyor..")
        break

    try:
        sayi = int(girdi)
        if sayi < 2:
            print("Lütfen 2 veya daha büyük bir sayı girin.")
            continue

        print("Tam Bölenler:", tambölen_bulma(sayi))

    except ValueError:
        print("Lütfen geçerli bir sayı girin.")