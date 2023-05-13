from django.contrib import admin

# Register your models here.

from . models import Post, Kategori

class TampilKategori(admin.ModelAdmin) : 
    list_display = ('judul','kategori')
    list_display_links = (None)

admin.site.register(Post, TampilKategori)
admin.site.register(Kategori)