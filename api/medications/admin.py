from django.contrib import admin
from api.medications.models import *


class MedicationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "dosage", "time")
    list_display_links = ("id", "title")
    search_fields = ("title", "dosage", )
    list_per_page = 12


admin.site.register(Medication, MedicationAdmin)