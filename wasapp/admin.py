from django.contrib import admin

# Register your models here.

from .models import waitingperson
@admin.register(waitingperson)
class waitingpersonAdmin(admin.ModelAdmin):
    pass