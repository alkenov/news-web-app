from django.contrib import admin

from .models import Articles, Category, Tag

admin.site.register(Articles)
admin.site.register(Category)
admin.site.register(Tag)
