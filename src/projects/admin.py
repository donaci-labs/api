from django.contrib import admin

from .models import Project, ProjectImage, Transaction


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'published',)

    inlines = [
        ProjectImageInline,
    ]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_filter = ('project', 'status',)
