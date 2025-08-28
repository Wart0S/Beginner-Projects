print("""*******************************************
Hesap Makinesi Programı

İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpla İşlemi

4. Bölme İşlemi
*******************************************
""")

a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))

İşlem = input("İşlemi Giriniz:")

if İşlem == "1":
    print("{} ile {} toplamı {} dir".format(a,b,a+b))

elif İşlem == "2":
    print("{} ile {} farkı {} dir".format(a,b,a-b))

elif İşlem == "3":
    print("{} ile {} çarpımı {} dir".format(a,b,a*b))

elif İşlem == "4":
    print("{} ile {} bölümü {} dir".format(a,b,a/b))

else:
    print("Geçersiz İşlem")