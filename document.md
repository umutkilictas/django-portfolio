# Django Kişisel Portfolio Web Sitesi — Proje Şartnamesi

## 1. Projenin amacı

Kişisel ve profesyonel bir portfolio web sitesi geliştirilecek. Proje, Python ve Django kullanılarak hazırlanacak ve gerçek bir alan adı üzerinden internete yayınlanacak.

Bu proje aynı zamanda geliştiricinin ilk Django projesidir. Bu nedenle yalnızca çalışan kod üretmek yeterli değildir. Geliştirme sırasında yapılan işlemler anlaşılır biçimde açıklanmalı ve geliştiriciye Django'nun temel mantığı öğretilmelidir.

### Temel hedefler

- Profesyonel, modern ve minimalist bir tasarım.
- Türkçe arayüz.
- Açık ve koyu tema arasında geçiş.
- Çok sayfalı web sitesi.
- Projelerin Django Admin üzerinden yönetilebilmesi.
- Mobil, tablet ve masaüstü uyumluluğu.
- SEO, erişilebilirlik ve performans.
- Gerçek bir domain ve Django destekleyen hosting üzerinde yayın.
- Anlaşılabilir, gereksiz karmaşıklık içermeyen kod mimarisi.

## 2. Teknoloji tercihleri

Zorunlu teknolojiler:

- Python
- Django 5.2 LTS
- HTML5
- CSS3
- Bootstrap 5
- Django Template Language
- SQLite
- Django Admin
- Git ve GitHub

JavaScript yalnızca tema değiştirme, mobil menü veya gerekli küçük etkileşimler için kullanılabilir.

### Kullanılmayacak teknolojiler

- React
- Vue veya Angular
- Node.js tabanlı frontend mimarisi
- Gereksiz REST API katmanı
- Mikroservis mimarisi
- İlk sürümde gereksiz üçüncü taraf paketler
- Gereksiz animasyon kütüphaneleri

Django'nun standart template sistemi kullanılmalı. Frontend ayrı bir uygulama olarak oluşturulmamalı.

## 3. Geliştirici profili ve içerik

Site sahibi: Umut Kılıçtaş

Eğitim: Gazi Üniversitesi Bilgisayar Mühendisliği mezunu.

GitHub: https://github.com/umutkilictas

LinkedIn: https://linkedin.com/umut-kilictas

Tanıtım başlığı kesinleştirilmemiştir. Türkçe, doğal ve profesyonel bir başlık öner. Geliştiriciyi deneyimli uzman gibi göstermeye çalışma. Gerçek deneyim seviyesini aşan ifadeler, uydurma şirketler, başarılar veya ölçümler kullanma.

İçeriklerde aşağıdaki yaklaşımı benimse:

- Python ve Django odağı.
- Bilgisayar mühendisliği eğitimi.
- Gerçek yazılım projeleri.
- Öğrenmeye ve geliştirmeye devam eden bir yazılım geliştirici profili.
- Abartısız ve işe alım uzmanlarının kolayca anlayabileceği açıklamalar.

E-posta adresi henüz belirlenmemiştir. Kodda tek bir merkezi yapılandırma veya kolayca değiştirilebilen bir iletişim bağlantısı kullan. Gerçek e-posta adresi uydurma.

Profil fotoğrafı kullanılmayacak. CV PDF dosyası daha sonra eklenecek; dosya mevcut değilken çalışanmış gibi bir indirme bağlantısı oluşturma.

## 4. Tasarım sistemi

### Genel görünüm

Modern, minimal ve profesyonel bir tasarım oluştur.

- İyi tanımlanmış tipografi hiyerarşisi.
- Tutarlı boşluklar ve hizalamalar.
- Okunaklı proje kartları.
- Gereksiz dekorasyonlardan kaçınma.
- Tutarlı butonlar, kartlar ve bağlantılar.
- Sade ikon kullanımı.
- Hafif ve hızlı sayfa yüklemesi.

### Tema

İki tema desteklenmeli:

1. Koyu tema.
2. Açık tema.

Header içerisinde tema değiştirme düğmesi bulunmalı. Kullanıcının tercihi localStorage üzerinden saklanabilir. İlk ziyarette işletim sisteminin tema tercihi dikkate alınabilir.

Tema değişimi için sayfanın tamamını yeniden yüklemek gerekmemeli. Tema değişimi CSS değişkenleri üzerinden yönetilmeli.

### Renk sistemi

Renkler CSS custom properties ile tanımlanmalı. Her sayfada ayrı ayrı renk kodları yazılmamalı.

Koyu temada arka plan, metin, kart ve vurgu renkleri birbiriyle uyumlu olmalı. Açık temada da aynı tasarım dili korunmalı.

### Animasyon

Özel animasyonlar, parallax efektleri ve ağır geçişler kullanılmayacak. Bootstrap bileşenleri dışında gereksiz animasyon eklenmeyecek. Hover durumları sade olmalı.

### Responsive tasarım

Öncelikle mobil uyumluluk dikkate alınmalı.

Aşağıdaki ekranlarda test edilmeli:

- 360 px genişliğinde mobil ekran.
- 768 px tablet.
- 1366 px masaüstü.
- Geniş masaüstü ekranlar.

Yatay taşma, kesilen metinler veya mobilde kullanılamayan menüler bulunmamalı.

## 5. Sayfalar ve URL yapısı

Aşağıdaki sayfaları oluştur:

- `/` — Ana sayfa
- `/hakkimda/` — Hakkımda
- `/projeler/` — Projeler
- `/projeler/<slug>/` — Proje detay sayfası
- `/deneyim-egitim/` — Deneyim ve eğitim
- `/sertifikalar/` — Sertifikalar
- `/iletisim/` — İletişim

Her sayfada ortak bir header ve footer bulunmalı. Bu alanlar Django template inheritance kullanılarak oluşturulmalı.

Önerilen şablon yapısı:

- `base.html`
- `includes/navbar.html`
- `includes/footer.html`
- `home.html`
- `about.html`
- `projects/project_list.html`
- `projects/project_detail.html`
- `experience.html`
- `certificates.html`
- `contact.html`
- `404.html`

Ana sayfa diğer sayfaların uzun bir kopyası olmamalı. Her bölümden kısa bir özet sunmalı ve kullanıcıyı ilgili detay sayfasına yönlendirmeli.

## 6. Ana sayfa

Ana sayfa şu bölümlerden oluşmalı:

### Karşılama alanı

- Umut Kılıçtaş ismi.
- Kısa ve gerçekçi profesyonel tanıtım.
- Projeler sayfasına gitme düğmesi.
- GitHub bağlantısı.
- LinkedIn bağlantısı.
- CV indirme düğmesi için sonradan etkinleştirilebilecek bir alan.

CV dosyası henüz mevcut değilse düğme gizlenmeli veya devre dışı bırakılmalı.

### Hakkımda özeti

Eğitim geçmişini, teknik ilgilerini ve yazılım geliştirme hedefini anlatan kısa bir metin.

### Teknik yetkinlikler özeti

Python, Django, HTML, CSS, Bootstrap, SQL ve Git/GitHub gibi gerçekten çalışılan teknolojileri göster.

Teknik seviyeler, yüzde çubukları ve gerçek olmayan uzmanlık puanları kullanma. Teknolojileri gruplandırarak göster.

### Öne çıkan projeler

İlk üç proje kartı gösterilmeli.

Her kartta:

- Proje adı.
- Kısa açıklama.
- Kullanılan teknolojiler.
- GitHub bağlantısı.
- Varsa canlı demo bağlantısı.
- Proje detay sayfasına yönlendirme.

Ana sayfada “Tüm projeleri gör” bağlantısı bulunmalı.

### Deneyim ve eğitim özeti

Eğitim ve ilgili deneyimlerden kısa bir özet gösterilmeli.

### Sertifikalar özeti

Gerçek sertifika bilgileri gösterilmeli. Sertifika dosyası veya doğrulama bağlantısı mevcut değilse uydurulmamalı.

### İletişim çağrısı

Ziyaretçiyi iletişim sayfasına, GitHub'a veya LinkedIn'e yönlendir.

## 7. Projeler

Projeler dinamik olmalı ve Django Admin üzerinden eklenip düzenlenebilmelidir.

Başlangıçta aşağıdaki projeler kullanılmalı:

### Proje 1 — Android Malware Detection with GCN/GNN

GitHub:
https://github.com/umutkilictas/android-gcn-malware-detection

Android uygulamalarının izin metaverileri ve grafik tabanlı öğrenme yaklaşımı kullanılarak statik zararlı yazılım tespiti üzerine bir çalışma.

Açıklama teknik olarak doğru olmalı. Dinamik analiz yapıldığı veya doğrulanmamış sonuçlar elde edildiği iddia edilmemeli.

### Proje 2 — OpenCV Smart Presence Monitor

GitHub:
https://github.com/umutkilictas/opencv-smart-presence-monitor

Python ve OpenCV kullanılarak geliştirilen, kamera üzerinden varlık algılama ve olay kaydı özelliklerine sahip bir uygulama.

### Proje 3 — Django Portfolio

Bu web sitesi, geliştirilmekte olan proje olarak eklenebilir. Tamamlanmamış özellikleri bitmiş gibi sunma. Proje yayına alındıktan sonra canlı demo bağlantısı eklenebilir.

### Proje modeli

Django ORM üzerinden bir `Project` modeli oluştur.

Önerilen alanlar:

- `title`
- `slug`
- `short_description`
- `description`
- `technologies`
- `github_url`
- `live_demo_url`
- `image`
- `featured`
- `is_published`
- `created_at`
- `updated_at`
- `display_order`

Alanların zorunluluğunu doğru belirle. Örneğin canlı demo bağlantısı boş bırakılabilmeli.

`slug` benzersiz olmalı. Proje detay sayfası yalnızca yayınlanmış projeleri göstermeli. Bulunamayan projeler standart 404 sayfasına yönlendirilmeli.

Teknoloji listesi için ilk sürümde JSONField veya ayrı bir teknoloji ilişkisi gibi gereksiz karmaşıklıklar ekleme. Öğrenilebilir bir yapı tercih et.

### Projeler listesi

- Projeler kartlar halinde gösterilmeli.
- Öne çıkan projeler işaretlenebilmeli.
- Görseller için düzgün bir oran ve yedek görsel yaklaşımı kullanılmalı.
- Tüm projeler ayrı sayfada listelenmeli.
- Proje sayısı arttığında sayfalama eklenebilecek şekilde yapı kurulmalı.
- Henüz demo bağlantısı olmayan projelerde boş veya çalışmayan butonlar gösterilmemeli.

## 8. Hakkımda sayfası

Aşağıdaki içerikleri düzenli biçimde göster:

- Eğitim geçmişi.
- Yazılım geliştirmeye yaklaşım.
- Teknik ilgi alanları.
- Projeler ve öğrenme deneyimi.
- Kariyer hedefi.

Metin profesyonel ama doğal olmalı. Uzun bir özgeçmiş metnini sayfaya olduğu gibi yapıştırma.

## 9. Teknik yetkinlikler

Yetkinlikleri kategorilere ayır:

- Programlama: Python.
- Web geliştirme: Django, HTML, CSS, Bootstrap.
- Veritabanı: SQL ve PostgreSQL bilgisi.
- Araçlar: Git, GitHub, Postman.
- Proje bazlı deneyim: OpenCV, Selenium ve ilgili araçlar.

Bunları yalnızca gerçek deneyimle uyumlu biçimde sun. Henüz başlangıç düzeyindeki teknolojileri ileri seviye gibi gösterme.

## 10. Deneyim ve eğitim

Eğitim ve deneyim bilgileri ayrı kayıtlar olarak yönetilebilmeli.

Django Admin üzerinden ekleme, düzenleme ve sıralama desteklenmeli.

Önerilen `Experience` modeli:

- `title`
- `organization`
- `description`
- `start_date`
- `end_date`
- `is_current`
- `display_order`

Önerilen `Education` modeli:

- `institution`
- `degree`
- `description`
- `start_date`
- `end_date`
- `display_order`

Gerçek tarih ve şirket bilgilerini doğrulamadan üretme. Bilinmeyen alanları boş bırak veya başlangıç içeriği olarak daha sonra doldurulacak şekilde tasarla.

## 11. Sertifikalar

Django Admin üzerinden yönetilebilen bir `Certificate` modeli oluştur.

Önerilen alanlar:

- `name`
- `issuer`
- `description`
- `issue_date`
- `credential_url`
- `certificate_file`
- `display_order`
- `is_published`

İlk sürümde gerçekten mevcut sertifikalar eklenmeli. Turkcell Akademi Geleceği Yazanlar OpenCV 201/301/401 eğitimleri için doğru sertifika ve eğitim adları doğrulanmalı.

Dosya yükleme özelliği kullanılacaksa güvenli dosya türü ve boyut sınırları belirlenmeli. Sertifika dosyası yoksa indirme bağlantısı gösterilmemeli.

## 12. İletişim sayfası

İlk sürümde backend üzerinden mesaj gönderme formu yapılmayacak.

- E-posta bağlantısı `mailto:` ile çalışmalı.
- E-posta adresi tek bir yerden kolayca değiştirilebilmeli.
- GitHub ve LinkedIn bağlantıları gösterilmeli.
- Gerçek adres belirlenene kadar örnek veya sahte e-posta kullanılmamalı.
- Harici bağlantılarda uygun güvenlik nitelikleri kullanılmalı.

## 13. Django Admin

Admin paneli, içerik yönetiminin temel aracı olmalı.

Aşağıdaki kayıtlar yönetilebilmeli:

- Projects
- Experiences
- Education
- Certificates

Admin listelerinde başlık, yayın durumu ve sıralama gibi alanlar görünmeli. Arama ve filtreleme uygun modellerde etkinleştirilmeli.

İlk yönetici hesabı terminal üzerinden `createsuperuser` komutuyla oluşturulmalı. Yönetici parolası kaynak koduna yazılmamalı.

Admin paneli için özel bir frontend geliştirmeye gerek yok.

## 14. Veritabanı ve Django mimarisi

SQLite kullanılacak.

Veritabanı şeması Django modelleri ve migration sistemi üzerinden oluşturulmalı. `db.sqlite3` dosyası Git deposuna eklenmemeli.

İlk sürümde tek bir `portfolio` uygulaması altında anlaşılır modeller kullanılabilir. Kodun büyümesi durumunda uygulamaları ayırmak değerlendirilebilir.

Örnek proje yapısı:

```text
portfolio-site/
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── portfolio/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   ├── includes/
│   ├── projects/
│   └── portfolio/
└── static/
    ├── css/
    ├── js/
    └── images/
```

Bu yapı başlangıç için yeterlidir. Gereksiz repository, service, factory veya dependency injection katmanları oluşturma.

Django'nun standart ORM, URL yönlendirme, view, template, form ve admin mekanizmalarını kullan.

## 15. Güvenlik ve ortam ayarları

Geliştirme ve production ayarları birbirinden ayrılmalı.

- `SECRET_KEY` ortam değişkeninden alınmalı.
- `DEBUG=False` production ortamında kullanılmalı.
- `ALLOWED_HOSTS` doğru domainlerle sınırlandırılmalı.
- HTTPS ve güvenli cookie ayarları uygun şekilde yapılmalı.
- `.env` dosyası Git'e eklenmemeli.
- Gerçek parolalar, API anahtarları veya özel bilgiler kaynak koduna yazılmamalı.
- CSRF koruması devre dışı bırakılmamalı.
- Django Admin güçlü bir parola ile korunmalı.
- Üretim ortamında Django development server kullanılmamalı.

Deployment öncesinde `python manage.py check --deploy` çalıştırılmalı ve önemli uyarılar giderilmeli.

## 16. SEO ve erişilebilirlik

SEO için:

- Her sayfada anlamlı ve benzersiz `<title>`.
- Sayfa başına uygun meta description.
- Semantik HTML başlıkları.
- Açıklayıcı bağlantı metinleri.
- Görsellerde anlamlı `alt` metinleri.
- `robots.txt`.
- Uygun olduğunda `sitemap.xml`.
- Canonical URL kullanımı.
- Sosyal paylaşım meta etiketleri.

Domain belli olduğunda canonical URL ve sitemap adresleri gerçek domainle güncellenmeli.

Erişilebilirlik için:

- Yeterli renk kontrastı.
- Klavye ile erişilebilir navigasyon.
- Görünür focus durumları.
- Form veya düğmelerde anlamlı etiketler.
- Tema değiştirici için açıklayıcı erişilebilir ad.
- Yalnızca renkle bilgi aktarmaktan kaçınma.

## 17. Performans

- Bootstrap'ın gereksiz bileşenleri kullanılmamalı.
- Büyük görseller optimize edilmeli.
- Görseller uygun boyutlarda sunulmalı.
- Gerekli yerlerde lazy loading kullanılmalı.
- Gereksiz JavaScript ve CSS eklenmemeli.
- Django template yapısı sade tutulmalı.
- Production ortamında `collectstatic` çalıştırılmalı.
- Statik dosyalar hosting sağlayıcısının önerdiği yöntemle sunulmalı.

## 18. Test ve kabul kriterleri

En az aşağıdaki testler yazılmalı:

1. Ana sayfa başarılı yanıt veriyor.
2. Tüm sayfaların URL'leri doğru çalışıyor.
3. Projeler listesi yayınlanmış kayıtları gösteriyor.
4. Proje detay sayfası doğru kaydı gösteriyor.
5. Bulunmayan proje için 404 dönüyor.
6. Yayınlanmamış projeler ziyaretçilere görünmüyor.
7. Django Admin erişilebilir ve modeller yönetilebilir.
8. Boş opsiyonel alanlar hata oluşturmuyor.
9. Tema değiştirme çalışıyor.
10. İletişim bağlantıları doğru hedeflere gidiyor.
11. Mobil ekranda yatay taşma oluşmuyor.
12. Production ayarlarıyla uygulama başlatılabiliyor.

Testler için Django `TestCase` kullanılmalı. Her aşamanın sonunda test komutları çalıştırılmalı ve sonuçlar açıklanmalı.

## 19. Hosting ve domain

Hedef, yıllık toplam maliyeti mümkün olduğunca 1.000 TL civarında tutmaktır.

Öncelikli domain: `umutkilictas.com.tr`

Alternatifler:

- `umutkilictas.com`
- `umutkilictas.dev`

Domain satın almadan önce gerçek müsaitlik, ilk yıl fiyatı, yenileme fiyatı ve vergiler kontrol edilmeli.

İlk hosting adayı, Django/Python desteği bulunan uygun fiyatlı bir Python hosting paketidir. Mitade'nin Python hosting paketi incelenecek; ancak satın almadan önce aşağıdakiler teyit edilmeli:

- Uygun bir Python sürümü.
- Django ve WSGI desteği.
- SSH veya terminal erişimi.
- `pip` ile bağımlılık kurulumu.
- Domain bağlama ve HTTPS.
- Kalıcı dosya sistemi ve SQLite veritabanının korunması.
- Statik dosyaların sunulması.
- Yedekleme ve geri yükleme imkânı.
- Yıllık toplam fiyat ve yenileme maliyeti.

Uygun paket bulunamazsa alternatif Python hosting sağlayıcıları karşılaştırılmalı. Yalnızca Django destekleyen bir plan seçilmeli; klasik PHP hosting yeterli kabul edilmemeli.

Ücretsiz Render planı SQLite verilerinin kalıcılığı garanti edilmediğinden ana production seçeneği olarak kullanılmamalı.

### Deployment adımları

1. Yerel geliştirme ortamını çalışır hale getir.
2. Testleri çalıştır.
3. Git deposunu oluştur ve GitHub'a gönder.
4. Hosting hesabını oluştur.
5. Domaini satın al ve DNS ayarlarını yap.
6. Hosting üzerinde Python sanal ortamı oluştur.
7. `requirements.txt` içindeki bağımlılıkları kur.
8. Ortam değişkenlerini ayarla.
9. Django migration işlemlerini çalıştır.
10. Statik dosyaları `collectstatic` ile hazırla.
11. WSGI uygulamasını yapılandır.
12. HTTPS sertifikasını etkinleştir.
13. Yönetici hesabı oluştur.
14. Production ortamında tüm sayfaları ve admin panelini test et.
15. Veritabanı yedeği ve geri yükleme yöntemini belgele.

Yayınlama sırasında SQLite dosyasının yanlışlıkla sıfırlanması veya silinmesi önlenmeli. Deployment öncesinde veritabanı yedeği alınmalı.

## 20. Antigravity çalışma yöntemi

Bu projeyi tek seferde kontrolsüz biçimde üretme. Her aşamada çalıştırılabilir bir sonuç oluştur ve geliştiricinin onayını bekle.

### Aşama 1 — Planlama

- Mevcut proje klasörünü incele.
- Gerekli dosya yapısını planla.
- Kullanılacak Django sürümünü ve bağımlılıkları belirle.
- Sayfa ve model tasarımını açıkla.
- Henüz büyük miktarda kod yazma.

### Aşama 2 — Django iskeleti

- Projeyi ve uygulamayı oluştur.
- URL yönlendirmelerini kur.
- Template inheritance yapısını kur.
- Statik dosyaları bağla.
- Uygulamayı yerelde çalıştır.

### Aşama 3 — Tasarım

- Ortak header ve footer.
- Açık/koyu tema.
- Ana sayfa ve diğer sayfalar.
- Responsive Bootstrap tasarımı.

### Aşama 4 — Modeller ve Admin

- Modelleri oluştur.
- Migration işlemlerini çalıştır.
- Admin kayıtlarını hazırla.
- Örnek proje verilerini ekle.
- Projeler listesi ve detay sayfasını tamamla.

### Aşama 5 — Test ve kalite

- Otomatik testleri çalıştır.
- Hataları düzelt.
- Mobil görünümü kontrol et.
- SEO ve erişilebilirlik kontrolü yap.
- Production ayarlarını gözden geçir.

### Aşama 6 — Yayınlama

- Hosting seçeneklerini karşılaştır.
- Domain müsaitliğini kontrol et.
- Satın alma öncesinde maliyeti onay için sun.
- Kullanıcı hesabı, ödeme veya DNS gibi dış işlemler için gerekli yönlendirmeyi yap.
- Kullanıcı onayı olmadan satın alma işlemi gerçekleştirdiğini iddia etme.
- Yayına alma adımlarını tek tek uygula ve doğrula.

## 21. Öğretici açıklama kuralları

Her aşamada şu formatı kullan:

**Ne yapıyoruz?**  
İşlemin amacı.

**Neden yapıyoruz?**  
Django içindeki yeri ve tercih sebebi.

**Hangi dosyalar değişti?**  
Oluşturulan veya güncellenen dosyaların listesi.

**Nasıl test ederim?**  
Terminal komutları ve beklenen sonuçlar.

**Sık karşılaşılabilecek hata**  
Hatanın nasıl anlaşılacağı ve nasıl düzeltileceği.

Açıklamalar Türkçe olmalı. Teknik terimler gerektiğinde İngilizce isimleriyle birlikte açıklanmalı.

Kullanıcı yeni başlayan biri olduğu için aynı anda çok fazla kavram anlatma. Önce temel işleyişi öğret, ardından sonraki aşamaya geç.

Önemli dosyaları açıklamadan büyük kod blokları üretme. Kullanıcıdan bir şey çalıştırmasını istediğinde komutu, çalıştırılacağı dizini ve beklenen çıktıyı açıkça belirt.

Mevcut dosyalar üzerinde çalışırken önce içeriği incele. Çalışan kodu gereksiz yere yeniden yazma.

Her aşama tamamlandığında kısa bir özet sun ve bir sonraki aşamaya geçmeden önce kullanıcıya kontrol fırsatı ver.

## 22. Projenin tamamlanmış sayılma koşulları

- Tüm sayfalar çalışıyor.
- Tasarım mobil ve masaüstünde düzgün.
- Açık/koyu tema çalışıyor.
- Projeler Django Admin üzerinden yönetilebiliyor.
- GitHub bağlantıları doğru.
- SEO ve erişilebilirlik temel gereksinimleri tamam.
- Otomatik testler geçiyor.
- Production güvenlik kontrolleri yapıldı.
- Gerçek domain üzerinden HTTPS ile erişilebiliyor.
- Veritabanı yedeği alınabiliyor.
- README dosyasında kurulum, geliştirme, test ve deployment adımları mevcut.
- Kullanıcı projenin temel dosyalarının ve Django akışının ne işe yaradığını anlayabiliyor.

**İlk görev:** Mevcut çalışma klasörünü incele, bu şartnameye göre kısa bir uygulama planı hazırla ve yalnızca Aşama 1'i gerçekleştir. Onay almadan sonraki aşamalara geçme.