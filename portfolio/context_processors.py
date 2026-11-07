from django.conf import settings

def portfolio_context(request):
    """
    Şablonların tümünde (özellikle navbar ve footer) ortak olarak kullanılabilen
    site sahibi ve sosyal bağlantı bilgileri.
    """
    return {
        'SITE_OWNER': getattr(settings, 'PORTFOLIO_OWNER', 'Umut Kılıçtaş'),
        'GITHUB_URL': getattr(settings, 'PORTFOLIO_GITHUB_URL', 'https://github.com/umutkilictas'),
        'LINKEDIN_URL': getattr(settings, 'PORTFOLIO_LINKEDIN_URL', 'https://linkedin.com/in/umut-kilictas'),
        'CONTACT_EMAIL': getattr(settings, 'PORTFOLIO_EMAIL', ''),
    }
