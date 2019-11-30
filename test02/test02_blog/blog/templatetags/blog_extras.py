from ..models import Post, Category, Tag
from django import template

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_posts_list': Post.objects.all().order_by('-create_time')[:num]
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'archives': Post.objects.dates(field_name='create_time', kind='month', order='DESC')
    }


@register.inclusion_tag(filename='blog/inclusions/_categories.html', takes_context=True)
def show_tags(context):
    return {
        'tags': Tag.objects.all()
    }


@register.inclusion_tag(filename='blog/inclusions/_categories.html', takes_context=True)
def show_categories(context,num=5):
    return {
        'categories': Category.objects.all()[:num]
    }
