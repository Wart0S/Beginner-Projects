while True:
    try:
        boy = float(input("Boyunuzu Metre Cinsinden Giriniz (Örnek: 1.75): "))
        if boy > 3:
            raise ValueError("Boyunuzu Metre Cinsinden Giriniz, örnek: 1.75")
        break
    except ValueError:
        print("Hatalı Giriş:")


while True:
    try:
        kilo = float(input("Kilonuzu kg Cinsinden Giriniz: "))
        if kilo <= 0:
            raise ValueError("Kilonuz Sıfırdan Büyük Olmalı!")
        break
    except ValueError:
        print("Hatalı Giriş:")


vki = kilo / (boy ** 2)
print(f"Vücut Kitle İndeksiniz: {vki:.2f}")

if vki < 18.5:
    print("Durum: Zayıf")

elif 18.5 <= vki < 24.9:
    print("Durum: Normal")

elif 25 <= vki < 29.9:
    print("Durum: Fazla Kilolu")

else:
    print("Durum: Obez")