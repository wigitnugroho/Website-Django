from django.contrib import admin

# Register your models here.
from.models import Artikel

class ArtikelAdmin(admin.ModelAdmin):
  read_only_fields =[
  "slug",
  'updated',
  'published',

  ]

admin.site.register(Artikel, ArtikelAdmin)