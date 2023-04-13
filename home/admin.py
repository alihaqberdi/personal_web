from django.contrib import admin
from .models import Portfolio, Images
# Register your models here.




class ImagesAdmin(admin.TabularInline):
    model = Images


class Portfolioadmin(admin.ModelAdmin):
    inlines = [
                ImagesAdmin
               ]

admin.site.register(Portfolio,Portfolioadmin)
# admin.site.register((Blog, Contact, Skills))
# admin.site.register((Portfolio))