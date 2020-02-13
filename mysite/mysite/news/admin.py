from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Articles, Category, Tag, Comments

class ArticlesAdmin(SummernoteModelAdmin):
    summernote_fields = ('post', 'description')



admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Category)
admin.site.register(Tag)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')

admin.site.register(Comments, CommentAdmin)