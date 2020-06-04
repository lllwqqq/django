from django.contrib import admin
from .models import Post, Category, Tag


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time']
    fields = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time']
    fields = ['name']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
