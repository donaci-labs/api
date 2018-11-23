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

    def formated_amount(self, obj):
        return 'R$ {}'.format(obj.amount)
    formated_amount.short_description = 'amount'

    list_display = ('project', 'transaction_id', 'formated_amount',)
    list_filter = ('project', 'status',)
