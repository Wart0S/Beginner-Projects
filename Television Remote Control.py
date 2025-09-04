import random
import time

class Kumanda():

    def __init__(self, tv_durumu="Kapalı", tv_ses=0, kanal_listesi=["Trt"], kanal="Trt"):
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal   # tuple hatasını düzelttim
        self.favoriler = []

    def tv_ac(self):
        if (self.tv_durumu == "Açık"):
            print("Televizyonunuz Zaten Açık.")
        else:
            print("Televizyonunuz Açılıyor Lütfen Bekleyiniz...")
            self.tv_durumu = "Açık"

    def tv_kapat(self):
        if (self.tv_durumu == "Kapalı"):
            print("Televizyonunuz Zaten Kapalı")
        else:
            print("Televizyonunuz Kapatılıyor...")
            self.tv_durumu = "Kapalı"

    def ses_ayarları(self):
        while True:
            cevap = input("Sesi Azaltmak İçin: '<'\nSesi Arttırmak İçin: '>'\nÇıkış: çıkış\nSeçimin: ")
            if cevap == "<":
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses:", self.tv_ses)
            elif cevap == ">":
                if (self.tv_ses != 100):
                    self.tv_ses += 1
                    print("Ses:", self.tv_ses)
            elif cevap == "çıkış":
                print("Ses Güncellendi", self.tv_ses)
                break
            else:
                print("Geçersiz seçim!")

    def kanal_ekle(self, kanal_ismi):
        print("Yeni Kanal Ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Yeni Kanal Eklendi...")

    def kanal_sil(self, kanal_ismi):
        if kanal_ismi in self.kanal_listesi:
            self.kanal_listesi.remove(kanal_ismi)
            print(f"'{kanal_ismi}' kanalı silindi.")
        else:
            print(f"'{kanal_ismi}' kanal listesinde bulunamadı.")

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Bulunduğunuz Kanal:", self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nBulunduğunuz Kanal: {}\n".format(
            self.tv_durumu, self.tv_ses, self.kanal_listesi, self.kanal
        )


kumanda = Kumanda()
print("""

Televizyon Uygulaması

1. Televizyon Aç
2. Televizyon Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısını Öğrenme
6. Rastgele Kanal
7. Televizyon Bilgileri
8. Kanal Sil

Çıkmak İçin 'q' ya Basınız.
""")

while True:
    işlem = input("İşlemi Seçiniz: ")
    if (işlem == "q"):
        print("Program Kapatılıyor...")
        break
    elif (işlem == "1"):
        kumanda.tv_ac()
    elif (işlem == "2"):
        kumanda.tv_kapat()
    elif (işlem == "3"):
        kumanda.ses_ayarları()
    elif (işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin: ")
        for kanal in kanal_isimleri.split(","):
            kumanda.kanal_ekle(kanal.strip())
    elif (işlem == "5"):
        print("Kanal Sayısı:", len(kumanda))
    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif (işlem == "7"):
        print(kumanda)
    elif (işlem == "8"):
        silinecek_kanal = input("Silmek istediğiniz kanalın ismini giriniz: ")
        kumanda.kanal_sil(silinecek_kanal)
    else:
        print("Geçersiz İşlem!")