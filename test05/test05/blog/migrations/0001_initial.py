# Generated by Django 2.2.3 on 2019-12-20 03:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('excerpt', models.CharField(max_length=200, verbose_name='摘要')),
                ('body', models.TextField(verbose_name='正文')),
                ('create_time', models.DateField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('modified_time', models.DateField(verbose_name='修改时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='分类')),
                ('tag', models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]
