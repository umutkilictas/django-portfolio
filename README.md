# Umut Kılıçtaş — Django Kişisel Portfolyo

Gazi Üniversitesi Bilgisayar Mühendisliği mezunu Umut Kılıçtaş için geliştirilen modern, sade ve dinamik kişisel portfolyo web sitesi.

## Özellikler

- **Teknoloji Yığını:** Python 3.14, Django 5.2 LTS, Bootstrap 5, SQLite.
- **Tema Desteği:** Açık (Light) ve Koyu (Dark) tema geçişi (`localStorage` ve işletim sistemi tercihi uyumlu).
- **Yönetim:** Django Admin paneli üzerinden yönetilebilir dinamik projeler, deneyimler, eğitimler ve sertifikalar.
- **Tasarım:** Responsive, mobil öncelikli, modern kart mimarisi ve semantik HTML5.

## Yerel Geliştirme Kurulumu

1. **Depoyu klonlayın veya indirin:**
   ```bash
   cd djangoPortfolio
   ```

2. **Sanal ortam oluşturun ve aktif edin:**
   ```bash
   py -m venv .venv
   # Windows PowerShell için:
   .\.venv\Scripts\Activate.ps1
   ```

3. **Bağımlılıkları yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Çevre değişkenlerini ayarlayın:**
   ```bash
   cp .env.example .env
   ```

5. **Veritabanı migration işlemlerini yapın:**
   ```bash
   python manage.py migrate
   ```

6. **Geliştirme sunucusunu başlatın:**
   ```bash
   python manage.py runserver
   ```
   Tarayıcınızda `http://127.0.0.1:8000/` adresine gidin.

## Testleri Çalıştırma

```bash
python manage.py test
```
