# BLM101 – Bilgisayar Mühendisliğine Giriş Dönem Projesi

1.  Öğrenci Bilgileri
- **Ad Soyad:** Bartu Çağlayan
- **Öğrenci Numarası:** 25360859089

---

2. Proje Konusu
**Ağlar, İnternet ve HTML**  
Python ile **Otomatik HTML Sayfası Oluşturucu**

---







3. YouTube Video Linki :




---

4. Proje Açıklaması
Bu proje, Python programlama dilinin String (Metin) işleme ve Dosya Yazma (File Write) yeteneklerini kullanarak, kullanıcıdan alınan verilerle dinamik bir web sayfası (HTML) oluşturur. Program, kullanıcının teknik bir HTML/CSS bilgisine ihtiyaç duymadan, konsol üzerinden girdiği bilgilerle kişisel bir web sayfası tasarlamasını sağlar.

Kullanılan Kütüphaneler
Projede Python'un yerleşik kütüphaneleri kullanılmıştır, harici bir kuruluma gerek yoktur:

os: Dosya yollarını yönetmek ve oluşturulan HTML dosyasını otomatik açmak için (Opsiyonel).

Temel dosya işlemleri (open, write) kullanılmıştır.

5. Algoritma ve Çalışma Mantığı
Kodun çalışma prensibi "Girdi - İşlem - Çıktı" döngüsü üzerine kuruludur ve proje yönergesinde belirtilen şu adımları takip eder:

Veri Girişi (Input):

Program kullanıcıya konsol üzerinden sırasıyla sorular sorar: "Adınız nedir?", "Biyografiniz nedir?", "Aldığınız dersler nelerdir?".

Dersler listesi alınırken kullanıcı 'q' tuşuna basana kadar döngü devam eder ve veriler bir liste yapısında tutulur.

Şablon Oluşturma ve İşleme (Process):

Python içerisindeki bir String değişkeninde, standart HTML5 iskeleti (DOCTYPE, html, head, body) tutulur.

Bu HTML şablonunun içine CSS kodları gömülerek sayfanın renkli ve düzenli görünmesi sağlanır.

Kullanıcının girdiği veriler (Ad, Biyografi, Dersler), f-string formatlama yöntemi ile HTML etiketlerinin (<h1>, <p>, <ul>, <li>) arasına yerleştirilir.

Dosya Oluşturma (Output):

Oluşturulan nihai metin bloğu, index.html adında bir dosya olarak kaydedilir.

Sonuç olarak, projenin bulunduğu klasörde tarayıcıda çalışmaya hazır, listeli ve stilli bir web sayfası meydana gelir.

6. Nasıl Çalıştırılır?
Bilgisayarınızda Python'un yüklü olduğundan emin olun.

Bu repodaki src (veya kodlar) klasörüne gidin.

Terminal veya IDE üzerinden .py uzantılı ana dosyanızı çalıştırın.

Konsoldaki soruları cevaplayın.

Program bittiğinde klasörde oluşan index.html dosyasına çift tıklayarak web sayfanızı görüntüleyin.

7. Depo (Repo) İçeriği
Genel proje yönergesine uygun olarak repo şu dosyaları içerir:

📂 /src (veya kodlar): Python kaynak kodları.

📄 sunum.pdf: Konu anlatımı ve proje detaylarını içeren sunum dosyası.

📝 README.md: Proje dökümantasyonu (Şu an okuduğunuz dosya).

🌐 index.html: (Program çalıştırıldıktan sonra örnek olarak oluşan çıktı dosyası).
