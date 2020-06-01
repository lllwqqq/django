from django.contrib import admin
from .models import Post, Category, Tag


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'excerpt', 'create_time', 'modified_time', 'author']
    fields = ['title', 'excerpt', 'body', 'category', 'tag']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
