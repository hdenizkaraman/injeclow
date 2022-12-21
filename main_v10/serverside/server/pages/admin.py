from django.contrib import admin
from . models import Hareket
# Register your models here.
@admin.register(Hareket)
class HareketAdmin(admin.ModelAdmin):
    list_display = ["name",]
    prepopulated_fields = {"slug":('name',)}
