from django.contrib import admin
from blog_dev.models import Blog_en, Keyword

class Blog_enAdmin(admin.ModelAdmin):
    filter_horizontal = ('keywords',)

admin.site.register(Blog_en, Blog_enAdmin)
admin.site.register(Keyword)
