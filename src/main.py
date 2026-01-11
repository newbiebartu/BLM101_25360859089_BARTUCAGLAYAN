import os
import webbrowser


# -----------------------------------------------------------
# BLM101 - Bilgisayar Mühendisliğine Giriş Dönem Projesi
# Grup 5: Ağlar, İnternet ve HTML
# Konu: Python ile Otomatik HTML Sayfası Oluşturucu
# -----------------------------------------------------------

def kullanici_verilerini_al():
    """
    # Bu fonksiyon kullanıcıdan ad, biyografi ve ders bilgilerini alır.
    """
    print("--- Web Sayfası Oluşturucuya Hoş Geldiniz ---")

    # Kullanıcıdan temel bilgileri istiyoruz [cite: 55]
    ad_soyad = input("Adınız Soyadınız nedir?: ")
    biyografi = input("Kısa biyografiniz (Kendinizi tanıtın): ")

    dersler = []
    print("\nAldığınız dersleri girin (Bitirmek için 'q' tuşuna basıp enterlayın):")

    # Kullanıcı 'q' diyene kadar dersleri listeye ekleyen döngü
    while True:
        ders = input("Ders adı: ")
        if ders.lower() == 'q':
            break
        dersler.append(ders)

    return ad_soyad, biyografi, dersler


def html_icerigi_olustur(ad, bio, ders_listesi):
    """
    # Bu fonksiyon alınan verileri HTML şablonuna yerleştirir ve CSS kodlarını ekler.
    """

    # Dersler listesini HTML liste elemanlarına (<li>) çeviriyoruz
    liste_html = ""
    for ders in ders_listesi:
        liste_html += f"            <li>{ders}</li>\n"

    # HTML Şablonu (f-string kullanarak verileri içine gömüyoruz) [cite: 54]
    # Yönerge gereği basit CSS renklendirmesi eklenmiştir [cite: 56]
    html_kod = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ad} - Kişisel Sayfa</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            color: #333;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max_width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }}
        .bio-kutusu {{
            background-color: #e8f6f3;
            padding: 15px;
            border-left: 5px solid #1abc9c;
            margin-bottom: 20px;
            font-style: italic;
        }}
        ul {{
            list-style-type: square;
        }}
        li {{
            margin-bottom: 5px;
            font-size: 1.1em;
        }}
        footer {{
            margin-top: 30px;
            text-align: center;
            font-size: 0.8em;
            color: #777;
        }}
    </style>
</head>
<body>

    <div class="container">
        <h1>Merhaba, Ben {ad}</h1>

        <h3>Hakkımda</h3>
        <div class="bio-kutusu">
            <p>{bio}</p>
        </div>

        <h3>Aldığım Dersler</h3>
        <ul>
{liste_html}
        </ul>

        <footer>
            <p>Bu sayfa Python BLM101 Projesi kapsamında otomatik oluşturulmuştur.</p>
        </footer>
    </div>

</body>
</html>
"""
    return html_kod


def dosyayi_kaydet(html_verisi):
    """
    # Bu fonksiyon oluşturulan HTML kodunu index.html adıyla dosyaya yazar.
    """
    dosya_adi = "index.html"

    # Dosya yazma işlemi (File Write) [cite: 54]
    try:
        with open(dosya_adi, "w", encoding="utf-8") as dosya:
            dosya.write(html_verisi)
        print(f"\n[BAŞARILI] '{dosya_adi}' dosyası başarıyla oluşturuldu.")

        # Oluşturulan dosyayı otomatik olarak tarayıcıda aç (Opsiyonel Kolaylık)
        webbrowser.open('file://' + os.path.realpath(dosya_adi))

    except Exception as hata:
        print(f"Dosya oluşturulurken hata meydana geldi: {hata}")


# --- Ana Program Akışı ---
if __name__ == "__main__":
    # 1. Adım: Verileri Al
    ad, bio, dersler = kullanici_verilerini_al()

    # 2. Adım: HTML Kodunu Hazırla
    olusan_html = html_icerigi_olustur(ad, bio, dersler)

    # 3. Adım: Dosyayı Kaydet
    dosyayi_kaydet(olusan_html)
