from django.contrib import admin
from api.info.models import CategoryInformation, SubcategoryInformation


class CategoryInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)


class SubcategoryInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "profile_picture", "block", "title", "description")
    list_display_links = ("id", "title")
    search_fields = ("block_title", "title",)


admin.site.register(CategoryInformation, CategoryInfoAdmin)
admin.site.register(SubcategoryInformation, SubcategoryInfoAdmin)
