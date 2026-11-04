from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('hakkimda/', views.about_view, name='about'),
    path('projeler/', views.project_list_view, name='project_list'),
    path('projeler/<slug:slug>/', views.project_detail_view, name='project_detail'),
    path('deneyim-egitim/', views.experience_view, name='experience'),
    path('sertifikalar/', views.certificates_view, name='certificates'),
    path('iletisim/', views.contact_view, name='contact'),
]
