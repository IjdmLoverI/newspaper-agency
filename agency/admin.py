from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from agency.models import Redactor, Newspaper, Topic


@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional Information", {"fields": ("years_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (("Additional Information", {"fields": ("years_of_experience")}))
    )


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("pub_date",)


admin.site.register(Topic)
