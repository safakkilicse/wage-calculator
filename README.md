# Maaş Hesaplama Web Uygulaması

Bu proje, Almanya'daki çalışanlar için saatlik ücret, gece mesaisi, hafta sonu mesaisi ve fazla mesai ücretlerini hesaplayan bir web uygulamasıdır. Uygulama, farklı vergi sınıflarına göre vergi kesintilerini de dikkate alır.

## Özellikler

- Normal çalışma saatleri, gece mesaisi, cumartesi ve pazar mesaisi için ayrı saat girişleri.
- Farklı vergi sınıflarına göre vergi kesintisi hesaplama.
- Gece mesaisi ve hafta sonu mesaileri için farklı bonus oranları.
- Fazla mesai ücretleri için yüzde 30 bonus hesaplama.
- Toplam ödeme ve vergi sonrası ödeme hesaplama.

## Kurulum

### Gereksinimler

- Python 3.x
- Flask

### Adımlar

1. Bu depoyu yerel makinenize klonlayın:
    ```sh
    git clone https://github.com/kullanici/maas-hesaplama.git
    ```
2. Proje dizinine gidin:
    ```sh
    cd maas-hesaplama
    ```
3. Gerekli bağımlılıkları yükleyin:
    ```sh
    pip install flask
    ```
4. Uygulamayı başlatın:
    ```sh
    python app.py
    ```

## Kullanım

1. Tarayıcınızda `http://127.0.0.1:5000/` adresine gidin.
2. Formdaki gerekli alanları doldurun:
    - Normal çalışma saatleri
    - Gece mesaisi (farklı saat dilimleri için)
    - Cumartesi çalışma saatleri
    - Pazar çalışma saatleri
    - Fazla mesai saatleri
    - Vergi sınıfı
3. "Hesapla" butonuna tıklayın.
4. Toplam ödeme ve vergi sonrası ödeme sonuçlarını görüntüleyin.

## Dosya Yapısı

- `app.py`: Ana Flask uygulama dosyası.
- `templates/`: HTML dosyalarının bulunduğu dizin.
  - `index.html`: Kullanıcıdan giriş verilerini alan form.
  - `result.html`: Hesaplama sonuçlarını gösteren sayfa.

## Vergi Sınıfları ve Oranları

- **Vergi Sınıfı 1**: %20 (Bekar, boşanmış, dul veya ayrı yaşayanlar)
- **Vergi Sınıfı 2**: %18 (Bekar ebeveynler)
- **Vergi Sınıfı 3**: %15 (Evli ve eşinin geliri olmayan veya düşük olan kişiler)
- **Vergi Sınıfı 4**: %20 (Evli ve eşlerin geliri benzer olan kişiler)
- **Vergi Sınıfı 5**: %25 (Evli ve eşinin yüksek geliri olan kişiler)
- **Vergi Sınıfı 6**: %30 (İkinci veya ek bir işte çalışanlar)

## Örnek Hesaplama

### Giriş Verileri
- Normal Çalışma Saatleri: 8 saat
- Gece Mesaisi (11pm-12am ve 4am-6am, %25 vergi dışı): 1 saat
- Gece Mesaisi (12am - 4am, %40 vergi dışı): 2 saat
- Gece Mesaisi (11pm-12am ve 4am-6am, %25 vergi içi): 1 saat
- Gece Mesaisi (12am - 4am, %10 vergi içi): 2 saat
- Cumartesi Çalışma Saatleri: 5 saat
- Pazar Çalışma Saatleri: 5 saat
- Fazla Mesai Saatleri: 2 saat
- Vergi Sınıfı: 1

### Çıktı
- Toplam Ödeme (Vergi Öncesi): €X
- Toplam Ödeme (Vergi Sonrası): €Y

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
# wage-calculator
