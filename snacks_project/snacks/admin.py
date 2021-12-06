from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Snack
# Register your models here.

@admin.register(Snack)
class AdminClass(admin.ModelAdmin):
    list_display  = ['name',"purchaser","description"]
    search_fields = ["name"]
# admin.site.register(Snack)



