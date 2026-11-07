from django.db import models
from django.urls import reverse

class Project(models.Model):
    """
    Portfolyoda sergilenen yazılım projeleri.
    Admin panelinden eklenip düzenlenebilir.
    """
    title = models.CharField(max_length=200, verbose_name="Proje Başlığı")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL Slug (Benzersiz)")
    short_description = models.CharField(max_length=350, verbose_name="Kısa Açıklama (Kartlar için)")
    description = models.TextField(verbose_name="Detaylı Açıklama")
    technologies = models.CharField(
        max_length=250, 
        verbose_name="Kullanılan Teknolojiler", 
        help_text="Virgülle ayırarak yazın (Örn: Python, Django, SQLite)"
    )
    github_url = models.URLField(blank=True, verbose_name="GitHub Bağlantısı")
    live_demo_url = models.URLField(blank=True, verbose_name="Canlı Demo Bağlantısı (Varsa)")
    image = models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name="Proje Görseli")
    featured = models.BooleanField(default=False, verbose_name="Ana Sayfada Öne Çıkar")
    is_published = models.BooleanField(default=True, verbose_name="Yayınlandı mı?")
    display_order = models.PositiveIntegerField(default=0, verbose_name="Görüntülenme Sırası (Küçükten Büyüğe)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Son Güncellenme")

    class Meta:
        verbose_name = "Proje"
        verbose_name_plural = "Projeler"
        ordering = ['display_order', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:project_detail', kwargs={'slug': self.slug})

    def get_technologies_list(self):
        """Virgülle ayrılmış teknolojileri şablonlarda rozet olarak dökmek için listeye çevirir."""
        if not self.technologies:
            return []
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]


class Experience(models.Model):
    """
    İş deneyimleri ve aday mühendislik / staj çalışmaları.
    """
    title = models.CharField(max_length=200, verbose_name="Pozisyon / Rol")
    organization = models.CharField(max_length=200, verbose_name="Kurum / Şirket Adı")
    location = models.CharField(max_length=100, blank=True, verbose_name="Konum / Şehir")
    date_text = models.CharField(max_length=100, blank=True, verbose_name="Tarih Aralığı (Örn: Eylül 2024 – Aralık 2024)")
    description = models.TextField(verbose_name="Açıklama ve Sorumluluklar")
    start_date = models.DateField(blank=True, null=True, verbose_name="Başlangıç Tarihi")
    end_date = models.DateField(blank=True, null=True, verbose_name="Bitiş Tarihi")
    is_current = models.BooleanField(default=False, verbose_name="Halen Devam Ediyor mu?")
    display_order = models.PositiveIntegerField(default=0, verbose_name="Görüntülenme Sırası")

    class Meta:
        verbose_name = "Deneyim"
        verbose_name_plural = "Deneyimler"
        ordering = ['display_order', '-start_date']

    def __str__(self):
        return f"{self.title} - {self.organization}"

    def get_bullet_points(self):
        """Açıklamadaki her satırı ayrı bir madde imi olarak döner."""
        return [line.strip().lstrip('-•* ') for line in self.description.splitlines() if line.strip()]


class Education(models.Model):
    """
    Lisans ve lise akademik eğitim geçmişi.
    """
    institution = models.CharField(max_length=200, verbose_name="Eğitim Kurumu / Üniversite")
    degree = models.CharField(max_length=200, verbose_name="Derece / Bölüm")
    faculty = models.CharField(max_length=200, blank=True, verbose_name="Fakülte")
    gpa = models.CharField(max_length=50, blank=True, verbose_name="Not Ortalaması / GANO / Mezuniyet Derecesi")
    location = models.CharField(max_length=100, blank=True, verbose_name="Konum / Şehir")
    date_text = models.CharField(max_length=100, blank=True, verbose_name="Yıllar (Örn: 2021 – 2025)")
    description = models.TextField(blank=True, verbose_name="Açıklama / Detay")
    start_date = models.DateField(blank=True, null=True, verbose_name="Başlangıç Tarihi")
    end_date = models.DateField(blank=True, null=True, verbose_name="Mezuniyet / Bitiş Tarihi")
    display_order = models.PositiveIntegerField(default=0, verbose_name="Görüntülenme Sırası")

    class Meta:
        verbose_name = "Eğitim"
        verbose_name_plural = "Eğitimler"
        ordering = ['display_order', '-end_date']

    def __str__(self):
        return f"{self.degree} ({self.institution})"


class Certificate(models.Model):
    """
    Mesleki eğitim, yetkinlik ve sertifikalar.
    """
    name = models.CharField(max_length=250, verbose_name="Sertifika / Eğitim Adı")
    issuer = models.CharField(max_length=200, verbose_name="Veren Kurum")
    description = models.TextField(blank=True, verbose_name="Açıklama / Kazanılan Beceriler")
    issue_date = models.DateField(blank=True, null=True, verbose_name="Veriliş Tarihi")
    credential_url = models.URLField(blank=True, verbose_name="Doğrulama Bağlantısı (Varsa)")
    certificate_no = models.CharField(max_length=100, blank=True, verbose_name="Sertifika Numarası (Varsa)")
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True, verbose_name="Sertifika Belgesi (PDF/Resim)")
    display_order = models.PositiveIntegerField(default=0, verbose_name="Görüntülenme Sırası")
    is_published = models.BooleanField(default=True, verbose_name="Yayınlandı mı?")

    class Meta:
        verbose_name = "Sertifika"
        verbose_name_plural = "Sertifikalar"
        ordering = ['display_order', '-issue_date']

    def __str__(self):
        return f"{self.name} - {self.issuer}"
