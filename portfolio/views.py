from django.shortcuts import render, get_object_or_404
from .models import Project, Experience, Education, Certificate

def home_view(request):
    """
    Ana sayfa: Karşılama, öne çıkan projeler (en fazla 3 adet),
    özet eğitim ve sertifikalar.
    """
    featured_projects = Project.objects.filter(is_published=True, featured=True)[:3]
    recent_education = Education.objects.all()[:2]
    recent_certificates = Certificate.objects.filter(is_published=True)[:2]

    context = {
        'featured_projects': featured_projects,
        'recent_education': recent_education,
        'recent_certificates': recent_certificates,
    }
    return render(request, 'portfolio/home.html', context)


def about_view(request):
    """
    Hakkımda sayfası: Detaylı özgeçmiş ve teknik ilgi alanları.
    """
    return render(request, 'portfolio/about.html')


def project_list_view(request):
    """
    Tüm yayınlanmış projelerin listelendiği sayfa.
    """
    projects = Project.objects.filter(is_published=True)
    return render(request, 'projects/project_list.html', {'projects': projects})


def project_detail_view(request, slug):
    """
    Tekil proje detay sayfası.
    Yalnızca yayınlanmış projeler erişilebilir; aksi takdirde 404 döner.
    """
    project = get_object_or_404(Project, slug=slug, is_published=True)
    return render(request, 'projects/project_detail.html', {'project': project})


def experience_view(request):
    """
    Deneyim ve eğitim sayfası.
    """
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    context = {
        'experiences': experiences,
        'educations': educations,
    }
    return render(request, 'portfolio/experience.html', context)


def certificates_view(request):
    """
    Yayınlanmış sertifikaların listelendiği sayfa.
    """
    certificates = Certificate.objects.filter(is_published=True)
    return render(request, 'portfolio/certificates.html', {'certificates': certificates})


def contact_view(request):
    """
    İletişim sayfası.
    """
    return render(request, 'portfolio/contact.html')


def custom_404_view(request, exception=None):
    """
    Özel 404 Sayfa Bulunamadı şablonu.
    """
    return render(request, '404.html', status=404)
