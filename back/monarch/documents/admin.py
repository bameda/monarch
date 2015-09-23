from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("subject", ("author", "creation_date"))}),
        (_("Info"), {"fields": ("file", "description", )}),
    )
    list_display = ("id", "subject", "author", "creation_date")
    list_filter = ("creation_date",)
    search_fields = ("subject", "description",  "author__email", "author__username", "author__full_name")
    ordering = ("-creation_date",)

