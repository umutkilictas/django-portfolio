from django.test import TestCase
from django.urls import reverse
from portfolio.models import Project, Experience, Education, Certificate

class PortfolioTests(TestCase):
    def setUp(self):
        # Test için yayınlanmış proje
        self.published_project = Project.objects.create(
            title="Açık Kaynak Test Projesi",
            slug="acik-kaynak-test-projesi",
            short_description="Test amaçlı yayınlanmış proje kısa açıklaması.",
            description="Detaylı test açıklaması.",
            technologies="Python, Django, SQLite",
            github_url="https://github.com/umutkilictas",
            live_demo_url="",
            featured=True,
            is_published=True,
            display_order=1
        )

        # Test için yayınlanmamış (taslak) proje
        self.draft_project = Project.objects.create(
            title="Taslak Gizli Proje",
            slug="taslak-gizli-proje",
            short_description="Yayınlanmamış proje.",
            description="Bu proje dışarıya kapalı olmalı.",
            technologies="Python",
            featured=False,
            is_published=False,
            display_order=2
        )

        # Eğitim kaydı
        self.education = Education.objects.create(
            institution="Gazi Üniversitesi",
            degree="Bilgisayar Mühendisliği (Lisans)",
            description="Lisans eğitimi",
            display_order=1
        )

        # Deneyim kaydı
        self.experience = Experience.objects.create(
            title="Yazılım Geliştirici",
            organization="Kişisel Projeler",
            description="Django çalışmaları",
            is_current=True,
            display_order=1
        )

        # Sertifika kaydı
        self.certificate = Certificate.objects.create(
            name="OpenCV Eğitimi",
            issuer="Turkcell",
            description="Görüntü işleme sertifikası",
            is_published=True,
            display_order=1
        )

    # 1. Ana sayfa başarılı yanıt veriyor
    def test_home_page_status_code_and_content(self):
        response = self.client.get(reverse('portfolio:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Umut Kılıçtaş')
        self.assertContains(response, self.published_project.title)

    # 2. Tüm sayfaların URL'leri doğru çalışıyor
    def test_all_pages_urls_working(self):
        urls = [
            reverse('portfolio:home'),
            reverse('portfolio:about'),
            reverse('portfolio:project_list'),
            reverse('portfolio:experience'),
            reverse('portfolio:certificates'),
            reverse('portfolio:contact'),
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, f"URL {url} 200 dönmedi!")

    # 3. Projeler listesi yalnızca yayınlanmış kayıtları gösteriyor
    def test_project_list_shows_only_published(self):
        response = self.client.get(reverse('portfolio:project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.published_project.title)
        self.assertNotContains(response, self.draft_project.title)

    # 4. Proje detay sayfası doğru kaydı gösteriyor
    def test_project_detail_view_success(self):
        response = self.client.get(reverse('portfolio:project_detail', kwargs={'slug': self.published_project.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.published_project.title)
        self.assertContains(response, "Python")

    # 5. Bulunmayan proje için 404 dönüyor
    def test_project_detail_not_found_returns_404(self):
        response = self.client.get(reverse('portfolio:project_detail', kwargs={'slug': 'olmayan-proje-slugi'}))
        self.assertEqual(response.status_code, 404)

    # 6. Yayınlanmamış projeler ziyaretçilere görünmüyor (404 dönüyor)
    def test_draft_project_detail_returns_404(self):
        response = self.client.get(reverse('portfolio:project_detail', kwargs={'slug': self.draft_project.slug}))
        self.assertEqual(response.status_code, 404)

    # 7. Django Admin paneli erişilebilir
    def test_admin_login_accessible(self):
        response = self.client.get('/admin/login/')
        self.assertEqual(response.status_code, 200)

    # 8. Boş opsiyonel alanlar (live_demo_url, image vb.) hata oluşturmuyor
    def test_optional_fields_do_not_crash(self):
        project = Project.objects.create(
            title="Minimalist Proje",
            slug="minimalist-proje",
            short_description="Kısa açıklama",
            description="Uzun açıklama",
            technologies="Python",
            github_url="",
            live_demo_url="",
            image=None,
            is_published=True
        )
        response = self.client.get(project.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Minimalist Proje")

    # 9. İletişim sayfasında harici linkler ve güvenlik nitelikleri
    def test_contact_page_links(self):
        response = self.client.get(reverse('portfolio:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'https://github.com/umutkilictas')
        self.assertContains(response, 'rel="noopener noreferrer"')

    # 10. Model helper method test: get_technologies_list
    def test_project_technologies_list_parsing(self):
        tech_list = self.published_project.get_technologies_list()
        self.assertEqual(tech_list, ['Python', 'Django', 'SQLite'])
