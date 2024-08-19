Terminalde Taş-KağıtMakas Oyunu

Bilgisayara karşı oynanan klasik bir taş-kağıt-makas oynudur.

Oyuna başlarken kuralları öğrenmek isteyip istemeyeceğiniz sorulur.
Eğer kuralları öğrenmek isterseniz kuralları açıklar ve oyunu başlatır aksi takdirde oyun direkt başlar.
Bir karakter seçmeniz istenir, bu sırada bilgisayar da kendi kararkterini seçer.
Siz karakteri girdiğinizde biligisayarın da karakteri açıklanır ve kazanan belirlenir.
Bir taraf 2 kere kazandığında yeni oyun oynamak isteyip istemediğiniz sorulur.
Evet derseniz oyun skorları sıfırlanır ve yeni oyuna geçilir. Hayır derseniz döngü durur ve oyundan çıkılır.

Başlangıçta kullanıcının kuralları öğrenme kısmında kullanıcının girdiği karakterleri kodla uyumlu olması için küçülten lower() methodunu kullanıdım
Sonrasında girilen karakterin kodla uyumlu olamsı için oyuncunun karakterinde capitalize() methodunu kullandım.
Bilgisayarın karakter seçiminde ise random kütüphanesini kullandım.

Kodun abşında bizi oyun kurallarının ve oyuna geçişin olduğu bir kod bloğu karşılıyor.
Sonrasında secim isimli bir fonksiyon başlıyor.Bu fonksiyon sayesinde karakter seçimleri ve oyuncu skorları belirleniyor.
En sonda oyunun kazananı belirleniyor ve yeni oyuna geçilmesi soruluyor.
