from django.core.management.base import BaseCommand
from portfolio.models import Project, Education, Experience, Certificate
from datetime import date

class Command(BaseCommand):
    help = 'Portfolyo için başlangıç verilerini (projeler, CV deneyimleri, eğitim ve sertifikalar) yükler.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Başlangıç verileri güncelleniyor...")

        # 1. Projeler
        p1, _ = Project.objects.get_or_create(
            slug='android-gcn-malware-detection',
            defaults={
                'title': 'Android Malware Detection with GCN/GNN',
                'short_description': 'Android uygulamalarının izin metaverileri ve grafik sinir ağları (GNN/GCN) yaklaşımı kullanılarak gerçekleştirilen statik zararlı yazılım tespiti çalışması (Lisans Bitirme Tezi).',
                'description': (
                    "Bu çalışma, Drebin ve AndroZoo veri setlerindeki 11.000+ Android uygulamasının bildirim dosyalarından "
                    "(AndroidManifest.xml) çıkarılan izin ve özellik ilişkilerini bir grafik yapısı olarak modellemekte ve "
                    "Grafik Sinir Ağları (Graph Convolutional Networks - GCN) aracılığıyla statik zararlı yazılım analizi gerçekleştirmektedir.\n\n"
                    "Variance Threshold yöntemiyle düşük varyanslı 3.503 izin filtrelenerek özellik sayısı 111 kritik izne indirgenmiştir. "
                    "Uygulamaları ve izinleri düğüm, aralarındaki ilişkileri kenar olarak modelleyen App–Permission Bipartite Graf yapısı kurgulanmıştır. "
                    "PyTorch Geometric ile GCN tabanlı model geliştirilerek uygulamaların benign/malware olarak yüksek doğrulukla sınıflandırılması sağlanmıştır."
                ),
                'technologies': 'Python, PyTorch Geometric, NetworkX, Scikit-learn, Pandas, NumPy',
                'github_url': 'https://github.com/umutkilictas/android-gcn-malware-detection',
                'live_demo_url': '',
                'featured': True,
                'is_published': True,
                'display_order': 1,
            }
        )

        p2, _ = Project.objects.get_or_create(
            slug='opencv-smart-presence-monitor',
            defaults={
                'title': 'OpenCV Smart Presence Monitor',
                'short_description': 'Python ve OpenCV kullanılarak geliştirilen, kamera üzerinden gerçek zamanlı yüz ve hareket algılama gerçekleştiren olay kayıt uygulaması.',
                'description': (
                    "Kamera görüntüsünden Haar Cascade sınıflandırıcıları ile yüz ve varlık tespiti gerçekleştiren, "
                    "tespit sonuçlarını ekran görüntüsü ve log kayıtlarıyla takip eden pratik bir bilgisayarla görü uygulaması.\n\n"
                    "Olay anında zaman damgasıyla loglama ve kare yakalama fonksiyonları optimize edilmiştir."
                ),
                'technologies': 'Python, OpenCV, Haar Cascade, NumPy',
                'github_url': 'https://github.com/umutkilictas/opencv-smart-presence-monitor',
                'live_demo_url': '',
                'featured': True,
                'is_published': True,
                'display_order': 2,
            }
        )

        p3, _ = Project.objects.get_or_create(
            slug='mvc-cv-project',
            defaults={
                'title': 'MVC Kişisel Portfolyo Web Uygulaması',
                'short_description': 'ASP.NET Core MVC, Entity Framework Core ve SQL kullanılarak katmanlı mimari prensiplerine uygun olarak geliştirilen dinamik web uygulaması.',
                'description': (
                    "ASP.NET Core MVC ve Entity Framework Core kullanılarak katmanlı mimari prensiplerine uygun, "
                    "CRUD operasyonları barındıran dinamik bir kişisel portfolyo ve yönetim sistemi uygulaması."
                ),
                'technologies': 'C#, ASP.NET Core MVC, Entity Framework Core, SQL',
                'github_url': 'https://github.com/umutkilictas/MVC-Cv-Project',
                'live_demo_url': '',
                'featured': True,
                'is_published': True,
                'display_order': 3,
            }
        )

        # 2. Deneyimler (CV'den Birebir)
        Experience.objects.all().delete()

        exp1 = Experience.objects.create(
            title='Aday Mühendis',
            organization='SPACEARTS UZAY HAVACILIK VE SAVUNMA SANAYİ LTD. ŞTİ.',
            location='Ankara',
            date_text='Eylül 2024 – Aralık 2024',
            start_date=date(2024, 9, 1),
            end_date=date(2024, 12, 31),
            is_current=False,
            display_order=1,
            description=(
                "STM32 mikrodenetleyici üzerinde C dili ile temel gömülü yazılım geliştirme çalışmaları gerçekleştirdim.\n"
                "GPIO kontrolü, timer kullanımı ve düşük seviyeli sürücülerle çalışma üzerine uygulamalar yaptım.\n"
                "Küçük ekranlar üzerinde grafik ve arayüz elemanlarının görüntülenmesini sağlayan bir modül geliştirdim.\n"
                "Gömülü yazılım sürecinde hata ayıklama ve donanım-yazılım etkileşimi üzerine pratik deneyim kazandım."
            )
        )
        self.stdout.write(self.style.SUCCESS(f"Deneyim eklendi: {exp1.title} - {exp1.organization}"))

        exp2 = Experience.objects.create(
            title='Stajyer Mühendis',
            organization='DİVVYDRİVE BİLİŞİM TEKNOLOJİLERİ A.Ş.',
            location='Ankara',
            date_text='Temmuz 2024 – Eylül 2024',
            start_date=date(2024, 7, 1),
            end_date=date(2024, 9, 1),
            is_current=False,
            display_order=2,
            description=(
                "Postman kullanarak REST API isteklerinin ve yanıtlarının test edilmesi üzerine çalışmalar gerçekleştirdim.\n"
                "Hazır backend servislerini entegre ederek dosya ve klasör yönetimi özelliklerine sahip bir mobil uygulama geliştirdim.\n"
                "Eğitilmiş bir yapay zekâ modeli kullanarak klasörlerde bulunan görsellerin içeriklerine göre sınıflandırılmasını sağlayan bir Python scripti yazdım.\n"
                "Selenium ile otomasyon testleri kodladım; MD5, SHA-256 kriptografik algoritmaları ve OWASP Top 10 prensipleri üzerine araştırmalar yaptım."
            )
        )
        self.stdout.write(self.style.SUCCESS(f"Deneyim eklendi: {exp2.title} - {exp2.organization}"))

        # 3. Eğitim (CV'den Birebir)
        Education.objects.all().delete()

        edu1 = Education.objects.create(
            institution='Gazi Üniversitesi',
            faculty='Teknoloji Fakültesi',
            degree='Lisans — Bilgisayar Mühendisliği',
            gpa='2.77 / 4.00',
            location='Ankara',
            date_text='2021 – 2025',
            start_date=date(2021, 9, 1),
            end_date=date(2025, 6, 30),
            display_order=1,
            description=''
        )
        self.stdout.write(self.style.SUCCESS(f"Eğitim eklendi: {edu1.degree} ({edu1.institution})"))

        edu2 = Education.objects.create(
            institution='Develi Borsa İstanbul Fen Lisesi',
            faculty='',
            degree='Lise',
            gpa='87.53 / 100',
            location='Kayseri',
            date_text='2016 – 2020',
            start_date=date(2016, 9, 1),
            end_date=date(2020, 6, 30),
            display_order=2,
            description=''
        )
        self.stdout.write(self.style.SUCCESS(f"Eğitim eklendi: {edu2.degree} ({edu2.institution})"))

        # 4. Sertifikalar (6 Gerçek Sertifika)
        Certificate.objects.all().delete()

        certificates_data = [
            {
                'name': 'OpenCV 401',
                'issuer': 'Turkcell Geleceği Yazanlar',
                'description': 'İleri seviye bilgisayarla görü, derin öğrenme tabanlı nesne tespiti ve pratik görüntü işleme projeleri.',
                'issue_date': date(2026, 8, 4),
                'certificate_no': '',
                'certificate_file': 'certificates/opencv-401.pdf',
                'display_order': 1,
            },
            {
                'name': 'OpenCV 301',
                'issuer': 'Turkcell Geleceği Yazanlar',
                'description': 'Morfolojik operasyonlar, kontur analizi, kenar tespiti, filtreleme ve nesne takip algoritmaları.',
                'issue_date': date(2026, 8, 3),
                'certificate_no': '',
                'certificate_file': 'certificates/opencv-301.pdf',
                'display_order': 2,
            },
            {
                'name': 'OpenCV 201',
                'issuer': 'Turkcell Geleceği Yazanlar',
                'description': 'Görüntü okuma, renk uzayları dönüşümü, piksel matris işlemleri ve temel görüntü işleme teknikleri.',
                'issue_date': date(2026, 7, 31),
                'certificate_no': '',
                'certificate_file': 'certificates/opencv-201.pdf',
                'display_order': 3,
            },
            {
                'name': 'C# Programlama',
                'issuer': 'BTK Akademi',
                'description': 'Nesne yönelimli programlama prensipleri, C# dili mimarisi, veri yapıları ve algoritma geliştirme.',
                'issue_date': date(2025, 11, 13),
                'certificate_no': '9Xrtz4alA9',
                'certificate_file': 'certificates/csharp-programlama.pdf',
                'display_order': 4,
            },
            {
                'name': 'Güvenli Yazılım Geliştirme',
                'issuer': 'BTK Akademi',
                'description': 'Web ve yazılım güvenliği, yaygın güvenlik açıkları (OWASP Top 10), güvenli kodlama standartları ve savunma mekanizmaları.',
                'issue_date': date(2023, 1, 22),
                'certificate_no': 'jK1hKENyVG',
                'certificate_file': 'certificates/guvenli-yazilim-gelistirme.pdf',
                'display_order': 5,
            },
            {
                'name': 'Sosyal Mühendislik ve Oltalama',
                'issuer': 'BTK Akademi',
                'description': 'Siber güvenlik farkındalığı, oltalama (phishing) saldırı modelleri, bilgi güvenliği tehditleri ve kurumsal korunma yöntemleri.',
                'issue_date': date(2023, 1, 21),
                'certificate_no': 'ax1hDVGJjX',
                'certificate_file': 'certificates/sosyal-muhendislik-ve-oltalama.pdf',
                'display_order': 6,
            },
        ]

        for cert_dict in certificates_data:
            Certificate.objects.create(
                is_published=True,
                **cert_dict
            )

        self.stdout.write(self.style.SUCCESS("Tüm veriler (Projeler, Deneyimler, Eğitimler, Sertifikalar) başarıyla yüklendi!"))
