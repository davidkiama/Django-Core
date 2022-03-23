from django.contrib import admin

from .models import Editor, Article, Tags
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Editor)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tags)
