from django.contrib import admin

from api.users.models import User


class UsersAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "email",
                    "name",
                    "surname",
                    "age",
                    "doctor",
                    "number",
                    "is_active",
                    "is_staff",
                    "is_superuser",)
    list_display_links = ("id", "email", "name", "surname")
    search_fields = ("email", "name", "surname", "age", )
    list_per_page = 12


admin.site.register(User, UsersAdmin)
