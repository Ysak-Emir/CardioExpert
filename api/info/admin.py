from django.contrib import admin
from api.info.models import CategoryInformation, SubcategoryInformation


class CategoryInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "title_rus", "title_kz")
    list_display_links = ("id", "title_rus", "title_kz")
    search_fields = ("title_rus", "title_kz", )


class SubcategoryInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "profile_picture", "block", "title_rus", "title_kz", "description_rus", "description_kz")
    list_display_links = ("id", "title_rus", "title_kz")
    search_fields = ("block_title", "title_rus",)


admin.site.register(CategoryInformation, CategoryInfoAdmin)
admin.site.register(SubcategoryInformation, SubcategoryInfoAdmin)
