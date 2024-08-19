import random

def tas_kagit_makas_Sedanur_Seker():
    print("Taş, Kağıt, Makas Oyununa Hoşgeldiniz!")
    kurallar= input("Kuralların açıklanmasını ister misiniz? evet/hayır=> ").lower()
    
    if kurallar == "evet":
        print("Oyunumuzda iki taraf vardır.(Siz ve Bilgisayar)\n3 seçenek vardır.(Taş,Kağıt,Makas)\nTaş makası kırar/Kağıt taşı sarar/Makas taşı keser.\nİlk iki turu kazanan oyunu kazanır.")
    elif kurallar == "hayır":
        print("Oyuna geçelim")
    else:
        raise ValueError("Geçersiz Giriş")

    def secim():
        baslangic= True
        bilgisayar_scor, oyuncu_scor = 0 , 0
        while baslangic == True:
            items = ("Taş","Kağıt","Makas")
            oyuncu= input("Karakterinizi seçiniz.(Taş/Kağıt/Makas)").capitalize()

            if oyuncu not in items:
                print("Geçersiz karakter!Tekrar deneyiniz.")
                continue
            
            bilgisayar= random.choice(items)
    

            durum1= "Berabere"
            durum2="Kazandınız"
            durum3="Kaybettiniz"

            if bilgisayar == oyuncu:
                print(durum1)    
            elif bilgisayar == "Taş" and oyuncu == "Makas":
                print("Bilgisayar Seçimi: Taş")
                print(durum3)
                bilgisayar_scor += 1
            elif bilgisayar == "Taş" and oyuncu == "Kağıt":
                print("Bilgisayar Seçimi: Taş")
                print(durum2)
                oyuncu_scor += 1
            elif bilgisayar == "Kağıt" and oyuncu == "Makas":
                print("Bilgisayar Seçimi: Kağıt")
                print(durum2)
                oyuncu_scor += 1
            elif bilgisayar == "Kağıt" and oyuncu == "Taş":
                print("Bilgisayar Seçimi: Kağıt")
                print(durum3)
                bilgisayar_scor += 1
            elif bilgisayar == "Makas" and oyuncu == "Kağıt":
                print("Bilgisayar Seçimi: Makas")
                print(durum3)
                bilgisayar_scor += 1    
            elif bilgisayar == "Makas" and oyuncu == "Taş":
                print("Bilgisayar Seçimi: Makas")
                print(durum2)
                oyuncu_scor += 1

            print(f"Oyuncu: {oyuncu_scor}    Bilgisayar: {bilgisayar_scor}")


            if bilgisayar_scor == 2 :
                print("KAYBETTİNİZ.\nLÜTFEN TEKRAR DENEYİN.")
                yeni_oyun = input("Yeni oyuna geçilsin mi? Evet/Hayır =>").capitalize()

                if yeni_oyun== "Evet":
                    print("Yeni oyuna geçiliyor!")
                    baslangic = True
                    bilgisayar_scor,oyuncu_scor = 0,0
                    continue
                else:
                    baslangic = False
                    print("Oyun sonlandırıldı.")
                       
            elif oyuncu_scor == 2:
                print("TEBRİKLER KAZANDINIZ")
                yeni_oyun = input("Yeni oyuna geçilsin mi? Evet/Hayır =>").capitalize()

                if yeni_oyun== "Evet":
                    print("Yeni oyuna geçiliyor!")
                    baslangic = True
                    bilgisayar_scor,oyuncu_scor = 0,0
                    continue
                else:
                    print("Oyun sonlandırıldı.")
                    baslangic = False
                             
            else:
                continue        
    
    secim()    
tas_kagit_makas_Sedanur_Seker()