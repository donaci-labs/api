from django.contrib import admin

from .models import Project, ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
