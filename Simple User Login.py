print("""****************************
Kullanıcı Girişi
****************************
""")


aks_kullanıcı_adı = "Enes"
aks_parola = "12345"

kullanıcı_adı = input("Kullanıcı Adı:")
parola = input("Parola:")

if (kullanıcı_adı == aks_kullanıcı_adı and parola != aks_parola):
    print("Parola Hatalı Tekrar Deneyiniz!")

elif (kullanıcı_adı != aks_kullanıcı_adı and parola == aks_parola):
    print ("Kullanıcı Adı Hatalı Tekrar Deneyiniz!")

elif (kullanıcı_adı != aks_kullanıcı_adı and parola != aks_parola):
    print("Kullanıcı Adı Ve Parola Hatalı Tekrar Deneyiniz!")

else:
    print("Sisteme Başarıyla Giriş Yapıldı Hoşgeldiniz!")

