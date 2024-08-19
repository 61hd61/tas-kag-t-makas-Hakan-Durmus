import random

def tas_kagıt_makas_Hakan_Durmus():
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Kurallar: Taş, Kağıt veya Makas'tan bir tanesini seçin.")
    print("Taş, Makas'ı ezer; Makas, Kağıt'ı keser; Kağıt, Taş'ı sarar.")
    print("İlk iki turu kazanan oyunu kazanır!")
    print("Oyun Büyük ve Küçük harf duyarlılığı vardır!")


    while True:
        # oyun sayacı ve oyuncuların puanları
        secenekler = ["Taş", "Kağıt", "Makas"]
        oyun_sayisi = 0
        puan_kullanıcı = 0
        puan_bilgisayar = 0


        while puan_kullanıcı<2 and puan_bilgisayar < 2:

            # bilgisayarın ve kullanıcının seçimini alma

            bilgisayar_secimi = random.choice(secenekler)
            kullanıcı_secimi = input("'Taş, Kağıt ve Makas' dan bir tanesini seçiniz: ")


            while kullanıcı_secimi not in secenekler:
                print("Oyun büyük ve küçük harf duyarlılığı var. Lütfen Taş, Kağıt ve Makas'tan bir tanesini seçiniz. Tercihinizi yaparken daha dikkatli olun!")
                kullanıcı_secimi = input("'Taş, Kağıt ve Makas' dan bir tanesini seçiniz: ")
            # oyun sonuçlarını belirleme
            if kullanıcı_secimi == bilgisayar_secimi:
                print("Bilgisayarın seçimi: ", {bilgisayar_secimi})
                oyun_sayisi += 1
                print("Berabere Kaldınız :", "Oynadığınız oyun sayısı: ", {oyun_sayisi}, "Senin puanın: ",
                      {puan_kullanıcı}, "Bilgisayarın puanı: ", {puan_bilgisayar})

            elif (kullanıcı_secimi == "Taş") and (bilgisayar_secimi == "Kağıt"):
                print("Bilgisayarın seçimi: ", {bilgisayar_secimi})
                puan_bilgisayar += 1
                oyun_sayisi += 1
                print("Kaybettiniz (Kural: Kağıt Taş'ı sarar) :", "Oynadığınız oyun sayısı: ", {oyun_sayisi},
                      "Senin puanın: ",
                      {puan_kullanıcı}, "Bilgisayarın puanı: ", {puan_bilgisayar})

            elif (kullanıcı_secimi == "Makas") and (bilgisayar_secimi == "Kağıt"):
                print("Bilgisayarın seçimi: ", {bilgisayar_secimi})
                puan_kullanıcı += 1
                oyun_sayisi += 1
                print("Kazandınız (Kural: Makas Kağı'ı keser) :", "Oynadığınız oyun sayısı: ", {oyun_sayisi},
                      "Senin puanın: ",
                      {puan_kullanıcı}, "Bilgisayarın puanı: ", {puan_bilgisayar})

            else:
                print("Bilgisayarın seçimi: ", {bilgisayar_secimi})
                puan_kullanıcı += 1
                oyun_sayisi += 1
                print("Kazandınız (Kural: Kağıt Taş'ı sarar) :", "Oynadığınız oyun sayısı: ", {oyun_sayisi},
                      "Senin puanın: ",
                      {puan_kullanıcı}, "Bilgisayarın puanı: ", {puan_bilgisayar})

        # oyunun galibini belirleme

        if puan_kullanıcı == 2:
            print("Tebrikler oyunu kazandınız!")
        else:
            print("Bilgisayar kazandı. bir dahaki sefere daha şanslı olun!")


        # oyuna devam edip etmeyeceğinin belirlenmesi

        Kullanıcının_DevamEtme_İstegi = input("Devam etmek istiyor musunuz? Evet ya da Hayır yazınız!: ")
        Bilgisayarın_DevamEtme_İstegi = random.choice(["Evet", "Hayır"])

        if Kullanıcının_DevamEtme_İstegi != "Evet" or Bilgisayarın_DevamEtme_İstegi != "Evet":
            print("Oyun Bitti, Bir Daha Ki Sefere Görüşmek Üzere!")
            break
        else:

            print("Oyuna Devam. Yeni Oyun Başlıyor!")

# fonksiyonu çağırma
tas_kagıt_makas_Hakan_Durmus()



















