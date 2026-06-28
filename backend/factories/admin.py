from django.contrib import admin
from .models import Factory


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "industry_type",
        "location",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "code",
        "industry_type",
    )

    list_filter = (
        "industry_type",
        "is_active",
    )

    ordering = ("name",)