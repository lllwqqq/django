from django.contrib import admin
from .models import Comments


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_time']
    fields = ['name', 'email', 'url', 'text', 'post']


admin.site.register(Comments,CommentAdmin)