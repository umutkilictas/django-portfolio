from django.core.management.base import BaseCommand
from portfolio.models import Project, Education, Experience, Certificate
from datetime import date

class Command(BaseCommand):
    help = 'Portfolyo için başlangıç verilerini (projeler, eğitim ve sertifikalar) yükler.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Başlangıç verileri yükleniyor...")

        # 1. Projeler
        p1, created = Project.objects.get_or_create(
            slug='android-gcn-malware-detection',
            defaults={
                'title': 'Android Malware Detection with GCN/GNN',
                'short_description': 'Android uygulamalarının izin metaverileri ve grafik sinir ağları (GNN/GCN) yaklaşımı kullanılarak gerçekleştirilen statik zararlı yazılım tespiti çalışması.',
                'description': (
                    "Bu çalışma, Android uygulama paketlerinin (APK) bildirim dosyalarından (AndroidManifest.xml) "
                    "çıkarılan izin ve özellik ilişkilerini bir grafik yapısı olarak modellemekte ve Grafik Sinir Ağları "
                    "(Graph Convolutional Networks - GCN) aracılığıyla statik zararlı yazılım analizi gerçekleştirmektedir.\n\n"
                    "Geleneksel imza tabanlı tespit yöntemlerinin yetersiz kaldığı durumlar için makine öğrenimi ve "
                    "grafik temsilleri kullanılarak yüksek doğruluklu sınıflandırma hedeflenmiştir."
                ),
                'technologies': 'Python, PyTorch, PyTorch Geometric, NetworkX, Scikit-learn',
                'github_url': 'https://github.com/umutkilictas/android-gcn-malware-detection',
                'live_demo_url': '',
                'featured': True,
                'is_published': True,
                'display_order': 1,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Proje eklendi: {p1.title}"))

        p2, created = Project.objects.get_or_create(
            slug='opencv-smart-presence-monitor',
            defaults={
                'title': 'OpenCV Smart Presence Monitor',
                'short_description': 'Python ve OpenCV kullanılarak geliştirilen, kamera üzerinden gerçek zamanlı varlık ve hareket algılama gerçekleştiren olay kayıt uygulaması.',
                'description': (
                    "Kamera akışı üzerinden görüntü işleme teknikleriyle hareket ve insan varlığını algılayan akıllı "
                    "izleme sistemi. Belirli bir alanda hareket veya insan algılandığında zaman damgasıyla olay loglaması "
                    "yapar ve görsel kareleri kayıt altına alır.\n\n"
                    "Optimizasyon teknikleri uygulanarak düşük gecikme ve kararlı kare hızı (FPS) hedeflenmiştir."
                ),
                'technologies': 'Python, OpenCV, NumPy, SQLite',
                'github_url': 'https://github.com/umutkilictas/opencv-smart-presence-monitor',
                'live_demo_url': '',
                'featured': True,
                'is_published': True,
                'display_order': 2,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Proje eklendi: {p2.title}"))

        p3, created = Project.objects.get_or_create(
            slug='django-portfolio',
            defaults={
                'title': 'Django Kişisel Portfolio Web Sitesi',
                'short_description': 'Django 5.2 LTS, Bootstrap 5 ve SQLite kullanılarak geliştirilmiş, açık/koyu tema destekli, Django Admin üzerinden yönetilebilir kişisel portfolyo platformu.',
                'description': (
                    "Bu web sitesi; sürdürülebilir Django MVT mimarisi, temiz kod prensipleri ve mobil uyumlu Bootstrap 5 "
                    "bileşenleri kullanılarak sıfırdan geliştirilmiştir.\n\n"
                    "Projeler, deneyimler ve sertifikalar Django Admin üzerinden dinamik olarak yönetilebilmekte; açık ve koyu tema "
                    "geçişi modern CSS değişkenleri ile sorunsuz şekilde sağlanmaktadır."
                ),
                'technologies': 'Python, Django 5.2 LTS, Bootstrap 5, SQLite, HTML5, CSS3, JavaScript',
                'github_url': 'https://github.com/umutkilictas',
                'live_demo_url': '',
                'featured': True,
                'is_published': True,
                'display_order': 3,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Proje eklendi: {p3.title}"))

        # 2. Eğitim
        edu, created = Education.objects.get_or_create(
            institution='Gazi Üniversitesi',
            degree='Bilgisayar Mühendisliği (Lisans)',
            defaults={
                'description': (
                    "Yazılım mühendisliği, algoritmalar ve veri yapıları, nesne yönelimli programlama, "
                    "veri tabanı yönetim sistemleri, işletim sistemleri ve yapay zeka dersleri başarıyla tamamlandı."
                ),
                'display_order': 1,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Eğitim eklendi: {edu.degree}"))

        # 3. Deneyim
        exp, created = Experience.objects.get_or_create(
            title='Yazılım Geliştirici (Bağımsız & Açık Kaynak)',
            organization='Kişisel Projeler',
            defaults={
                'description': (
                    "Python ve Django ekosistemi üzerinde web uygulamaları geliştirme; bilgisayarla görü (OpenCV) ve "
                    "grafik modelleri (GNN/PyTorch) üzerine uygulamalı projeler üretme. Temiz kod, sürdürülebilirlik "
                    "ve Git versiyon kontrol prensiplerini uygulama."
                ),
                'is_current': True,
                'display_order': 1,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Deneyim eklendi: {exp.title}"))

        # 4. Sertifikalar
        cert, created = Certificate.objects.get_or_create(
            name='OpenCV ile Görüntü İşleme (201 / 301 / 401)',
            issuer='Turkcell Geleceği Yazanlar',
            defaults={
                'description': (
                    "Görüntü okuma, morfolojik filtreler, kenar tespiti (Canny, Sobel), renk uzayları, "
                    "kontur tespiti ve nesne izleme konularında kapsamlı uygulamalı eğitim programı."
                ),
                'display_order': 1,
                'is_published': True,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Sertifika eklendi: {cert.name}"))

        self.stdout.write(self.style.SUCCESS("Tüm başlangıç verileri başarıyla yüklendi!"))
