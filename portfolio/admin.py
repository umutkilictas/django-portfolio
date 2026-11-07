from django.contrib import admin
from .models import Project, Experience, Education, Certificate

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'is_published', 'display_order', 'created_at')
    list_filter = ('is_published', 'featured', 'created_at')
    search_fields = ('title', 'short_description', 'description', 'technologies')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('featured', 'is_published', 'display_order')
    ordering = ('display_order', '-created_at')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'location', 'date_text', 'is_current', 'display_order')
    list_filter = ('is_current', 'organization')
    search_fields = ('title', 'organization', 'description')
    list_editable = ('display_order', 'is_current')
    ordering = ('display_order', '-start_date')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'gpa', 'date_text', 'display_order')
    search_fields = ('degree', 'institution', 'description')
    list_editable = ('display_order',)
    ordering = ('display_order', '-end_date')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'certificate_no', 'issue_date', 'is_published', 'display_order')
    list_filter = ('is_published', 'issuer')
    search_fields = ('name', 'issuer', 'certificate_no', 'description')
    list_editable = ('is_published', 'display_order')
    ordering = ('display_order', '-issue_date')
